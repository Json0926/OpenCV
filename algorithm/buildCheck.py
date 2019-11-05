#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/10/31 11:10 2019

@author : json
"""

"""
    楼体检测
"""

import cv2
import numpy as np

"""
    图像预处理
"""
def process(img):

    gaussian = cv2.GaussianBlur(img, (3, 3), 0, 0, cv2.BORDER_DEFAULT)
    median = cv2.medianBlur(gaussian, 5)

    # sobel算子
    sobel = cv2.Sobel(median, cv2.CV_8U, 1, 0, ksize=3)
    # 图像深度是cv2.CV_8U 16U。。。中的一个

    # 阈值处理
    thres = cv2.threshold(sobel, 50, 255, cv2.THRESH_BINARY)[1]

    # 形态学处理
    # 腐蚀和膨胀的核函数  参数分别是核函数的形状和大小
    element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 9))
    element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 9))

    # 膨胀一次 突出轮廓
    dilation = cv2.dilate(thres, element2, iterations=1)
    # 腐蚀一次，去噪
    erosion = cv2.erode(dilation, element1, iterations=1)
    # 膨胀多次，再次突出轮廓
    dilation2 = cv2.dilate(erosion, element2, iterations=3)

    cv2.imshow('sobel', sobel)
    cv2.imshow('thres', thres)
    cv2.imshow('dilation1', dilation)
    cv2.imshow('erode', erosion)
    cv2.imshow('dilation2', dilation2)

    return dilation

"""
    定位
"""
def getRegion(img):
    region = []
    _, contours, hier = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        # if (area < 2000):
        #     continue

        # 轮廓  epsilon是从轮廓到近似轮廓的最大距离。是一个准确率参数，好的epslion选择可以得到正确的输出。
        # True决定曲线是否闭合
        epslion = 1e-3 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epslion, True)

        # 四个boxpoint是从左下开始顺时针计数
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        height = abs(box[0][1] - box[2][1])
        width = abs(box[0][0] - box[2][0])
        ratio = float(width)/float(height)
        if (ratio > 0 and ratio < 0.6):
            region.append(box)
    return region

def detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    pre = process(gray)

    region = getRegion(pre)
    for box in region:
        cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
        print(box)
    cv2.imshow('result', img)
    cv2.waitKey(0)


if __name__ == "__main__":
    image = './data/630.png'
    img = cv2.imread(image)
    detect(img)