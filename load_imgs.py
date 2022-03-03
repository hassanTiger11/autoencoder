import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import pathlib
IMAGE_PATH = os.path.join(os.getcwd(), "mutant_plots")

builder = tfds.ImageFolder(IMAGE_PATH)
print(builder.info)  # num examples, labels... are automatically calculated
ds = builder.as_dataset(split='train', shuffle_files=False)
tfds.show_examples(ds, builder.info)