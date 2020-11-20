"""
Evaluation module
"""
import numpy as np
from matplotlib import pyplot
import rasterio.plot

from src.utilities import project_boxes
from src import get_data
from src import IoU

def field_crowns(df, project, show):
    """
    df: a pandas dataframe with columns plot_name, xmin, xmax, ymin, ymax
    show: Whether to show boxes as they are plotted
    summarize: Whether to group statistics by plot and overall score
    project: Whether to compute summary statistics (TRUE) or return raw matching data (False)
    """
    plot_names = df.plot_name.unique()
    if len(plot_names) > 1:
        raise ValueError("More than one plot passed to image crown: {}".format(plot_name))
    else:
        plot_name = plot_names[0]
    
    ground_truth = get_data.load_field_crown(plot_name)    
    ground_truth = ground_truth.reset_index(drop=True)
    
    df = project_boxes(df, transform = project)
    
    if show:
        rgb_path = get_data.find_path(plot_name, data_type="rgb")
        rgb_src = rasterio.open(rgb_path)        
        fig, ax = pyplot.subplots(figsize=(6, 6))
        rasterio.plot.show(rgb_src, ax = ax)
        ground_truth.geometry.boundary.plot(color="red", ax = ax)
        df.geometry.boundary.plot(ax=ax,color="blue")
        
    #match  
    result = IoU.compute_IoU(ground_truth, df)
    
    return result