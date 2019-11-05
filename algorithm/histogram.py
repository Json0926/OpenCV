#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/10/8 14:21 2019

@author : json
"""

from matplotlib import pyplot as plt
import numpy as np
import cv2

src = '../data/EXC_point1_1375043.jpg'

image = cv2.imread(src)
chans = cv2.split(image)
colors = ("b","g","r")
plt.figure()
plt.title("Flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("Pixels")

for (chan,color) in zip(chans,colors):
    hist = cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(hist,color = color)
    plt.xlim([0,256])
plt.show()

cv2.imshow("Original",image)
cv2.waitKey(0)
cv2.destroyAllWindows()



# img = cv2.imread(src)
# img1 = cv2.imread(src1)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
#
# dif = cv2.absdiff(gray, gray1)
# ret, dst = cv2.threshold(dif, 2, 255, cv2.THRESH_BINARY)
# cv2.imshow('diff', dst)
#
# B, G, R = cv2.split(img)
#
# # cv2.imshow('r', R)
# # cv2.imshow('g', G)
# # cv2.imshow('b', B)
# cv2.imshow('HSV1', gray)
# cv2.imshow('HSV2', gray1)