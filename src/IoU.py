"""
IoU Module, with help from https://github.com/SpaceNetChallenge/utilities/blob/spacenetV3/spacenetutilities/evalTools.py
"""
from tqdm import tqdm
import rtree

def create_rtree_from_poly(poly_list):
    # create index
    index = rtree.index.Index(interleaved=True)
    for idx, geom in enumerate(poly_list):
        index.insert(idx, geom.bounds)

    return index

def _iou_(test_poly, truth_polys, rtree_index):
    fidlistArray = []
    iou_list = []
    fidlist = rtree_index.intersection(test_poly)
    results = []
    for fid in fidlist:
        intersection_result = test_poly.intersection(truth_polys[fid])
        intersection_area = intersection_result.area
        union_area = test_poly.union(truth_polys[fid]).area
        score = (intersection_area / union_area)
        result = pd.DataFrame({"ground_truth": fid,"IoU":score})
        results.append(result)
    
    results = pd.concat(results, ignore_index= True)
    
    return results

def compute_precision_recall(ground_truth, submission, iou_threshold=0.5):
    """
    Args:
        ground_truth: a projected geopandas dataframe with geoemtry
        submission: a projected geopandas dataframe with geometry 
    Returns:
        iou_df: dataframe of IoU scores
        """
    
    #rtree_index 
    rtree_index = create_rtree_from_poly(ground_truth.geometry)
    
    #Create IoU dataframe
    iou_df = submission.geometry.apply(lambda x : _iou_(x, ground_truth, rtree_index))
    
    return iou_df

    
    
    
