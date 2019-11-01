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
import numpy as np

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
    cap = cv2.VideoCapture(video)
    ret, frame = cap.read()
    print(frame.shape)
    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video stream or file")

    fps = 25
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    videoCap = cv2.VideoWriter('cha.avi', cv2.VideoWriter_fourcc('X','V','I','D'), fps, (960, 544))


    frameNum = 0
    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
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
                median = cv2.cvtColor(median, cv2.COLOR_GRAY2BGR)

                # print('frame', frame, frame.shape)
                # print('median', median, median.shape)
                videoCap.write(median)

                ret, threshold_frame = cv2.threshold(currentframe, 50, 255, cv2.THRESH_BINARY)
                # zero = np.zeros(threshold_frame.shape, threshold_frame.dtype)
                # print(dst.shape, dst.dtype)
                gauss_image = cv2.GaussianBlur(threshold_frame, (3, 3), 0)

                print('thres', threshold_frame, threshold_frame.shape)
                threshold_frame = cv2.cvtColor(threshold_frame, cv2.COLOR_GRAY2BGR)
                print(222)
                # Display the resulting frame
                # cv2.imshow('原图', frame)
                # cv2.imshow('Frame', currentframe)
                cv2.imshow('median', median)
                # cv2.imshow('sum', dst)
                cv2.imshow('thres', threshold_frame)

                # cv2.imwrite("thres{}.jpg".format(frameNum), threshold_frame)

                # Press Q on keyboard to  exit
                if cv2.waitKey(33) & 0xFF == ord('q'):
                    break
            previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
        # Break the loop

        else:
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()




if __name__ == '__main__':
    video_path = '../data/video/科技炫酷视频.mp4'
    save_path = '../data/video/'
    # frameDiff(video_path, save_path, 60)
    # detect_video(video_path, save_path)
    diff(video_path)














