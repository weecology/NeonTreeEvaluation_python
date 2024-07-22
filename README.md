# Deprecation Notice.

This project is not mantained. For scores against the NeonTreeEvaluation benchmark use the R package: https://github.com/weecology/NeonTreeEvaluation_package. For python users looking to evaluate against the DeepForest model, use the DeepForest python package: https://deepforest.readthedocs.io/en/latest/

# A multi-sensor benchmark dataset for detecting individual trees in airborne RGB, Hyperspectral and LiDAR point clouds

[![Travis-CI Build
Status](https://travis-ci.org/Weecology/neontreeevaluation_python.svg?branch=master)](https://travis-ci.org/Weecology/neontreeevaluation_python)

Maintainers: Dylan Stewart and Ben Weinstein - University of Florida.

# Paper and Citation

https://www.biorxiv.org/content/10.1101/2020.11.16.385088v1

Broad scale remote sensing promises to build forest inventories at unprecedented scales. A crucial step in this process is designing individual tree segmentation algorithms to associate pixels into delineated tree crowns. While dozens of tree delineation algorithms have been proposed, their performance is typically not compared based on standard data or evaluation metrics, making it difficult to understand which algorithms perform best under what circumstances. There is a need for an open evaluation benchmark to minimize differences in reported results due to data quality, forest type and evaluation metrics, and to support evaluation of algorithms across a broad range of forest types. Combining RGB, LiDAR and hyperspectral sensor data from the National Ecological Observatory Network’s Airborne Observation Platform with multiple types of evaluation data, we created a novel benchmark dataset to assess individual tree delineation methods. This benchmark dataset includes an R package to standardize evaluation metrics and simplify comparisons between methods. The benchmark dataset contains over 6,000 image-annotated crowns, 424 field-annotated crowns, and 3,777 overstory stem points from a wide range of forest types. In addition, we include over 10,000 training crowns for optional use. We discuss the different evaluation sources and assess the accuracy of the image-annotated crowns by comparing annotations among multiple annotators as well as to overlapping field-annotated crowns. We provide an example submission and score for an open-source baseline for future methods.


* Free software: MIT license
* This package is a port of the R package: https://github.com/weecology/NeonTreeEvaluation_package

# Installation

This repo uses conda to manage dependencies

```
git clone https://github.com/weecology/NeonTreeEvaluation_python.git
cd NeonTreeEvaluation_python
conda create env -f=environment.yml 
conda activate NeonTreeEvaluation
```

# Download sensor data

To download evaluation data from the Zenodo archive (1GB), use the download() function to place the data in the correct package location.

```
from src import download
download()
```

This will download the image-annotations as well as the remote sensing data to the data/ folder of this repo.

# Submission Format

The format of the submission a

* A csv file
* 5 required columns: plot_name, xmin, ymin, xmax, ymax

Each row contains information for one predicted bounding box.

The plot_name column should be named the same as the files in the dataset without extension (e.g. SJER_021 not SJER_021.tif) and not the full path to the file on disk. Not all evaluation data are available for all plots. Functions like evaluate_field_crowns and evaluate_image_crowns will look for matching plot name and ignore other plots.Depending on the speed of the algorithm, the simplest thing to do is predict all images in the RGB folder and the package will handle matching images with the correct data to the correct evaluation procedure.

## Scores for an image-annotated crowns

The main data source are image-annotated crowns, in which a single observer annotated visible trees in 200 40m x 40m images from across the United States. This submission has bounding boxes in image coordinates. To get the benchmark score image-annotated ground truth data.

```
#Get a three sample plots to run quickly, ignore to run the entire dataset
import pandas as pd
from src.eval import evaluate_image_crowns

submission = pd.read_csv("data/submission.csv")
df = submission[submission.plot_name.isin(["SJER_052","TEAK_061","TEAK_057"])]

#Compute total recall and precision for the overlap data
results = evaluate_image_crowns(df = df,project = True, show=False)
results
```

## Scores for an field-annotated crowns

The second data source is a small number of field-deliniated crowns from three geographic sites. These crowns were drawn on a tablet while physically standing in the field, thereby reducing the uncertainty in crown segmentation.

```
import pandas as pd
from src.eval import evaluate_field_crowns

submission = pd.read_csv("data/submission.csv")
df = submission[submission.plot_name.isin(["OSBS_095_competition"])]

#Compute total recall and precision for the overlap data
results = evaluate_field_crowns(df = df,project = True, show=False)

results
```

## Scores for an field-collected stems [not yet implemented]

The third data source is the NEON Woody Vegetation Structure Dataset. Each tree stem is represented by a single point. This data has been filtered to represent overstory trees visible in the remote sensing imagery. This evaluation metric is evaluable in the R package (see above), but has not yet been ported to the python package.
