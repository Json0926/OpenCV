#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019-07-25 20:29 2019

@author : json
"""

import cv2
import numpy as np

img = cv2.imread('../img/img2.jpg', 0)

ret, thresh = cv2.threshold(img, 200, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
print(M)