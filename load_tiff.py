'''
This file uses the experimental tool published by tensorflow to load
tiff files
'''

import pandas as pd
import tensorflow as tf
import numpy as np
import json
import tensorflow_io as tfio
import os
def get_dataframe():
    '''Create a datrame from json file'''
    file = open('ds.json', 'r')
    df = pd.DataFrame(json.load(file))
    file.close()
    return df

def decode_img(img):

    print(f'decoding ... ')
    img = tfio.experimental.image.decode_tiff(img, index=0, name=None)

    # resize the image to the desired size
    return tf.image.resize(img, [256, 256])


def process_path(file_path):

    # load the raw data from the file as a string
    print(f'reading {file_path}')
    img = tf.io.read_file(file_path)
    img = decode_img(img)

    return img


def load_from_df(df):
    '''
    This function loads a tensorflow dataset from pandas dataframe
    WARNINGL: This is for expermentation, edit code to automize
    '''
    if(df.empty):
        df = pd.read_csv('ds.csv')
    ds = []
    for i, img in enumerate(df['2020-06-23__10-36-48-868']):
        tensor = tf.convert_to_tensor(img)
        ds.append(tensor)
    
    print(ds)
    return ds
if __name__ == '__main__':
    df = get_dataframe()
    print(f'df_size = {df.size}')
    
    

    list_ds = tf.data.Dataset.from_tensor_slices(df['2020-06-23__10-36-48-868'].values)
    for i, img in enumerate(df['2020-06-23__10-36-48-868']):
        print(f'{i}: {img}')
        df['2020-06-23__10-36-48-868'][i] = process_path(img)

    load_from_df(df)