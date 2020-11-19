"""Get data module. Given a plot name, recover the correct data"""
from src import get_data

def find_path(plot_name, data_type, base_dir = "data"):
    """Given a plot name recover the location on disk of the correct path"""
    
    if data_type == "rgb":
        return "{}/NeonTreeEvaluation/evaluation/RGB/{}.tif".format(base_dir, plot_name)
    elif data_type == "lidar":
        return "{}/NeonTreeEvaluation/evaluation/LiDAR/{}.laz".format(base_dir, plot_name)
    elif data_type == "hyperspectral":
        return "{}/NeonTreeEvaluation/evaluation/Hyperspectral/{}.tif".format(base_dir, plot_name)
    elif data_type == "annotations":
        return "{}/NeonTreeEvaluation/annotations/{}.xml".format(base_dir, plot_name)
    elif data_type == "chm":
        return "{}/NeonTreeEvaluation/evaluation/CHM/{}.tif".format(base_dir, plot_name)        
    
def load_ground_truth(plot_name):
    xml_path = get_data.find_path(plot_name, "annotations")
    ground_truth = xml_parse(xml_path)
    
    return ground_truth

def load_rgb(plot_name):
    path = find_path(plot_name,data_type="rgb")
    src = rasterio.open(path)
    image = src.read()
    
    return image
