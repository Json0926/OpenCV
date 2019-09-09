#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019-08-27 16:13 2019

@author : json
"""

import cv2
import numpy as np

img = cv2.imread('../part3/image/500.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 3, 15, 0.04)
img[dst>0.01 * dst.max()] = [0, 0, 255]
cv2.imshow('corners', img)
cv2.waitKey()
cv2.destroyAllWindows()