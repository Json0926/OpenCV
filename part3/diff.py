#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019-09-09 16:47 2019

@author : json
"""

import cv2
import numpy as np

img1 = cv2.imread('./image/500.jpg')
img2 = cv2.imread('./image/1000.jpg')

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
err = cv2.subtract(gray1, gray2)

cv2.imshow('sub', err)
cv2.waitKey()
cv2.destroyAllWindows()
