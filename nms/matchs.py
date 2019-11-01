#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/10/12 15:45 2019

@author : json
"""

import numpy as np
import cv2

img = cv2.imread('img.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('point.jpg')
gray_tem = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
h, w = template.shape[:2]

res = cv2.matchTemplate(gray, gray_tem, cv2.TM_CCOEFF_NORMED)
threshold = 0.8

loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  # *号表示可选参数
    right_bottom = (pt[0] + w, pt[1] + h)
    cv2.rectangle(img, pt, right_bottom, (0, 0, 255), 1)

cv2.imshow('gray', img)
cv2.waitKey()
cv2.destroyAllWindows()