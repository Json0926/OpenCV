#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/9/27 18:00 2019

@author : json
"""

import sys
import cv2 as cv
import numpy as np




def main(argv):
    default_file = './data/color/EXC_point1_1374179.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    # src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    src = cv.imread(default_file)
    # Check if image is loaded fine
    if src is None:
        print('Error opening image!')
        print('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
        return -1

    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)

    # gray = cv.medianBlur(gray, 5)

    rows = gray.shape[0]
    number = 1
    # circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
    #                           param1=2, param2=20,
    #                           minRadius=1, maxRadius=10)

    # canny边缘检测去噪
    edges = cv.Canny(gray, 100, 200)

    circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, 1, 10,
                              param1=4, param2=15,
                              minRadius=5, maxRadius=10)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # center = (i[0], i[1])
            # # circle center
            # cv.circle(src, center, 1, (0, 100, 100), 1)
            # # circle outline
            # radius = i[2]
            # cv.circle(src, center, radius, (255, 0, 255), 2)

            # draw the outer circle
            cv.circle(src, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv.circle(src, (i[0], i[1]), 2, (0, 0, 255), 3)

            # 加编号
            font = cv.FONT_HERSHEY_SIMPLEX
            c = cv.putText(src, str(number), (i[0] + 3, i[1]), font, 0.2, (30, 182, 255),
                            1)  # 明黄色BGR 30, 182, 255
            number += 1

    cv.imshow("detected circles", src)
    cv.waitKey(0)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])