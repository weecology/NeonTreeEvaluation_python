import pytest
import os
from src import get_data

def test_find_path():
    path = get_data.find_path(plot_name = "SJER_052", datatype ="rgb", base_dir="tests/data/")
    assert os.path.exists(path)
    
    path = get_data.find_path(plot_name = "SJER_052", datatype ="lidar", base_dir="tests/data/")
    assert os.path.exists(path)
    
    path = get_data.find_path(plot_name = "SJER_052", datatype ="annotations", base_dir="tests/data/")
    assert os.path.exists(path)
   
    path = get_data.find_path(plot_name = "SJER_052", datatype ="chm", base_dir="tests/data/")
    assert os.path.exists(path)
    
    path = get_data.find_path(plot_name = "SJER_052", datatype ="hyperspectral", base_dir="tests/data/")
    assert os.path.exists(path)    
            
    