# A multi-sensor benchmark dataset for detecting individual trees in airborne RGB, Hyperspectral and LiDAR point clouds

[![Travis-CI Build
Status](https://travis-ci.org/Weecology/neontreeevaluation_python.svg?branch=master)](https://travis-ci.org/Weecology/neontreeevaluation_python)

Maintainers: Dylan Stewart and Ben Weinstein - University of Florida.

This benchmark dataset contains a consistent annotation approach across a variety of ecosystems.

* Free software: MIT license
* Documentation: https://neontreeevaluation-python.readthedocs.io.
* This package is a port of the R package: https://github.com/weecology/NeonTreeEvaluation_package

# Installation

# Download sensor data

To download evaluation data from the Zenodo archive (1GB), use the download() function to place the data in the correct package location.

```
from src import download
download()
```

This will download the image-annotations as well as the remote sensing data to the data/ folder of this repo.

# Submission Format

The format of the submission is as follows

* A csv file
* 5 columns: Plot Name, xmin, ymin, xmax, ymax

Each row contains information for one predicted bounding box.

The plot column should be named the same as the files in the dataset without extension (e.g. SJER_021 not SJER_021.tif) and not the full path to the file on disk. Not all evaluation data are available for all plots. Functions like evaluate_field_crowns and evaluate_image_crowns will look for matching plot name and ignore other plots.Depending on the speed of the algorithm, the simplest thing to do is predict all images in the RGB folder and the package will handle matching images with the correct data to the correct evaluation procedure.

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
``

For a list of NEON site abbreviations: https://www.neonscience.org/field-sites/field-sites-map


## Scores for an field-annotated crowns

The second data source is a small number of field-deliniated crowns from three geographic sites. These crowns were drawn on a tablet while physically standing in the field, thereby reducing the uncertainty in crown segmentation.

```
#Get a three sample plots to run quickly, ignore to run the entire dataset
import pandas as pd
from src.eval import evaluate_field_crowns

submission = pd.read_csv("data/submission.csv")
df = submission[submission.plot_name.isin(["OSBS_095_competition"])]

#Compute total recall and precision for the overlap data
results = evaluate_field_crowns(df = df,project = True, show=False)
results
``

## Scores for an field-collected stems [not yet implemented]
The third data source is the NEON Woody Vegetation Structure Dataset. Each tree stem is represented by a single point. This data has been filtered to represent overstory trees visible in the remote sensing imagery. This evaluation metric is evaluable in the R package (), but has not yet been ported to the python package.
