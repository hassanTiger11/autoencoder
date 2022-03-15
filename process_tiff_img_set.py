'''
This file uses the experimental tool published by tensorflow to load
tiff files

I expect the subset ot look like:
foldername:
        label1:
            img1
            img2
            img3 
            ...
        ...

I produce a list of all images in all files without labels:
[ tensor(img1), tensor(img2), ...]

'''

import pandas as pd
import tensorflow as tf
import numpy as np
import json
import tensorflow_io as tfio
import os

from load_tiff import process_path


class process_tiff_img_set():
    def __init__(self, ds_folder_name):
        
        self.folder = ds_folder_name
        self.df =  self.create_df()
        

    def create_df(self):
        '''
        This function creates a dataframe with all labels and 
        images file paths
        I will use later to store numpy arrays
        '''
        ds = []
        DS_PATH = os.path.join(os.getcwd(), self.folder)
        labels = os.listdir(DS_PATH)
        for lbl in labels:
            cwd = os.path.join(DS_PATH, lbl)
            if(not os.path.isdir(cwd)):
                print(f'{cwd} is not a directory. Will not be in dict')
                continue
            images = os.listdir(cwd)
            for img in images:
                #convert to numpy matrix here
                if(img.split('.')[1] != 'tif'):
                    print(f'{img} is not a tiff file. Will not be in dict')
                    continue
                path = os.path.join(cwd, img)

                #changes
                img_np = process_path(path) #Tensor 
                ds.append(img_np)

        #df = pd.DataFrame(ds)
        #df.to_csv('ds.csv')
        return ds
        
    def get_dataframe(self):
        '''Create a datrame from json file'''
        file = open('ds.json', 'r')
        df = pd.DataFrame(json.load(file))
        file.close()
        return df

    def decode_img(self, img):
        #print(f'decoding ... ')
        img = tfio.experimental.image.decode_tiff(img, index=0, name=None)
        # resize the image to the desired size
        return tf.image.resize(img, [256, 256])


    def process_path(self, file_path):

        # load the raw data from the file as a string
        #print(f'reading {file_path}')
        img = tf.io.read_file(file_path)
        img = self.decode_img(img)

        return img

    def get_tensor(self):
        return (self.df)


    def __str__(self):
        obj_str = ""
        for i, obj in enumerate(self.df):
            obj_str += f'{i}: {str(obj)},\n'
        return f'<process_tiff_img_set>:\n{obj_str}'


if __name__ == '__main__':
    pre_process = process_tiff_img_set('subset')
    print(pre_process)
