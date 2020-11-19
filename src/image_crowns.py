"""
Evaluation module
"""
from src.utilities import project_submission
from src import get_data
from src import IoU
from matplotlib import pyplot

def image_crowns(df, project, show):
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
    
    ground_truth = get_data.load_ground_truth(plot_name)
    rgb_image = get_data.load_rgb_image(plot_name)
    
    if project:
        df = utilities.project_submission(df)
    
    #match  
    result = IoU.compute_precision_recall(ground_truth, df)
    
    if show:
        ax = pyplot.imshow(rgb_image)
        ground_truth.plot(ax=ax, color="red",fill=None)
        df.plot(ax=ax,color="blue",fill=None)
    
    return result