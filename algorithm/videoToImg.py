#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019-09-09 13:36 2019

@author : json
"""

import cv2

cameraCapture = cv2.VideoCapture(0)
# size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
#         int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# fps = 20
# videoWriter = cv2.VideoWriter('outputVideo.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'),
#                               fps, size)
ret, frame = cameraCapture.read()
count = 1
# while count < 200:
#     count += 1
#     _, frame = cameraCapture.read()
#     cv2.putText(frame, str(count), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1, cv2.LINE_AA)
#     videoWriter.write(frame)

timeF = 500
while ret:
    ret, frame = cameraCapture.read()
    if(count % timeF == 0):
        cv2.imwrite('image/'+ str(count) +'.jpg', frame)
    count += 1
    print(count)
cv2.waitKey()
# videoWriter.release()
cameraCapture.release()



