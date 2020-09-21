#test_download
import os
from src import download

def test_download():
    download.download()
    basedir = os.path.dirname(os.path.dirname(download.__file__))
    datadir = "{}/{}".format(basedir, "data")     
    assert os.path.exists("{}/evaluation/".format(datadir))
    assert os.path.exists("{}/annotations/".format(datadir))
