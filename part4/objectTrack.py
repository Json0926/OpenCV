#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019-07-23 16:34 2019

@author : json
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(1):

    # blue = np.uint8([0, 0, 255])
    # hsv_green = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    # print(hsv_green)

    # 获取每一帧
    ret, frame = cap.read()

    # 转换到HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 设定蓝色区域阈值
    low_blue = np.array([110, 50, 50])
    high_blue = np.array([130, 255, 255])

    # 根据阈值构建掩膜
    mask = cv2.inRange(hsv, low_blue, high_blue)

    # 对原图像和掩膜进行位运算
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 显示图像
    cv2.imshow('frame', frame)
    cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(0)&0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
