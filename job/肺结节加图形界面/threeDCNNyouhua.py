# -*- coding: utf-8 -*-
import os
import random
from keras import layers
from keras import backend as K
from keras.layers import Input, Convolution3D, MaxPooling3D, Flatten, Dropout,\
AveragePooling3D, BatchNormalization,Activation
from keras.metrics import binary_accuracy, binary_crossentropy
from keras.models import Model
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, History, EarlyStopping
from keras.models import model_from_json
import matplotlib.pyplot as plt
import numpy
import cv2

K.image_data_format()
CUBE_SIZE = 32
MEAN_PIXEL_VALUE = 41
BATCH_SIZE = 8

def get_3dnnnet(input_shape=(CUBE_SIZE, CUBE_SIZE, CUBE_SIZE, 1), 
                load_weight_path=None, USE_DROPOUT=True) -> Model:
    inputs = Input(shape=input_shape, name="input_1")
    x = inputs 
    
    #-------------------------------------------------------------
    X_shortcut = x    #保存输入值,后面将需要添加回主路径
    #-------------------------------------------------------------
    
    x = AveragePooling3D(pool_size=(2, 1, 1), strides=(2, 1, 1), border_mode="same")(x)
    x = Convolution3D(64, 3, 3, 3, border_mode='same', name='conv1', subsample=(1, 1, 1))(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = MaxPooling3D(pool_size=(1, 2, 2), strides=(1, 2, 2), border_mode='valid', name='pool1')(x)
    if USE_DROPOUT:
        x = Dropout(p=0.3)(x)
        #空间金字塔池化
    #dropout = SpatialDropout3D(rate=dropout_rate, data_format=data_format)(convolution1)

    # 2nd layer group
    x = Convolution3D(128, 3, 3, 3, border_mode='same', name='conv2', subsample=(1, 1, 1))(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), border_mode='valid', name='pool2')(x)
    if USE_DROPOUT:
        x = Dropout(p=0.3)(x)
    
    # 3rd layer group
    x = Convolution3D(256, 3, 3, 3, activation='relu', border_mode='same', name='conv3a', subsample=(1, 1, 1))(x)
    x = Convolution3D(256, 3, 3, 3, activation='relu', border_mode='same', name='conv3b', subsample=(1, 1, 1))(x)
    x = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), border_mode='valid', name='pool3')(x)
    if USE_DROPOUT:
        x = Dropout(p=0.4)(x)

    # 4th layer group
    x = Convolution3D(512, 3, 3, 3, activation='relu', border_mode='same', name='conv4a', subsample=(1, 1, 1))(x)
    x = Convolution3D(512, 3, 3, 3, activation='relu', border_mode='same', name='conv4b', subsample=(1, 1, 1), )(x)
    x = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), border_mode='valid', name='pool4')(x)
    if USE_DROPOUT:
        x = Dropout(p=0.5)(x)
    
    # shortcut路径--------------------------------------------
    X_shortcut = Convolution3D(512, 3, 3, 3, activation='relu', border_mode='same', name='conv4a_X', subsample=(1, 1, 1))(x)
    X_shortcut = Convolution3D(512, 3, 3, 3, activation='relu', border_mode='same', name='conv4b_X', subsample=(1, 1, 1))(X_shortcut)
    X_shortcut = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2), border_mode='valid', name='pool5')(X_shortcut)
    X_shortcut = BatchNormalization()(X_shortcut)

    # 主路径最后部分,为主路径添加shortcut并通过relu激活
    X = layers.add([x, X_shortcut])
    #--------------------------------------------
    
    last64 = Convolution3D(64, 2, 2, 2, activation="relu", name="last_64")(X)
    out_class = Convolution3D(1, 1, 1, 1, activation="sigmoid", name="out_class_last")(last64)
    out_class = Flatten(name="out_class")(out_class)
    model = Model(input=inputs, output=[out_class])

    model.load_weights(load_weight_path, by_name=True)
    ################以下两行代码自己加的
    json_string=model.to_json()
    model=model_from_json(json_string)
    
    model.compile(optimizer=Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0),
                  loss={"out_class": "binary_crossentropy"},
                  metrics={"out_class": [binary_accuracy, binary_crossentropy]})
    return model
