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
    
    assert recall == 7/9
    assert precision == 7/7

def test_evaluate_field_crowns(submission):
    submission = pd.read_csv("data/submission.csv")
    submission = submission[submission.plot_name == "OSBS_95_competition"]
    
    recall, precision = eval.evaluate_field_crowns(df = submission, project=True, show=True)
    
    assert recall == 1.0
