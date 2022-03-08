  
from autoencoder import *
from load_imgs import load_dataset

ds = load_dataset()

autoencoder = Autoencoder(64) 

autoencoder.compile(optimizer='adam', loss=losses.MeanSquaredError())

autoencoder.fit(ds, ds,
                epochs=10,
                shuffle=True,
                validation_data=(x_test, x_test))
autoencoder.save('saved_models/autoencoder_0')