#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/9/27 11:33 2019

@author : json
"""

import cv2
import numpy as np

img = cv2.imread('../img/EXC_point1_1374179.jpg')

rows, cols, channels = img.shape
blank = np.zeros([rows, cols, channels], img.dtype)
dst = cv2.addWeighted(img, 0.7, blank, 0.2, 0)
cv2.imshow('ori_img', img)
cv2.imshow('bright_img', dst)
cv2.waitKey()
cv2.destroyAllWindows()