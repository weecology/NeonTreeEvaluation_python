"""
Utilities module
"""
import os
import rasterio

def check_submission(df):
    """
    Ensure the submission is correctly formatted
    Args:
        df: a pandas dataframe
    Returns:
        None: Error is raised if format assertions are not met
    """    
    if not all([x in df.columns for x in ["plot_name","xmin","xmax","ymin","ymax"]]):
        raise ValueError("Incorrect column specifications, required columns are plot_name, xmin, xmax, ymin, ymax. Found {}".format(df.columns))

    #Check valid polygons?
    #if not test_poly.is_valid:
        #test_poly = test_poly.buffer(0.0)
        
def check_download():
    """
    Ensure evaluation data has been downloaded from Zenodo
    """
    #To allow testing, looking for an env var
    if "NEONTREEEVALUATION_DIR" in os.environ:
        data_dir = os.environ["NEONTREEEVALUATION_DIR"]
    else:
        data_dir = "data/NeonTreeEvaluation"
    
    if os.path.exists(data_dir):
        return True
    else:
        return False

def project_submission(df):
    """Convert from image coordinates to geopgraphic cooridinates
    Note that this assumes df is just a single plot being passed to this function
    """
    plot_names = df.plotname.unique()
    if len(plot_names) > 1:
        raise ValueError("This function projects a single plots worth of data. Multiple plot names found {}".format(plot_names))
    else:
        plot_name = plot_names[0]
    
    rgb_path = get_data.find_path(plot_name, "rgb")
    rgb_src = rasterio.open(rgb_path)
    
    #TO DO project
    