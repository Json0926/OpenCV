import numpy as np
import tensorflow as tf
import skimage.transform as tran
import os
import cv2

img_path = "./rotateimg/croppedImg.jpg"
save_path = './imgProcess/'

# 随机裁剪图片
def random_crop_image(image_file, num):
    with tf.Graph().as_default():
        tf.compat.v1.random.set_random_seed(666)
        file_contents = tf.io.read_file(image_file)
        image = tf.image.decode_image(file_contents, channels=3)
        image_crop_en_list = []
        for i in range(num):
            # 裁剪后图片分辨率保持224x224,3通道
            image_crop = tf.image.random_crop(image, [50, 50, 3])
            image_crop_en_list.append(tf.image.encode_png(image_crop))
        with tf.compat.v1.Session() as sess:
            sess.run(tf.compat.v1.global_variables_initializer())
            sess.run(tf.compat.v1.local_variables_initializer())
            results = sess.run(image_crop_en_list)
            for idx, re in enumerate(results):
                with open('cropImg/' + str(idx) + '.png', 'wb') as f:
                    f.write(re)


# 随机旋转图片有问题
def random_rotate_image(image_file, num):
    with tf.Graph().as_default():
        tf.compat.v1.set_random_seed(666)
        file_contents = tf.io.read_file(image_file)
        image = tf.image.decode_image(file_contents, channels=3)
        image_rotate_en_list = []

        def random_rotate_image_func(image):
            #旋转角度范围
            angle = np.random.uniform(low=-30.0, high=30.0)
            return tran.rotate(image, angle, 'bicubic')
        for i in range(num):
            image_rotate = tf.py_function(random_rotate_image_func, [image], tf.uint8)
            image_rotate_en_list.append(tf.image.encode_png(image_rotate))
        with tf.compat.v1.Session() as sess:
            sess.run(tf.compat.v1.global_variables_initializer())
            sess.run(tf.compat.v1.local_variables_initializer())
            results = sess.run(image_rotate_en_list)
            for idx, re in enumerate(results):
                with open('rotateimg/' + str(idx) + '.png', 'wb') as f:
                    f.write(re)


# 随机翻转图片
def random_flip_image(image_file, num):
    with tf.Graph().as_default():
        tf.compat.v1.set_random_seed(666)
        file_contents = tf.io.read_file(image_file)
        image = tf.image.decode_image(file_contents, channels=3)
        image_flip_en_list = []
        for i in range(num):
            image_flip = tf.image.random_flip_left_right(image)
            image_flip_en_list.append(tf.image.encode_png(image_flip))
        with tf.compat.v1.Session() as sess:
            sess.run(tf.compat.v1.global_variables_initializer())
            sess.run(tf.compat.v1.local_variables_initializer())
            results = sess.run(image_flip_en_list)
            for idx, re in enumerate(results):
                with open('flipImg/' + str(idx) + '.png', 'wb') as f:
                    f.write(re)


# 随机变化图片亮度
def random_brightness_image(image_file, num):
    # 默认图
    with tf.Graph().as_default():
        tf.compat.v1.set_random_seed(666)
        file_contents = tf.io.read_file(image_file)
        image = tf.image.decode_image(file_contents, channels=3)
        image_bright_en_list = []
        for i in range(num):
            image_bright = tf.image.random_brightness(image, max_delta=0.3)
            image_bright_en_list.append(tf.image.encode_png(image_bright))
        with tf.compat.v1.Session() as sess:
            sess.run(tf.compat.v1.global_variables_initializer())
            sess.run(tf.compat.v1.local_variables_initializer())
            results = sess.run(image_bright_en_list)
            for ids, re in enumerate(results):
                if not os.path.exists("brightImg"):
                    os.mkdir("brightImg")
                with open('brightImg/' + str(ids) + '.png', 'wb') as f:
                    f.write(re)


def crop(image_file):
    img = cv2.imread(image_file)
    cropped = img[460:880, 420:1720]
    cv2.imwrite("./rotateimg/croppedImg.jpg", cropped)


if __name__ == '__main__':
    # crop(img_path)
    random_crop_image(img_path, 10000)
