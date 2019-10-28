#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on 2019/10/26 9:12 2019

@author : json
"""

"""
    帧间差分法
"""
import cv2
import datetime
import time

def frameDiff(video, save_path, video_time):
    cameraCapture = cv2.VideoCapture(video)
    startTime = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    name = time.strftime("%Y%m%d", time.localtime(time.time())) + '.avi'
    save_path = save_path + time.strftime("%Y%m%d", time.localtime(time.time())) + '.avi'
    fps = 30
    # fps = videoCapture.get(cv2.CAP_PROP_FPS)
    size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    videoWriter = cv2.VideoWriter(
        save_path, cv2.VideoWriter_fourcc('I', '4', '2', '0'),
        fps, size)
    ret, frame = cameraCapture.read()
    numFrameRemaining = video_time * fps - 1
    while numFrameRemaining > 0:
        videoWriter.write(frame)
        ret, frame = cameraCapture.read()
        cv2.putText(frame, str(numFrameRemaining), (10, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1, cv2.LINE_AA)
        numFrameRemaining -= 1
    cameraCapture.release()

"""
    检测运动物体
"""
def detect_video(video, save_path):
    camera = cv2.VideoCapture(video)
    history = 2

    fps = int(camera.get(cv2.CAP_PROP_FPS))
    size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    videoWriter = cv2.VideoWriter(
        save_path, cv2.VideoWriter_fourcc('I', '4', '2', '0'),
        fps, size)
    frameNumber = camera.get(7)

    bs = cv2.createBackgroundSubtractorKNN(detectShadows=True)
    bs.setHistory(history)


    frames = 0

    while True:
        ret, frame = camera.read()
        if not ret:
            break
        fg_mask = bs.apply(frame)

        if frames < history:
            frames += 1
            continue

        videoWriter.write(fg_mask)
        ret, frame = camera.read()

            # 对原始帧进行膨胀去噪
        th = cv2.threshold(fg_mask.copy(), 244, 255, cv2.THRESH_BINARY)[1]
        th = cv2.erode(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=2)
        dilated = cv2.dilate(th, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 3)), iterations=2)

        # 获取所有检测框
        image, contours, hier = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            # 获取矩形框边界坐标
            x, y, w, h = cv2.boundingRect(c)
            # 计算矩形框的面积
            area = cv2.contourArea(c)
            # if 500 < area < 3000:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # videoWriter.write(th)
        cv2.imshow("back", fg_mask)
        cv2.imshow("detection", frame)
        if cv2.waitKey(110) & 0xff == 27:
            break
    camera.release()


"""
检测小球运动轨迹  帧差
"""
def diff(video):
    cameraCapture = cv2.VideoCapture(video)
    ret, frame = cameraCapture





if __name__ == '__main__':
    video_path = '../data/video/1026.mp4'
    save_path = '../data/video/'
    # frameDiff(video_path, save_path, 60)
    detect_video(video_path, save_path)














