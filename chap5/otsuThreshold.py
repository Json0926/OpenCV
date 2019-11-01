#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/10/8 9:45 2019

@author : json
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img1 = '../img/EXC_point1_1374179.jpg'
img2 = '../img/EXC_point1_1375043.jpg'

def diffColor(src1, src2):
    img1 = cv2.imread(src1)
    img2 = cv2.imread(src2)

    hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    H1, S1, V1 = cv2.split(hsv1)
    H2, S2, V2 = cv2.split(hsv2)

    diffH = cv2.subtract(H1, H2)
    diffS = cv2.subtract(S1, S2)
    diffV = cv2.subtract(V1, V2)
    mergeHsv = cv2.merge([diffH, S1, V1])

    cv2.imshow('H1', H1)
    cv2.imshow('H2', H2)
    cv2.imshow('hsvMerge', mergeHsv)

    B1, G1, R1 = cv2.split(img1)
    B2, G2, R2 = cv2.split(img2)

    diffB = cv2.absdiff(B1, B2)
    diffG = cv2.absdiff(G1, G2)
    diffR = cv2.absdiff(R1, R2)

    # cv2.imshow('B1', B1)
    # cv2.imshow('B2', B2)
    # cv2.imshow('difB', diffB)

    merge = cv2.merge([diffB, diffG, diffR])
    # cv2.imshow('merge', merge)
    cv2.waitKey(0)

def ThresholdByOtsu(src):
    img = cv2.imread(src)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    B, G, R = cv2.split(img)

    # save origin image r, g, b
    # cv2.imwrite()

    ret_r, threshold_r = cv2.threshold(R, 254, 255, cv2.THRESH_TOZERO_INV)
    ret_g, threshold_g = cv2.threshold(G, 254, 255, cv2.THRESH_TOZERO_INV)
    ret_b, threshold_b = cv2.threshold(B, 254, 255, cv2.THRESH_TOZERO_INV)

    # cv2.imshow('r', threshold_r)
    # cv2.imshow('g', threshold_g)
    # cv2.imshow('b', threshold_b)

    merge = cv2.merge([threshold_b, threshold_g, threshold_r])
    rgb = cv2.cvtColor(merge, cv2.COLOR_BGR2RGB)

    return rgb

def ThresholdByHSV(src):
    img = cv2.imread(src)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    H, S, V = cv2.split(hsv)

    ret_h, threshold_h = cv2.threshold(H, 150, 180, cv2.THRESH_TOZERO_INV)
    ret_s, threshold_s = cv2.threshold(S, 50, 255, cv2.THRESH_TOZERO_INV)
    ret_v, threshold_v = cv2.threshold(V, 250, 255, cv2.THRESH_TOZERO_INV)

    merge = cv2.merge([threshold_h, threshold_s, threshold_v])
    bgr = cv2.cvtColor(merge, cv2.COLOR_HSV2BGR)
    return bgr

def RGBToHSI(rgb_lwpImg):
    rows = int(rgb_lwpImg.shape[0])
    cols = int(rgb_lwpImg.shape[1])
    b, g, r = cv2.split(rgb_lwpImg)
    # 归一化到[0,1]
    b = b / 255.0
    g = g / 255.0
    r = r / 255.0
    hsi_lwpImg = rgb_lwpImg.copy()
    H, S, I = cv2.split(hsi_lwpImg)
    for i in range(rows):
        for j in range(cols):
            num = 0.5 * ((r[i, j]-g[i, j])+(r[i, j]-b[i, j]))
            den = np.sqrt((r[i, j]-g[i, j])**2+(r[i, j]-b[i, j])*(g[i, j]-b[i, j]))
            theta = float(np.arccos(num/den))

            if den == 0:
                    H = 0
            elif b[i, j] <= g[i, j]:
                H = theta
            else:
                H = 2*3.14169265 - theta

            min_RGB = min(min(b[i, j], g[i, j]), r[i, j])
            sum = b[i, j]+g[i, j]+r[i, j]
            if sum == 0:
                S = 0
            else:
                S = 1 - 3*min_RGB/sum

            H = H/(2*3.14159265)
            I = sum/3.0
            # 输出HSI图像，扩充到255以方便显示，一般H分量在[0,2pi]之间，S和I在[0,1]之间
            hsi_lwpImg[i, j, 0] = H*255
            hsi_lwpImg[i, j, 1] = S*255
            hsi_lwpImg[i, j, 2] = I*255
    return hsi_lwpImg

if __name__ == '__main__':
    ori1 = cv2.imread(img1)
    cv2.namedWindow('image1ori', 0)
    cv2.imshow('image1ori', ori1)
    image1 = ThresholdByOtsu(img1)
    cv2.namedWindow('img1', 0)
    cv2.imshow('img1', image1)

    ori2 = cv2.imread(img2)
    cv2.imshow('image2ori', ori2)
    image2 = ThresholdByHSV(img2)
    cv2.imshow('img2', image2)

    err = cv2.bitwise_xor(image1, image2)
    cv2.imshow('err', err)
    cv2.waitKey()
    cv2.destroyAllWindows()

