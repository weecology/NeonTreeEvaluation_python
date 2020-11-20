"""Get data module. Given a plot name, recover the correct data"""

import os
import geopandas as gpd
import pandas_read_xml as pdx
import pandas as pd
import rasterio

from src import get_data
from src import utilities

def find_path(plot_name, data_type):
    """Given a plot name recover the location on disk of the correct path"""
    
    #To allow testing, looking for an env var
    if "NEONTREEEVALUATION_DIR" in os.environ:
        base_dir = os.environ["NEONTREEEVALUATION_DIR"]
    else:
        base_dir = "data/"
        
    if data_type == "rgb":
        return "{}/NeonTreeEvaluation/evaluation/RGB/{}.tif".format(base_dir, plot_name)
    elif data_type == "lidar":
        return "{}/NeonTreeEvaluation/evaluation/LiDAR/{}.laz".format(base_dir, plot_name)
    elif data_type == "hyperspectral":
        return "{}/NeonTreeEvaluation/evaluation/Hyperspectral/{}_hyperspectral.tif".format(base_dir, plot_name)
    elif data_type == "annotations":
        return "{}/NeonTreeEvaluation/annotations/{}.xml".format(base_dir, plot_name)
    elif data_type == "chm":
        return "{}/NeonTreeEvaluation/evaluation/CHM/{}_CHM.tif".format(base_dir, plot_name)        

def xml_parse(path):
    """Parse a xml annotation and return a pandas df"""
    
    plot_name = os.path.basename(path)
    plot_name = plot_name.split(".")[0]
    
    df = pdx.read_xml(path, ["annotation","object"])
    xmin = df.bndbox.apply(lambda x: x["xmin"])
    xmax = df.bndbox.apply(lambda x: x["xmax"])
    ymin = df.bndbox.apply(lambda x: x["ymin"])
    ymax = df.bndbox.apply(lambda x: x["ymax"])
    
    result = pd.DataFrame({"xmin":xmin, "xmax":xmax, "ymin":ymin, "ymax":ymax, "plot_name":plot_name})
    return result

    
def load_ground_truth(plot_name):
    """Load annotation and return projected data"""
    xml_path = get_data.find_path(plot_name, "annotations")
    ground_truth = xml_parse(xml_path)
    
    #convert to geopandas
    geo_ground_truth = utilities.project_boxes(ground_truth)
    
    return geo_ground_truth

def load_field_crown(plot_name):
    """Load annotation and return projected data"""
    field_data = gpd.read_file("data/field_crowns.shp")
    plot_name = plot_name.replace("_competition","")
    plot_data = field_data[field_data.plotID == plot_name]
    return plot_data

def load_rgb_image(plot_name):
    path = find_path(plot_name,data_type="rgb")
    src = rasterio.open(path)
    image = src.read()
    
    return image
