#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/10/9 14:14 2019

@author : json
"""
import cv2
from matplotlib import pyplot as plt

merge = cv2.imread('')

chans = cv2.split(merge)
colors = ("b", "g", "r")
plt.figure()
plt.title("Flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("Pixels")

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.show()