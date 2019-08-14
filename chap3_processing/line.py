#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created on 2019-07-19 14:15 2019

# @author : json

import numpy as np
import cv2

img = np.zeros((512, 512, 3), np.int8)

cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
cv2.circle(img, (447, 63), 63, (0, 0, 225), -1)
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 225, -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()