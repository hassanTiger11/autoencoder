'''
This file is influeced by Tensorflow tutorial
More edits will be applied to it
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
import os

from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, losses
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Model

def read_npy_file(item):
    data = np.load(item.decode())
    return data.astype(np.float32)


def load_dataset():
  PATH = os.path.join(os.getcwd(), 'subset_numpy')
  file_list = os.listdir(PATH)
  dataset = tf.data.Dataset.from_tensor_slices(file_list)
  dataset = dataset.map(
          lambda item: tuple(tf.py_func(read_npy_file, [item], [tf.float32,])))
  print(dataset)


class Autoencoder(Model):
  def __init__(self, latent_dim):
    super(Autoencoder, self).__init__()
    self.latent_dim = latent_dim   
    self.encoder = tf.keras.Sequential([
      layers.Flatten(),
      layers.Dense(latent_dim, activation='relu'),
    ])
    self.decoder = tf.keras.Sequential([
      layers.Dense(784, activation='sigmoid'),
      layers.Reshape((28, 28))
    ])

  def call(self, x):
    encoded = self.encoder(x)
    decoded = self.decoder(encoded)
    return decoded