# 将二维图像依次叠加，转换为三维图像
def stack_2dcube_to_3darray(src_path, rows, cols, size):
    img = cv2.imread(src_path, cv2.IMREAD_GRAYSCALE)
    # assert rows * size == cube_img.shape[0]
    # assert cols * size == cube_img.shape[1]

    res = numpy.zeros((rows * cols, size, size))

    img_height = size
    img_width = size

    for row in range(rows):
        for col in range(cols):
            src_y = row * img_height
            src_x = col * img_width
            res[row * cols + col] = img[src_y:src_y + img_height, src_x:src_x + img_width]

    return res


# 将三维的dicom图像缩放到1mm:1mm:1mm的尺度
def rescale_patient_images2(images_zyx, target_shape, verbose=False):
    if verbose:
        print("Target: ", target_shape)
        print("Shape: ", images_zyx.shape)

    # print ("Resizing dim z")
    resize_x = 1.0
    interpolation = cv2.INTER_NEAREST if False else cv2.INTER_LINEAR
    res = cv2.resize(images_zyx, dsize=(target_shape[1], target_shape[0]), interpolation=interpolation)
    # print ("Shape is now : ", res.shape)

    res = res.swapaxes(0, 2)
    res = res.swapaxes(0, 1)

    # cv2 can handle max 512 channels..
    if res.shape[2] > 512:
        res = res.swapaxes(0, 2)
        res1 = res[:256]
        res2 = res[256:]
        res1 = res1.swapaxes(0, 2)
        res2 = res2.swapaxes(0, 2)
        res1 = cv2.resize(res1, dsize=(target_shape[2], target_shape[1]), interpolation=interpolation)
        res2 = cv2.resize(res2, dsize=(target_shape[2], target_shape[1]), interpolation=interpolation)
        res1 = res1.swapaxes(0, 2)
        res2 = res2.swapaxes(0, 2)
        res = numpy.vstack([res1, res2])
        res = res.swapaxes(0, 2)
    else:
        res = cv2.resize(res, dsize=(target_shape[2], target_shape[1]), interpolation=interpolation)

    res = res.swapaxes(0, 2)
    res = res.swapaxes(2, 1)
    if verbose:
        print("Shape after: ", res.shape)
    return res


# 对即将输入网络的cube进行预处理操作
def prepare_image_for_net3D(img, MEAN_PIXEL_VALUE):
    img = img.astype(numpy.float32)
    img -= MEAN_PIXEL_VALUE
    img /= 255.
    img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2], 1)
    return img


