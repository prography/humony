"""Run inference a DeepLab v3 model using tf.estimator API."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import encodings
import argparse
import os
import sys

import tensorflow as tf

from .deeplab_model import *
from .utils import preprocessing
from .utils import dataset_util

from PIL import Image
import matplotlib.pyplot as plt
import cv2
import urllib.request
from io import BytesIO
from urllib import parse
import numpy as np

from tensorflow.python import debug as tf_debug
import datetime

parser = argparse.ArgumentParser()
date = datetime.datetime.now()
date = date.strftime('%Y/%m/%d/')
# date = str(datetime.datetime.strptime(date, '%Y/%m/%d/'))
# parser.add_argument('--data_dir', type=str, default='dataset/VOCdevkit/VOC2012/JPEGImages',
#                     help='The directory containing the image data.')
parser.add_argument('--infer_data_dir', type=str, default='./dataset/inpic/'+date,
                    help='Path to the file listing the inferring images.')

parser.add_argument('--segout_dir', type=str, default='./dataset/segpic/'+date,
                    help='Path to the directory to generate the inference results')

parser.add_argument('--cutout_dir', type=str, default='./dataset/outpic/'+date,
                    help='Path to the directory to generate the inference results')

parser.add_argument('--model_dir', type=str, default='./model',
                    help="Base directory for the model. "
                         "Make sure 'model_checkpoint_path' given in 'checkpoint' file matches "
                         "with checkpoint name.")

parser.add_argument('--base_architecture', type=str, default='resnet_v2_101',
                    choices=['resnet_v2_50', 'resnet_v2_101'],
                    help='The architecture of base Resnet building block.')

parser.add_argument('--output_stride', type=int, default=16,
                    choices=[8, 16],
                    help='Output stride for DeepLab v3. Currently 8 or 16 is supported.')

parser.add_argument('--debug', action='store_true',
                    help='Whether to use debugger to track down bad values during training.')

_NUM_CLASSES = 21

def humony_segment(url): # url을 넣으면 ./dataset/segmentation_output/ 에 seg 결과 넣어줌
    # Using the Winograd non-fused algorithms provides a small performance boost.
    tf.logging.set_verbosity(tf.logging.INFO)
    FLAGS, unparsed = parser.parse_known_args()
    os.environ['TF_ENABLE_WINOGRAD_NONFUSED'] = '1'

    pred_hooks = None
    if FLAGS.debug:
        debug_hook = tf_debug.LocalCLIDebugHook()
        pred_hooks = [debug_hook]

    infer_data_dir = FLAGS.infer_data_dir
    if not os.path.exists(infer_data_dir):
        os.makedirs(infer_data_dir)

    originNames = url.split("/")
    image_filename = originNames[len(originNames) - 1]
    image_path = infer_data_dir + image_filename

    urllib.request.urlretrieve(url, image_path.encode('utf-8'))

    model = tf.estimator.Estimator(
        model_fn= deeplabv3_model_fn,
        model_dir=FLAGS.model_dir,
    params={
        'output_stride': FLAGS.output_stride,
        'batch_size': 1,  # Batch size must be 1 because the images' size may differ
        'base_architecture': FLAGS.base_architecture,
        'pre_trained_model': None,
        'batch_norm_decay': None,
        'num_classes': _NUM_CLASSES,
    })

    predictions = model.predict(
        input_fn=lambda: preprocessing.eval_input_fn([image_path]),
        hooks=pred_hooks)

    segout_dir = FLAGS.segout_dir
    if not os.path.exists(segout_dir):
        os.makedirs(segout_dir)

    cutout_dir = FLAGS.cutout_dir
    if not os.path.exists(cutout_dir):
        os.makedirs(cutout_dir)

    image_basename = os.path.splitext(image_filename)[0]
    mask_filename = image_basename + '_seg.png'
    mask_path = segout_dir +  mask_filename
#    output_filename = image_basename + '_cut.png'
#    output_path = os.path.join(cutout_dir, output_filename)

    color_list = [[0, 0, 0]]

    for pred_dict, path in zip(predictions, [image_path]):
        print("generating:", mask_path)
        mask = pred_dict['decoded_labels']
        mask_list = mask.tolist()
        for i in range(mask.shape[0]):
            for j in range(mask.shape[1]):
                if mask_list[i][j] not in color_list:
                    color_list.append(mask_list[i][j])

        mask = Image.fromarray(mask)
        mask.save(mask_path)

    i = 0
    for color in color_list:
        color_list[i] = [color[2], color[1], color[0]]
        i += 1
    seg_data = []
    seg_data.append(image_path)
    seg_data.append(mask_path)
    seg_data.append(color_list)
    return seg_data

def humony_selcut(image_path, mask_path, color_list, col_sel_list): # mask에서 원하는 color에 해당하는 부분만 image에서 추출해서 잘라줌
    tf.logging.set_verbosity(tf.logging.INFO)
    FLAGS, unparsed = parser.parse_known_args()
    os.environ['TF_ENABLE_WINOGRAD_NONFUSED'] = '1'

    img = cv2.imread(image_path)
    mask = cv2.imread(mask_path)
    mask_list = mask.tolist()
#해당 경로에 이미지가 없는 경우 
    sel_mask = mask
    
    print('color_list: ', color_list, 'col_sel_list: ', col_sel_list)

    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            sel_mask[i][j] = [0, 0, 0]

            for col_index in col_sel_list:
                # print(color_list[col_index]) 
                print('col_index: ', col_index, 'color_list[col_index]: ', color_list[int(col_index)], 'mask: ', mask_list[i][j])
                #print('col_index: ', col_index, 'color_list: ', color_list, type(color_list), np.shape(color_list))

                
                if mask_list[i][j] == color_list[col_index]:
                    sel_mask[i][j] = mask_list[i][j]

    sel_mask = cv2.cvtColor(sel_mask, cv2.COLOR_BGR2GRAY)
    res = cv2.bitwise_and(img, img, mask=sel_mask)
    res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
    res = Image.fromarray(res)

    originNames = image_path.split("/")
    image_filename = originNames[len(originNames) - 1]
    image_basename = os.path.splitext(image_filename)[0]
    output_filename = image_basename + '_cut.png'
    output_path = FLAGS.cutout_dir + output_filename
    res.save(output_path)

    return output_path
