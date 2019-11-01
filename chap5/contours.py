#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/9/24 14:39 2019

@author : json
"""

import numpy as np
import cv2


"""
    查找轮廓
"""
def findContours():
    img = cv2.imread('../data/n07740461_51.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(img, contours, -1, (255, 0, 255), 1)

    cv2.imshow('image', img)
    cv2.waitKey(0)

"""
    轮廓的外接矩形
"""
def contoursBounding():
    img = cv2.imread('../data/EXC_point1_18835.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)
    # cv2.imshow('ret', thresh)
    # kernel = np.ones((8, 8), np.uint8)
    # dilate = cv2.dilate(thresh, kernel)
    # cv2.imshow('dil', dilate)
    image, contours, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 画布
    canvas = np.copy(img)

    # 外接矩形
    for cidx, cnt in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(cnt)
        print('Rect: x = {}, y = {}, w = {}, h = {}'.format(x, y, w ,h))
        cv2.rectangle(canvas, pt1=(x, y), pt2=(x+w, y+h), color=(255, 255, 255), thickness=3)
        cv2.imwrite("number_boundingrect_cidx_{}.jpg".format(cidx), img[y:y+h, x:x+w])

    cv2.imshow('canvas.jpg', canvas)
    cv2.waitKey(0)


if __name__ == '__main__':
    contoursBounding()


