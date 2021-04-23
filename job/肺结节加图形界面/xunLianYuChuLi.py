# -*- coding: utf-8 -*-
# 准备3dcnn的训练数据
import os
import SimpleITK
import pydicom
import numpy as np
import cv2
import glob
from tqdm import tqdm


def is_dicom_file(filename):
    """
           判断某文件是否是dicom格式的文件
    :param filename: dicom文件的路径
    :return:
    """

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

def rescale_patient_images(images_zyx, org_spacing_xyz, target_voxel_mm, is_mask_image=False):
    """
            将dicom图像缩放到1mm:1mm:1mm的尺度
        :param images_zyx: 缩放前的图像(3维)
        :return: 缩放后的图像(3维)

    """

    print("Spacing: ", org_spacing_xyz)
    print("Shape: ", images_zyx.shape)

    # print ("Resizing dim z")
    resize_x = 1.0
    resize_y = float(org_spacing_xyz[2]) / float(target_voxel_mm)
    interpolation = cv2.INTER_NEAREST if is_mask_image else cv2.INTER_LINEAR
    res = cv2.resize(images_zyx, dsize=None, fx=resize_x, fy=resize_y, interpolation=interpolation)
    # print ("Shape is now : ", res.shape)

    res = res.swapaxes(0, 2)
    res = res.swapaxes(0, 1)
    # print ("Shape: ", res.shape)
    resize_x = float(org_spacing_xyz[0]) / float(target_voxel_mm)
    resize_y = float(org_spacing_xyz[1]) / float(target_voxel_mm)

    # cv2 can handle max 512 channels..
    if res.shape[2] > 512:
        res = res.swapaxes(0, 2)
        res1 = res[:256]
        res2 = res[256:]
        res1 = res1.swapaxes(0, 2)
        res2 = res2.swapaxes(0, 2)
        res1 = cv2.resize(res1, dsize=None, fx=resize_x, fy=resize_y, interpolation=interpolation)
        res2 = cv2.resize(res2, dsize=None, fx=resize_x, fy=resize_y, interpolation=interpolation)
        res1 = res1.swapaxes(0, 2)
        res2 = res2.swapaxes(0, 2)
        res = np.vstack([res1, res2])
        res = res.swapaxes(0, 2)
    else:
        res = cv2.resize(res, dsize=None, fx=resize_x, fy=resize_y, interpolation=interpolation)

    res = res.swapaxes(0, 2)
    res = res.swapaxes(2, 1)

    print("Shape after: ", res.shape)
    return res

def get_cube_from_img(img3d, center_x, center_y, center_z, block_size):
    #切割为小cube并平铺存储为png
    start_x = max(center_x - block_size / 2, 0)
    if start_x + block_size > img3d.shape[2]:
        start_x = img3d.shape[2] - block_size

    start_y = max(center_y - block_size / 2, 0)
    start_z = max(center_z - block_size / 2, 0)
    if start_z + block_size > img3d.shape[0]:
        start_z = img3d.shape[0] - block_size
    start_z = int(start_z)
    start_y = int(start_y)
    start_x = int(start_x)
    res = img3d[start_z:start_z + block_size,
                start_y:start_y + block_size,
                start_x:start_x + block_size]
    return res

def normalize_hu(image):

    """
    将输入图像的像素值(-4000 ~ 4000)归一化到0~1之间
    :param image 输入的图像数组
    :return: 归一化处理后的图像数组
    """

    MIN_BOUND = -1000.0
    MAX_BOUND = 400.0
    image = (image - MIN_BOUND) / (MAX_BOUND - MIN_BOUND)
    image[image > 1] = 1.
    image[image < 0] = 0.
    return image


def load_patient_images(src_dir, wildcard="*.*", exclude_wildcards=[]):
    """
        读取一个病例的所有png图像，返回值为一个三维图像数组
    :param image 输入的一系列png图像
    :return: 三维图像数组
    """

    src_img_paths = glob.glob(src_dir + wildcard)
    for exclude_wildcard in exclude_wildcards:
        exclude_img_paths = glob.glob(src_dir + exclude_wildcard)
        src_img_paths = [im for im in src_img_paths if im not in exclude_img_paths]
    src_img_paths.sort()
    images = [cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) for img_path in src_img_paths]
    images = [im.reshape((1,) + im.shape) for im in images]
    res = np.vstack(images)
    return res


def save_cube_img(target_path, cube_img, rows, cols):
    """
        将3维cube图像保存为2维图像,方便勘误检查
    :param 二维图像保存路径, 三维输入图像
    :return: 二维图像
    """

    assert rows * cols == cube_img.shape[0]
    img_height = cube_img.shape[1]
    img_width = cube_img.shape[1]
    res_img = np.zeros((rows * img_height, cols * img_width), dtype=np.uint8)

    for row in range(rows):
        for col in range(cols):
            target_y = row * img_height
            target_x = col * img_width
            res_img[target_y:target_y + img_height,
                    target_x:target_x + img_width] = cube_img[row * cols + col]

    cv2.imwrite(target_path, res_img)


if __name__ == '__main__':
    dicom_dir = './data/dicom_demo/'
   
    slices = load_patient(dicom_dir)                  # 读取dicom文件的元数据(dicom tags)
    
    pixel_spacing = slices[0].PixelSpacing           # 获取dicom的spacing值
    pixel_spacing.append(slices[0].SliceThickness)
    print('The dicom spacing : ', pixel_spacing)
    
    image = get_pixels_hu_by_simpleitk(dicom_dir)    # 提取dicom文件中的像素值
    # 标准化不同规格的图像尺寸, 统一将dicom图像缩放到1mm:1mm:1mm的尺度
    image = rescale_patient_images(image, pixel_spacing, 1.00)
    for i in tqdm(range(image.shape[0])):
        img_path = "./temp_dir/dcm_2_png/img_" + str(i).rjust(4, '0') + "_i.png"
        
        org_img = normalize_hu(image[i])             # 将像素值归一化到[0,1]区间
        
        cv2.imwrite(img_path, org_img * 255)         # 保存图像数组为灰度图(.png)

    # 加载上一步生成的png图像
    pngs = load_patient_images("./temp_dir/dcm_2_png/", "*_i.png")
    # 输入人工标记的结节位置: coord_x, coord_y, coord_z
    cube_img = get_cube_from_img(pngs, 272, 200, 134, 64)
    print(cube_img)
    save_cube_img('./temp_dir/chapter3_3dcnn_img_X.png', cube_img, 8, 8)




