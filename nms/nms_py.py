#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/10/12 11:08 2019

@author : json
"""
import numpy as np
from matplotlib import pyplot as plt

boxes = np.array([[100,100,210,210,0.72],
        [250,250,420,420,0.8],
        [220,220,320,330,0.92],
        [100,100,210,210,0.72],
        [230,240,325,330,0.81],
        [220,230,315,340,0.9]])

def py_cpu_nms(dets, thresh):
    # dets:(m, 5):x1, y1, x2, y2, score
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]

    areas = (y2 - y1 + 1) * (x2 - x1 + 1)
    scores = dets[:, 4]
    keep = []

    order = scores.argsort()[::-1]

    while order.size > 0:
        i = order[0]
        keep.append(i)

        x11 = np.maximum(x1[i], x1[order[1:]])
        y11 = np.maximum(y1[i], y1[order[1:]])
        x22 = np.maximum(x2[i], x2[order[1:]])
        y22 = np.maximum(y2[i], y2[order[1:]])

        width = np.maximum(0.0, x22 - x11 + 1)
        height = np.maximum(0.0, y22 - y11 + 1)

        inter = width * height
        IOUs = inter / (areas[i] + areas[order[1:]] - inter)

        idx = np.where(IOUs <= thresh)[0]
        order= order[idx + 1]

    return keep


def plot_bbox(dets, c):

    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]

    plt.plot([x1, x2], [y1, y1], c)
    plt.plot([x1, x1], [y1, y2], c)
    plt.plot([x1, x2], [y2, y2], c)
    plt.plot([x2, x2], [y1, y2], c)
    if c == 'k':
        plt.title("before nms")
    else:
        plt.title('after nms')
    plt.show()


# if __name__ == "__main__":
plot_bbox(boxes, 'k')

keep = py_cpu_nms(boxes, thresh=1)
plot_bbox(boxes[keep], 'r')
