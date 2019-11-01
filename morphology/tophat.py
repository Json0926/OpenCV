#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/10/14 16:28 2019

@author : json
"""
import cv2

img = cv2.imread('../img/EXC_point1_1374179.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thres_img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)



kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
open_img = cv2.morphologyEx(thres_img, cv2.MORPH_OPEN, kernel)
close_img = cv2.morphologyEx(thres_img, cv2.MORPH_CLOSE, kernel)
tophat_img = cv2.morphologyEx(thres_img, cv2.MORPH_TOPHAT, kernel)
blackhat_img = cv2.morphologyEx(thres_img, cv2.MORPH_BLACKHAT, kernel)

bitwiseXor_gray = cv2.absdiff(gray,tophat_img)
blackXor = cv2.bitwise_xor(gray, blackhat_img)

cv2.imshow('oriImg', img)
cv2.imshow('open', open_img)
cv2.imshow('close', close_img)
# cv2.imshow('topHatImg', tophat_img)
# cv2.imshow('blackHat', blackhat_img)
# cv2.imshow('topXor', bitwiseXor_gray)
# cv2.imshow('blackXor', blackXor)

cv2.waitKey(0)
