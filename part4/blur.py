#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019-07-25 11:18 2019

@author : json
"""
import cv2

src = '../data/EXC_point1_1375043.jpg'

img = cv2.imread(src)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

B, G, R = cv2.split(img)

    # save origin image r, g, b
    # cv2.imwrite()

ret_r, threshold_r = cv2.threshold(R, 254, 255, cv2.THRESH_TOZERO)
ret_g, threshold_g = cv2.threshold(G, 254, 255, cv2.THRESH_TOZERO)
ret_b, threshold_b = cv2.threshold(B, 254, 255, cv2.THRESH_TOZERO)

    # cv2.imshow('r', threshold_r)
    # cv2.imshow('g', threshold_g)
    # cv2.imshow('b', threshold_b)

merge = cv2.merge([threshold_r, threshold_g, threshold_b])
bgr = cv2.cvtColor(merge, cv2.COLOR_RGB2BGR)

cv2.imshow('rgb', merge)
cv2.imshow('bgr', bgr)

cv2.waitKey()
cv2.destroyAllWindows()