#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019-09-02 11:28 2019

@author : json
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

queryImage = cv2.imread('../img/img4.png', 0)
trainingImage = cv2.imread('../img/chess_board.jpeg', 0)

# create SIFT and detect/compute
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(queryImage, None)
kp2, des2 = sift.detectAndCompute(trainingImage, None)

# FLANN matches
FLANN_INDEX_KDTREE = 0
indexParam = dict(algorithm = FLANN_INDEX_KDTREE, trees=5)
searchParam = dict(checks=50)

flann = cv2.FlannBasedMatcher(indexParam, searchParam)
matches = flann.knnMatch(des1, des2, k=2)
matchesMask = [[0, 0] for i in range(len(matches))]

for i, (m, n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i] = [1, 0]

drawParam = dict(matchColor = (0, 255, 0),
                 singlePointColor = (255, 0, 0),
                 matchesMask = matchesMask,
                 flags = 0)
resultImage = cv2.drawMatchesKnn(queryImage, kp1, trainingImage, kp2, matches, None, **drawParam)

plt.imshow(resultImage), plt.show()


