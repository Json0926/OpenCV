#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019-07-19 17:25 2019

@author : json
"""

import cv2
import numpy as np

img = cv2.imread('../img/img1.jpg')
# px = img[100, 100]
# print(px)
# blue = img[100, 100, 0]
# print(blue)
#
# print(img.item(10, 10, 2))
# img.itemset((10, 10, 2), 100)
# print(img.item(10, 10, 2))

# print(img.dtype)

roi = img[280:380, 330:430]
img[273:373, 100:200] = roi

# 拆分颜色通道
# cv2.split
# cv2.merge

# 图像加法
# x = np.uint8([250])
# y = np.uint8([10])
# print(cv2.add(x, y))  # 250+10=260  -> 255
# print(x+y)            # 250+10=260 % 256 = 4

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()