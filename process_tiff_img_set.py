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
        #self.ds = self.load_from_df()
        self.ds = self.df

       

    def create_df(self):
        '''
        This function creates a dataframe with all labels and 
        images file paths
        I will use later to store numpy arrays
        '''
        ds = {}
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
                img_np = process_path(path) #Tensor 
                if(lbl in ds):
                    #print(f'#ds[{lbl} = [..., {os.path.join(cwd, img)}]')
                    
                    ds[lbl].append(img_np)
                else:
                    #print(f'*ds[{lbl} = [{os.path.join(cwd, img)}]]')
                    ds[lbl] = []
                    ds[lbl].append(img_np)
        df = pd.DataFrame.from_dict(ds)
        df.to_csv('ds.csv')
        return df
        
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


    def load_from_df(self):
        '''
        This function loads a tensorflow dataset from pandas dataframe
        WARNINGL: This is for expermentation, edit code to automize
        '''
        df = self.df
        if(df.empty):
            #print(f'df is empty, loading existing df')
            df = pd.read_csv('ds.csv')
        self.ds = {}
        for date in df:
            for i, img in enumerate(date):
                tensor = tf.convert_to_tensor(img)
                if(date not in self.ds):
                    self.ds[date] = []
                self.ds[date].append(tensor)
        pd.DataFrame(self.ds).to_csv('processed_ds.csv')
        return self.ds

    def get_tensor(self):
        return pd.DataFrame(self.ds)
    def get_dataframe(self):
        return self.df

    def __str__(self):
        obj_str = ""
        for i, obj in enumerate(self.ds):
            obj_str += f'{i}: {str(obj)},\n'
        return f'<process_tiff_img_set>:\n{obj_str}'


if __name__ == '__main__':
    pre_process = process_tiff_img_set('subset')
    print(pre_process)
