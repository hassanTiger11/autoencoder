  
from autoencoder import *
from process_tiff_img_set import process_tiff_img_set

x_train = process_tiff_img_set("./subset")
x_train = x_train.get_tensor()


x_test = process_tiff_img_set('./subset2')
x_test = x_test.get_tensor()


print(f'x_train shape: {x_train.shape}')
print(f'x_test shape: {x_test.shape}')

#print(f'{ds}')

x_train=np.asarray(x_train).astype(np.float32)

autoencoder = Autoencoder(64) 

autoencoder.compile(optimizer='adam', loss=losses.MeanSquaredError())

autoencoder.fit(x_train, x_train,
                epochs=1,
                shuffle=True,
                validation_data=(x_test, x_test), verbose=1)
autoencoder.save('saved_models/autoencoder_0')