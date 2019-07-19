#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created on 2019-07-18 20:36 2019
# @author : json
# @file : mltimage.py
# @software: PyCharm

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../img/img1.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()