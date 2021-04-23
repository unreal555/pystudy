# -*- coding: utf-8 -*-
# 肺有效区域提取
import SimpleITK #读取dicom序列
from scipy import ndimage as ndi
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import disk, dilation, binary_erosion, binary_closing
from skimage.filters import roberts, sobel
import cv2


def get_pixels_hu_by_simpleitk(dicom_dir):
    '''
        读取某文件夹内的所有dicom文件,并提取像素值(-4000 ~ 4000)
    :param src_dir: dicom文件夹路径
    :return: image array
    '''
    reader = SimpleITK.ImageSeriesReader()
    dicom_names = reader.GetGDCMSeriesFileNames(dicom_dir)#序列图片路径
    reader.SetFileNames(dicom_names)
    image = reader.Execute()
    img_array = SimpleITK.GetArrayFromImage(image)
    img_array[img_array == -2000] = 0
    return img_array


def normalize_hu(image):
    '''
           将输入图像的像素值(-4000 ~ 4000)归一化到0~1之间
       :param image 输入的图像数组
       :return: 归一化处理后的图像数组
    '''
    MIN_BOUND = -1000.0
    MAX_BOUND = 400.0
    image = (image - MIN_BOUND) / (MAX_BOUND - MIN_BOUND)
    image[image > 1] = 1.
    image[image < 0] = 0.
    return image


def get_segmented_lungs(im):
    '''
    对输入的图像进行肺部区域分割，提取有效的肺部区域，用于模型训练
    :param 输入的图像
    :return: 返回分割结果
    '''
    
    binary = im < -400                      # Step 1: 转换为二值化图像
    #清除与边界相连的目标物
    cleared = clear_border(binary)          # Step 2: 清除图像边界的小块区域
    #连通区域标记
    label_image = label(cleared)            # Step 3: 分割图像
    
    areas = [r.area for r in regionprops(label_image)]  # Step 4: 保留2个最大的连通区域
    areas.sort()
    if len(areas) > 2:
        for region in regionprops(label_image):
            if region.area < areas[-2]:
                for coordinates in region.coords:
                       label_image[coordinates[0], coordinates[1]] = 0
    binary = label_image > 0
    #生成给定半径的盘形
    selem = disk(2)                         # Step 5: 图像腐蚀操作,将结节与血管剥离
    binary = binary_erosion(binary, selem)
    selem = disk(10)                        # Step 6: 图像闭环操作,保留贴近肺壁的结节
    binary = binary_closing(binary, selem)
    #罗伯次算子2X2
    edges = roberts(binary)                 # Step 7: 进一步将肺区残余小孔区域填充
    binary = ndi.binary_fill_holes(edges)
    
    get_high_vals = binary == 0             # Step 8: 将二值化图像叠加到输入图像上
    im[get_high_vals] = -2000
    
    print('lung segmentation complete.')
    return im, binary


if __name__ == '__main__':
    dicom_dir = './data/dicom_demo/'
    # 提取dicom文件中的像素值
    image = get_pixels_hu_by_simpleitk(dicom_dir)      #图片像素提取
    im, binary = get_segmented_lungs(image[133])       #肺部区域分割
    org_img = normalize_hu(image[133])                 #【0,1】归一化
    cv2.imwrite('./temp_dir/chapter3_segmentation_im.png', org_img*255)
    cv2.imwrite('./temp_dir/chapter3_segmentation_binary.png', binary*255)



