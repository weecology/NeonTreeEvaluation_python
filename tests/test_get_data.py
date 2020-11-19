import pytest
import os
from src import get_data
import numpy as np


def test_find_path():
    path = get_data.find_path(plot_name = "SJER_052", data_type ="rgb", base_dir="tests/data/")
    assert os.path.exists(path)
    
    path = get_data.find_path(plot_name = "SJER_052", data_type ="lidar", base_dir="tests/data/")
    assert os.path.exists(path)
    
    path = get_data.find_path(plot_name = "SJER_052", data_type ="annotations", base_dir="tests/data/")
    assert os.path.exists(path)
   
    path = get_data.find_path(plot_name = "SJER_052", data_type ="chm", base_dir="tests/data/")
    assert os.path.exists(path)
    
    path = get_data.find_path(plot_name = "SJER_052", data_type ="hyperspectral", base_dir="tests/data/")
    assert os.path.exists(path)    
            
def test_xml_parse():
    path = get_data.find_path(plot_name = "SJER_052", data_type ="annotations", base_dir="tests/data/")
    df  = get_data.xml_parse(path)
    assert np.array_equal(df.columns.values,np.array(["xmin","xmax","ymin","ymax","plot_name"]))