import cv2
import matplotlib.pyplot as plt
import copy
import numpy as np
import os
from src import model
from src import util
from src.body import Body
from src.hand import Hand

test_images = ['images/demo_coco.jpg', 
               'images/demo_coco2.jpg',
               'images/demo_beach.jpg',
               'images/demo_ucsd.jpg',
               'images/demo_ucsd2.jpg']
multi_scale = False     # use multi scale image pyramid

for test_image in test_images:
    body_estimation = Body('model/body_pose_model.pth', multi_scale=multi_scale)
    oriImg = cv2.imread(test_image)  # B,G,R order
    candidate, subset, heatmap_list, heatmap_list_converted_list = body_estimation(oriImg)
    heatmap_0 = heatmap_list[0] 
    canvas = copy.deepcopy(oriImg)
    canvas = util.draw_bodypose(canvas, candidate, subset)

    plt.figure(figsize=(10, 10))
    img_name = os.path.basename(test_image).split(".")[0]
    plt.title(f"{img_name}, multi_scale={multi_scale}")
    plt.imshow(canvas[:, :, [2, 1, 0]])
    plt.savefig(f"{img_name},multi_scale={multi_scale}.png",bbox_inches="tight")