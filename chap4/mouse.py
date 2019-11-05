#!/usr/bin/env python

"""
# -*- coding:utf-8 -*-
# Created on 2019-07-19 14:47 2019

# @author : json
"""

"""
import cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
"""

import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


img = np.zeros((512, 512, 3), np.int8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(10)&0xFF==27:
        break
cv2.destroyAllWindows()