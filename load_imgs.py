'''
This file '''
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import pathlib
DS_PATH = os.path.join(os.getcwd(), "mutant_plots")

train_ds = tf.keras.utils.image_dataset_from_directory(
  DS_PATH,
  validation_split=0.2,
  subset="training",
  seed=123,
  
  )