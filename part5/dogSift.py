#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019-08-27 16:52 2019

@author : json
"""

import sys
import cv2
import numpy as np

imgpath = sys.argv[1]
img = cv2.imread(imgpath)
alg = sys.argv[2]

def fd(algorithm):
    if algorithm == 'SIFT':
        return cv2.xfeatures2d.SIFT_create()
    if algorithm == 'SURF':
        return cv2.xfeatures2d.SURF_create(float(sys.argv[3]) if
                                           len(sys.argv) == 4 else 4000)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
keypoints, descriptor = sift.detectAndCompute(gray, None)

img = cv2.drawKeypoints(image=img, outImage=img, keypoints=keypoints,
                        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
                        color=(51, 163, 236))

cv2.imshow('sift', img)
cv2.waitKey()
cv2.destroyAllWindows()
