#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/10/29 15:58 2019

@author : json
"""
import cv2
import numpy as np
import os

video = '../data/video/1026.mp4'
cap = cv2.VideoCapture(video)
# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")
frameNum = 0

fps = 25

fourcc = cv2.VideoWriter_fourcc(*"I420")


# Read until video is completed
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()

    w, h, _ = frame.shape
    videoWriter = cv2.VideoWriter("saveVideo.avi", fourcc, fps, (w, h))

    # dst = np.zeros((frame.shape[0], frame.shape[1]), frame.dtype)
    frameNum += 1
    if ret == True:
        tempframe = frame
        if (frameNum == 1):
            previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
            print(111)
        if (frameNum >= 2):
            currentframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
            currentframe = cv2.absdiff(currentframe, previousframe)
            median = cv2.medianBlur(currentframe, 3)

            #        img = cv2.imread("E:/chinese_ocr-master/4.png")
            #        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, threshold_frame = cv2.threshold(currentframe, 50, 255, cv2.THRESH_BINARY)
            # zero = np.zeros(threshold_frame.shape, threshold_frame.dtype)
            # dst = cv2.add(zero, threshold_frame)
            # dst += threshold_frame
            # print(dst.shape, dst.dtype)
            gauss_image = cv2.GaussianBlur(threshold_frame, (3, 3), 0)

            print(222)

            # Display the resulting frame
            # cv2.imshow('原图', frame)
            # cv2.imshow('Frame', currentframe)
            cv2.imshow('median', median)
            # cv2.imshow('sum', dst)

            videoWriter.write(median)

            cv2.imshow('thres', threshold_frame)

            # cv2.imwrite("thres{}.jpg".format(frameNum), threshold_frame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(33) & 0xFF == ord('q'):
                break
        previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
    # Break the loop

    else:
        break

    # cv2.imshow('dst', dst)
# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()