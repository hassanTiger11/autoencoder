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

ds, ds_info = tfds.load(DS_PATH)
