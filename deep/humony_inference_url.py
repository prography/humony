"""Run inference a DeepLab v3 model using tf.estimator API."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys

import tensorflow as tf

from . import deeplab_model
from .utils import preprocessing
from .utils import dataset_util

from PIL import Image
import matplotlib.pyplot as plt
import cv2
import urllib.request
from io import BytesIO

from tensorflow.python import debug as tf_debug
import datetime

date = datetime.datetime.now()
date = date.strftime('%Y/%m/%d/')
# date = str(datetime.datetime.strptime(date, '%Y/%m/%d/'))
parser = argparse.ArgumentParser()

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






def humony(url, option):

  tf.logging.set_verbosity(tf.logging.INFO)
  FLAGS, unparsed = parser.parse_known_args()
  # Using the Winograd non-fused algorithms provides a small performance boost.
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
  image_path = infer_data_dir + '/' + image_filename

  urllib.request.urlretrieve(url, image_path)

  model = tf.estimator.Estimator(
      model_fn=deeplab_model.deeplabv3_model_fn,
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
  path_to_mask = os.path.join(segout_dir, mask_filename)
  output_filename = image_basename + '_cut.png'
  path_to_output = os.path.join(cutout_dir, output_filename)

  for pred_dict, path in zip(predictions, [image_path]):
      print("generating:", path_to_mask)
      mask = pred_dict['decoded_labels']
      mask = Image.fromarray(mask)
      mask.save(path_to_mask)

      img = cv2.imread(image_path)
      mask = cv2.imread(path_to_mask, 0)
      res = cv2.bitwise_and(img, img, mask=mask)
      res = Image.fromarray(res)
      res.save(path_to_output)
      print("generating:", path_to_output)
  if option == 1:
    return (path_to_mask)
  elif option == 2:
    return (path_to_output)

#
# if __name__ == '__main__':
#   tf.logging.set_verbosity(tf.logging.INFO)
#   FLAGS, unparsed = parser.parse_known_args()
#   humony(sys.argv[1])
#

