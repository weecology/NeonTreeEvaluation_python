# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:53:40 2020

@author: d.stewart
"""
import geopandas as gp
import pandas as pd
import numpy as np
import rasterio
import glob, os
import fiona
from shapely.geometry import shape, Polygon


def bb_intersection_over_union(boxAA, boxBB):
    # recalculate vertices for box a and b from length weight
    boxA = boxAA.copy()
    boxB = boxBB.copy()
    boxA[2] = boxA[0] + boxA[2]
    boxA[3] = boxA[1] + boxA[3]
    boxB[2] = boxB[0] + boxB[2]
    boxB[3] = boxB[1] + boxB[3]
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = abs(max((xB - xA, 0)) * max((yB - yA), 0))
    if interArea == 0:
        return 0
    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = abs((boxA[2] - boxA[0]) * (boxA[3] - boxA[1]))
    boxBArea = abs((boxB[2] - boxB[0]) * (boxB[3] - boxB[1]))

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = interArea / float(boxAArea + boxBArea - interArea)

    # return the intersection over union value
    return iou

def get_vertex_per_plot(pl):
    pix_per_meter = 10
    detection_path = 'submission.csv'
    ras_path = "./tests/data/evaluation/RGB2/" + pl
    # read plot raster to extract detections within the plot boundaries
    raster = rasterio.open(ras_path)
    true_path = "./data/OSBS_field_polygons_2019_final.shp"
    gdf = gp.read_file(detection_path)
    gdf = gdf.loc[gdf['plot_name']==pl[:-4]]
    gtf = gp.read_file(true_path, bbox=raster.bounds)
    
    # turn WTK into coordinates within in the image
    # gtf_limits = gtf.bounds
    
    xmin = raster.bounds[0]
    ymin = raster.bounds[1]
    
    updatedgdf = []
    for p in range(len(gdf)):
        xmint,ymint,xmaxt,ymaxt = gdf.iloc[p]['xmin'],gdf.iloc[p]['ymin'],gdf.iloc[p]['xmax'],gdf.iloc[p]['ymax']
        x = np.array([xmint,xmaxt,xmaxt,xmint]).astype(float)
        y = np.array([ymint,ymint,ymaxt,ymaxt]).astype(float)
        polygon_geom = zip(x,y)
        tempP = Polygon(polygon_geom)
        updatedgdf.append(tempP)
    
    updatedgtf = []
    for p in range(len(gtf)):
        temp = gtf.iloc[p]['geometry']
        x,y = temp.exterior.coords.xy
        x = (np.array(x)-xmin) * pix_per_meter
        y = (np.array(y)-ymin) * pix_per_meter
        polygon_geom = zip(x,y)
        tempP = Polygon(polygon_geom)
        updatedgtf.append(tempP)
    # # length
    # gtf_limits["maxy"] = (gtf_limits["maxy"] - gtf_limits["miny"]) * pix_per_meter
    # gdf["ymax"] = gdf["ymax"].astype(float).astype(int)
    # gdf["ymin"] = gdf["ymin"].astype(float).astype(int)
    # gdf["ymax"] = gdf["ymax"]-gdf["ymin"]
    
    # # width
    # gtf_limits["maxx"] = (gtf_limits["maxx"] - gtf_limits["minx"]) * pix_per_meter
    # gdf["xmax"] = gdf["xmax"].astype(float).astype(int)
    # gdf["xmin"] = gdf["xmin"].astype(float).astype(int)
    # gdf["xmax"] = gdf["xmax"] - gdf["xmin"]
    
    # # translate coords to 0,0
    # gdf.rename(columns={'xmax':'width','ymax':'length'})
    # gdf = gdf.drop(['score','label','plot_name','geometry'],axis=1)
   
    
    return (updatedgdf, updatedgtf, gdf.plot_name)

# field_crowns_temp = fiona.open('./data/OSBS_field_polygons_2019_final.shp')
# field_crowns = [shape(item['geometry']) for item in field_crowns_temp]
# field_crowns_temp = gp.read_file('./data/OSBS_field_polygons_2019_final.shp')
sub = gp.read_file('./submission.csv')
# stems = gp.read_file('cleaned_neon_stems.csv')

list_plots = [os.path.basename(x) for x in glob.glob("./tests/data/evaluation/RGB2/*.tif")]

evaluation_iou = np.array([])
itc_ids = np.array([])
# get ith plot
for pl in list_plots:
    tmpi = 0
    # get coordinates of groundtruth and predictions
    gdf_limits, gtf_limits, itc_name = get_vertex_per_plot(pl)
    # initialize IoU maxtrix GT x Detections
    iou = np.zeros((len(gdf_limits), len(gtf_limits)))
    for det_itc in range(len(gdf_limits)):
        for tr_itc in range(len(gtf_limits)):
            # dets = gdf_limits.iloc[det_itc, :].values
            # trues = gtf_limits.iloc[tr_itc, :].
            dets = gdf_limits[det_itc]
            trues = gtf_limits[tr_itc]
            # calculate the iou
            # iou[det_itc, tr_itc] = bb_intersection_over_union(dets, trues)
            tempint = dets.intersection(trues).area
            tempun = dets.union(trues).area
            iou[det_itc,tr_itc] = tempint/tempun
            tmpi+=1
    # calculate the optimal matching using hungarian algorithm
    mlocs = np.argmin(-iou,axis=0)
    
    # assigned couples
    itc_ids = np.append(itc_ids, itc_name)
    foo = np.take_along_axis(iou,mlocs[:,None],axis=0)
    plot_scores = np.diagonal(foo)
    plot_scores = np.mean(plot_scores)
    evaluation_iou = np.append(evaluation_iou, plot_scores)  # pl,plot_scores])
    print(evaluation_iou)