import pytest
import os
from src import get_data
import numpy as np

#set test env
os.environ["NEONTREEEVALUATION_DIR"] = "{}/data/".format(os.path.dirname(__file__))


def test_find_path():
    path = get_data.find_path(plot_name = "SJER_052", data_type ="rgb")
    assert os.path.exists(path)
    
    path = get_data.find_path(plot_name = "SJER_052", data_type ="lidar")
    assert os.path.exists(path)
    
    path = get_data.find_path(plot_name = "SJER_052", data_type ="annotations")
    assert os.path.exists(path)
   
    path = get_data.find_path(plot_name = "SJER_052", data_type ="chm")
    assert os.path.exists(path)
    
    path = get_data.find_path(plot_name = "SJER_052", data_type ="hyperspectral")
    assert os.path.exists(path)    
            
def test_xml_parse():
    path = get_data.find_path(plot_name = "SJER_052", data_type ="annotations")
    df  = get_data.xml_parse(path)
    assert np.array_equal(df.columns.values,np.array(["xmin","xmax","ymin","ymax","plot_name"]))