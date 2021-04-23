# -*- coding: utf-8 -*-
#pip install SimpleItk        # 读取CT医学图像
#pip install tqdm             # 可扩展的Python进度条，封装迭代器 
#pip install pydicom          # 用于读取 dicom 图片
#pip install opencv-python
"""
读取dicom图像并将其转换为png图像

读取某文件夹内的所有dicom文件
:param src_dir: dicom文件夹路径
:return: dicom list
""" 

import os
import SimpleITK
import pydicom
import numpy as np
import cv2
from tqdm import tqdm


def is_dicom_file(filename):

    #判断某文件是否是dicom格式的文件

    file_stream = open(filename, 'rb')
    file_stream.seek(128)
    data = file_stream.read(4)
    file_stream.close()
    if data == b'DICM':
        return True
    return False


def load_patient(src_dir):
    
    #读取某文件夹内的所有dicom文件
    
    files = os.listdir(src_dir)
    slices = []
    for s in files:
        if is_dicom_file(src_dir + '/' + s):
            instance = pydicom.read_file(src_dir + '/' + s)
            slices.append(instance)
    slices.sort(key=lambda x: int(x.InstanceNumber))
    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2]\
                                 - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)
    for s in slices:
        s.SliceThickness = slice_thickness
    return slices


def get_pixels_hu_by_simpleitk(dicom_dir):

    #读取某文件夹内的所有dicom文件,并提取像素值(-4000 ~ 4000)

    reader = SimpleITK.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(dicom_dir)
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    img_array = SimpleITK.GetArrayFromImage(image)
    img_array[img_array == -2000] = 0
    return img_array


def normalize_hu(image):
	#将输入图像的像素值(-4000 ~ 4000)归一化到0~1之间
    MIN_BOUND = -1000.0
    MAX_BOUND = 400.0
    image = (image - MIN_BOUND) / (MAX_BOUND - MIN_BOUND)
    image[image > 1] = 1.
    image[image < 0] = 0.
    return image

if __name__ == '__main__':
    dicom_dir = './data/dicom_demo/'               # 读取dicom文件的元数据(dicom tags)
    slices = load_patient(dicom_dir)
    print('The number of dicom files : ', len(slices))
    
    image = get_pixels_hu_by_simpleitk(dicom_dir)  # 提取dicom文件中的像素值
    for i in tqdm(range(image.shape[0])):
        img_path = "./temp_dir/dcm_2_png/img_" + str(i).rjust(4, '0') + "_i.png"
        
        org_img = normalize_hu(image[i])           # 将像素值归一化到[0,1]区间
        cv2.imwrite(img_path, org_img * 255)       # 保存图像数组为灰度图(.png)
"""
图像数据增强(augmentation)操作
"""

import random
import numpy as np
import cv2

def random_rotate_img(img, min_angle, max_angle):
    """
    图像旋转
    random rotation an image

    :param img:         image to be rotated
    :param min_angle:   min angle to rotate
    :param max_angle:   max angle to rotate
    :return:            image after random rotated

    """

    if not isinstance(img, list):
        img = [img]

    angle = random.randint(min_angle, max_angle)
    center = (img[0].shape[0] / 2, img[0].shape[1] / 2)
    rot_matrix = cv2.getRotationMatrix2D(center, angle, scale=1.0)

    res = []
    for img_inst in img:
        img_inst = cv2.warpAffine(img_inst, rot_matrix,dsize=img_inst.shape[:2],
                                  borderMode=cv2.BORDER_CONSTANT)
        res.append(img_inst)
    if len(res) == 0:
        res = res[0]
    return res


def random_flip_img(img):                         
    '''
	图像平移
    random flip image,both on horizontal and vertical
    :param img:                 image to be flipped
    :return:                    image after flipped
    '''
    flip_val = 0
    if not isinstance(img, list):
        res = cv2.flip(img, flip_val)  # 0 = X axis, 1 = Y axis,  -1 = both
    else:
        res = []
        for img_item in img:
            img_flip = cv2.flip(img_item, flip_val)
            res.append(img_flip)
    return res

if __name__ == '__main__':
    imagePath = './data/chaper3_img_01.png'
    # 读取dicom文件的元数据(dicom tags)
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    print(img.shape)
    res_rotate = random_rotate_img(img, 30, 90)
    cv2.imwrite('./temp_dir/chapter3_rotate_img.png', res_rotate[0])
    res_flip = random_flip_img(img)
    cv2.imwrite('./temp_dir/chapter3_flip_img.png', res_flip)

# 准备U-net训练数据

from scipy import ndimage as ndi
import numpy
import cv2

MASK_MARGIN = 5

def make_mask(v_center, v_diam, width, height):
    mask = numpy.zeros([height, width])
    v_xmin = numpy.max([0, int(v_center[0] - v_diam) - MASK_MARGIN])
    v_xmax = numpy.min([width - 1, int(v_center[0] + v_diam) + MASK_MARGIN])
    v_ymin = numpy.max([0, int(v_center[1] - v_diam) - MASK_MARGIN])
    v_ymax = numpy.min([height - 1, int(v_center[1] + v_diam) + MASK_MARGIN])
    v_xrange = range(v_xmin, v_xmax + 1)
    v_yrange = range(v_ymin, v_ymax + 1)

    for v_x in v_xrange:
        for v_y in v_yrange:
            p_x = v_x
            p_y = v_y
            if numpy.linalg.norm(numpy.array([v_center[0], v_center[1]])\
                                 - numpy.array([p_x, p_y]))<= v_diam * 2:
                mask[p_y, p_x] = 1.0   #设置节点区域的像素值为1
    return (mask)

if __name__ == '__main__':
    imagePath = './data/chaper3_img_01.png'
    # 读取dicom文件的元数据(dicom tags)
    img = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    print('before resize: ', img.shape)
    img_X = ndi.interpolation.zoom(img, [320/512, 320/512], mode='nearest')
    print('before resize: ', img_X.shape)
    cv2.imwrite('./temp_dir/chapter3_img_X.png', img_X)
    img_Y = make_mask((217, 160), 3, 320, 320)
    img_Y[img_Y < 0.5] = 0
    img_Y[img_Y > 0.5] = 255
    nodule_mask = img_Y.astype('uint8')
    cv2.imwrite('./temp_dir/chapter3_img_Y.png', img_Y)