# 自定义的数据加载器(迭代地批量加入训练数据，其间对训练样本做了augmentation)
def data_generator(batch_size, record_list, train_set):
    batch_idx = 0
    means = []
    while True:
        img_list = []
        class_list = []
        if train_set:
            random.shuffle(record_list)
        CROP_SIZE = CUBE_SIZE
        # CROP_SIZE = 48
        for record_idx, record_item in enumerate(record_list):
            # rint patient_dir
            class_label = record_item[1]
            if class_label == 0:
                cube_image = stack_2dcube_to_3darray(record_item[0], 6, 8, 48)

            elif class_label == 1:
                cube_image = stack_2dcube_to_3darray(record_item[0], 8, 8, 64)
            if train_set:
                pass

            current_cube_size = cube_image.shape[0]
            indent_x = (current_cube_size - CROP_SIZE) / 2
            indent_y = (current_cube_size - CROP_SIZE) / 2
            indent_z = (current_cube_size - CROP_SIZE) / 2
            wiggle_indent = 0
            wiggle = current_cube_size - CROP_SIZE - 1
            if wiggle > (CROP_SIZE / 2):
                wiggle_indent = CROP_SIZE / 4
                wiggle = current_cube_size - CROP_SIZE - CROP_SIZE / 2 - 1

            if train_set:
                indent_x = wiggle_indent + random.randint(0, wiggle)
                indent_y = wiggle_indent + random.randint(0, wiggle)
                indent_z = wiggle_indent + random.randint(0, wiggle)

            indent_x = int(indent_x)
            indent_y = int(indent_y)
            indent_z = int(indent_z)

            cube_image = cube_image[indent_z:indent_z + CROP_SIZE, 
                                    indent_y:indent_y + CROP_SIZE,
                                    indent_x:indent_x + CROP_SIZE]

            if CROP_SIZE != CUBE_SIZE:
                cube_image = rescale_patient_images2(cube_image, (CUBE_SIZE, CUBE_SIZE, CUBE_SIZE))

            assert cube_image.shape == (CUBE_SIZE, CUBE_SIZE, CUBE_SIZE)

            if train_set:
                if random.randint(0, 100) > 50:
                    cube_image = numpy.fliplr(cube_image)
                if random.randint(0, 100) > 50:
                    cube_image = numpy.flipud(cube_image)
                if random.randint(0, 100) > 50:
                    cube_image = cube_image[:, :, ::-1]
                if random.randint(0, 100) > 50:
                    cube_image = cube_image[:, ::-1, :]

            means.append(cube_image.mean())
            img3d = prepare_image_for_net3D(cube_image, MEAN_PIXEL_VALUE)
            if train_set:
                if len(means) % 1000000 == 0:
                    print("Mean: ", sum(means) / len(means))
            img_list.append(img3d)
            class_list.append(class_label)

            batch_idx += 1
            if batch_idx >= batch_size:
                x = numpy.vstack(img_list)
                y_class = numpy.vstack(class_list)
                yield x, {"out_class": y_class}
                img_list = []
                class_list = []
                batch_idx = 0


# 三维卷积神经网络的训练过程
def train_3dcnn(train_gen, val_gen):
    # 加载预训练好的权重
    model = get_3dnnnet(load_weight_path='./model/3dcnn.hd5')
    history = History()
    model.summary(line_length=150)
    # 设置权重的中间存储路径
    checkpoint = ModelCheckpoint('./model/cpt_3dcnn_' + "{epoch:02d}-{binary_accuracy:.4f}.hd5",
                                 monitor='val_loss', verbose=1,
                                 save_best_only=True, save_weights_only=True, mode='auto', period=1)
    # 开始训练
    hist = model.fit_generator(
        generator=train_gen, steps_per_epoch=280, epochs=10,
        verbose=2,
        callbacks=[EarlyStopping(monitor='val_loss', patience=20),
                   history, checkpoint],
        validation_data=val_gen,
        validation_steps=60)

    plt.plot(hist.history['loss'])
    plt.plot(hist.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    # 保存训练过程的学习效果曲线
    plt.savefig("./temp_dir/chapter5/learning_curve.jpg")

if __name__ == '__main__':
    img_and_labels = []
    # 正样本集所在路径
    source_png_positive = "./data/chapter5/train/temp_cudes_pos/"
    # 负样本集所在路径
    source_png_negative = "./data/chapter5/train/temp_cudes_neg/"
    
    for each_image in os.listdir(source_png_positive):
        file_path = os.path.join(source_png_positive, each_image)
        img_and_labels.append((file_path, 1))
    for each_image in os.listdir(source_png_negative):
        file_path = os.path.join(source_png_negative, each_image)
        img_and_labels.append((file_path, 0))
    
    # 随机打乱正负样本： 80%作为训练集，20%作为验证集
    random.shuffle(img_and_labels) 
    train_res, holdout_res = img_and_labels[:int(len(img_and_labels) * 0.8)],\
    img_and_labels[int(len(img_and_labels) * 0.8):] 
    
    # 制定训练集和验证集的数据加载器(data_loader)
    train_generator = data_generator(BATCH_SIZE, train_res, True)
    val_generator = data_generator(BATCH_SIZE, holdout_res, False)
    # 调用训练函数，开始训练
    train_3dcnn(train_generator, val_generator)

