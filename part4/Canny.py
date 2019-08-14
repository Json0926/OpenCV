#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019-07-25 19:06 2019

@author : json
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../img/img3.jpg', 0)

# blurred = cv2.GaussianBlur(img, (3, 3), 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])

plt.show()

