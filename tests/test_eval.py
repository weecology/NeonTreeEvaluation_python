from src import eval
import os
import pytest
import pandas as pd

#Set testing env
os.environ["NEONTREEEVALUATION_DIR"] = "{}/data/".format(os.path.dirname(__file__))

@pytest.fixture()
def submission():
    """Sample data submission"""
    submission = pd.read_csv("data/submission.csv")
    #Just take a small chunk for testing
    submission = submission[submission.plot_name=="SJER_052"]
    
    return submission

def test_evaluate_image_crowns(submission):
    recall, precision = eval.evaluate_image_crowns(df = submission, project=True)
    
    assert (recall > 0 & recall < 1)
    assert (precision > 0 & precision < 1)
    
