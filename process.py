import os
import pandas as pd
from process_tiff_img_set import process_tiff_img_set
from autoencoder import Autoencoder
import numpy as np
import tensorflow as tf
import tf.keras.losses as losses



x_train = process_tiff_img_set("subset")
x_train = x_train.get_tensor()


x_test = process_tiff_img_set('subset2')
x_test = x_test.get_tensor()

#x_train & x_test are a list of tensors
#each tensor is 256x256, dtype=float32
#
#print to get more insight
#print(f'x_train: {x_train}')
#print(f'x_test: {x_test}')



x_train=np.asarray(x_train).astype(np.float32)

autoencoder = Autoencoder(4) 

autoencoder.compile(optimizer='adam', loss=losses.MeanSquaredError())

history = autoencoder.fit(x_train, x_train,
                epochs=10,
                batch_size = 2,
                shuffle=True,
                validation_data=(x_test, x_test), verbose=1)
autoencoder.save('saved_models/autoencoder_0')