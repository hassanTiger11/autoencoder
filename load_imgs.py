import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import pathlib
dataset_url = "/xdisk/dukepauli/halnamer/autoencoder/mutant_plots"
data_dir = tf.keras.utils.get_file(origin=dataset_url,
                                   fname='shadows',
                                   untar=True)
data_dir = pathlib.Path(data_dir)

image_count = len(list(data_dir.glob('*/*/*.tif')))
print(f'image_count: {image_count}')