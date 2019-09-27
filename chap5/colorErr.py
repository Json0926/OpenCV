#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/9/25 17:43 2019

@author : json
"""

import cv2
import numpy as np

img1 = cv2.imread('')
img2 = cv2.imread('')

err = cv2.subtract(img1, img2)
