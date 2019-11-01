#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created on 2019-07-18 20:48 2019
# @author : json

import numpy as np
import cv2
import pandas as pd
import time

video = '../data/video/G10301505.mp4'
time.sleep(1)
print(1)

cap = cv2.VideoCapture(video)
a = cap.get(5)
print('aa',a)
print(2)
ret, frame = cap.read()
if(cap.isOpened() == False):
    print('opening videl file')
fps = 10
size = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
videoCap = cv2.VideoWriter('ma.avi', cv2.VideoWriter_fourcc('X','V','I','D'), fps, size)
ret, frame = cap.read()
# cv2.imshow('frame', frame)
while (cap.isOpened()):
    # videoCap.write(frame)
    ret, frame = cap.read()
    videoCap.write(frame)

cap.release()




