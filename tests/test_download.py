#test_download
import os
from src import download

is_travis = 'TRAVIS' in os.environ
@pytest.mark.skipif(is_travis, reason="Cannot load comet on TRAVIS")
def test_download():
    download.download()
    basedir = os.path.dirname(os.path.dirname(download.__file__))
    datadir = "{}/{}".format(basedir, "data")     
    assert os.path.exists("{}/evaluation/".format(datadir))
    assert os.path.exists("{}/annotations/".format(datadir))
