from src import utilities
import pandas as pd
import pytest

def test_check_download():
    pass

def test_check_submission():
    df = pd.DataFrame({"p_name": ["OSBS_017"] ,"xmin":[100]})
    with pytest.raises(ValueError):
        utilities.check_submission(df)
        
    df = pd.DataFrame({"plot_name": ["OSBS_017"] ,"xmin":[100],"xmax":[100],"ymax":[90],"ymin":[85]})
    utilities.check_submission(df)    