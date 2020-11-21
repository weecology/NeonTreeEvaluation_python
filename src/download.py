## Module to download annotation and evaluation data from NeonTreeEvaluation benchmark. 
import os
import subprocess
import zipfile
import glob
import shutil  

def download():
    """Download data from zenodo. 
    The NeonTreeEvaluation benchmark consists of two parts:
    1) package code to run evaluation workflows
    2) evaluation data. Evaluation data is ~ 2GB in size and will be downloaded to package contents.
"""
    basedir = os.path.dirname(os.path.dirname(__file__))
    print(basedir)
    datadir = os.path.join(basedir,"data/NeonTreeEvaluation/")
    print("Downloading data files to {}".format(datadir))    
    eval_url = zenodo_url(concept_rec_id="3723356", datadir=datadir)
    
def zenodo_url(concept_rec_id, datadir):
    subprocess.call(["zenodo_get", concept_rec_id, "-e","-o", datadir])
    file = glob.glob("{}/NeonTreeEvaluation*.zip".format(datadir))[0]
    if os.path.exists(file):
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(datadir)
    else:
        raise IOError("Cannot find zip file in {}".format(datadir))
    os.remove(file)


    
    
