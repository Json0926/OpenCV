#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019-08-12 16:47 2019

@author : json
"""

import cv2
import numpy as np

img = np.zeros((200, 200), dtype=np.uint8)
img[50:150, 50:150] = 255

ret, thresh = cv2.threshold(img, 127, 255, 0)
""" findContours(输入图像，层次类型，轮廓逼近方法)  会修改输入图像"""
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
cv2.imshow("contours", color)
cv2.waitKey()
cv2.destroyAllWindows()
