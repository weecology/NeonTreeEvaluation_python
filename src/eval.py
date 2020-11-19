"""
Evaluation module
"""
import pandas as pd
from src.utilities import check_submission, check_download
from src.image_crowns import image_crowns

def evaluate_image_crowns(path=None, df = None, shp=None, project=False, show=True):
    """Image annotated crown evaluation routine
    submission can be submitted as a .shp, existing pandas dataframe or .csv path
    path: path to .csv on disk
    df: a pandas dataframe
    shp: path to a polygon shp 
    show: Whether to show boxes as they are plotted
    project: Whether to compute summary statistics (TRUE) or return raw matching data (False)
    """
    if not check_download():
        raise ValueError("Evaluation data has not been downloaded. The data is large and kept seperate from the python package. use download() to place the data in the data/ directory")
    
    if path:
        df = pd.read_csv(path)
    if shp:
        df = gpd.read_file(shp)
    if all([x is None for x in [path,df,shp]]):
        raise ValueError("No submission found. Submission must be provided as pandas df, .csv path or shapefile.")
    
    check_submission(df)
    
    #Run evaluation on all plots
    results = df.groupby("plot_name").apply(lambda x: image_crowns(df =x, project=project, show=show))
    
    results["match"] = results.IoU > iou_threshold
    true_positive = sum(results["match"] == True)
    recall = true_positive / ground_truth.shape[0]
    precision = true_positive / submission.shape[0]
    
    return recall, precision

def evaluate_field_crowns(path=None, df = None):
    check_download()    
    check_submission(df)

def evaluate_field_stems(path=None, df= None):
    check_download()    
    check_submission(df)