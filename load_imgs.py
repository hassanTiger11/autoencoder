'''
This file '''
import numpy  
import numpy as np
import os
from PIL import Image
from scipy import misc
import imageio
#import tensorflow as tf
#import tensorflow_datasets as tfds
import pathlib
from pathlib import Path
import json
import tensorflow as tf
import sys
from tifffile import memmap

def read_npy_file(item):
    data = np.load(item.decode())
    print(f'{item}=\n{data}')
    return data.astype(np.float32)


def load_dataset():
    print('---------load_dataset----------')
    PATH = os.path.join(os.getcwd(), 'subset_numpy')
    file_list = os.listdir(PATH)
    dataset = tf.data.Dataset.from_tensor_slices(file_list)
    for elem in dataset:
        print(f'type: {type(elem)} --> {elem}')
    #dataset = dataset.map(lambda item: tuple(tf.numpy_function(read_npy_file, [item], [tf.float32,])))

    
    return dataset


DS_PATH = os.path.join(os.getcwd(), "subset")
def create_filname_dict():
    '''
    This function creates a dictionary with all labels and 
    images file paths
    I will use later to store numpy arrays
    '''
    ds = {}
    labels = os.listdir(DS_PATH)
    for lbl in labels:
        cwd = os.path.join(DS_PATH, lbl)
        images = os.listdir(cwd)
        for img in images:
            if(lbl in ds):
                print(f'#ds[{lbl} = [..., {os.path.join(cwd, img)}]')
                ds[lbl].append(os.path.join(cwd, img))
            else:
                print(f'*ds[{lbl} = [{os.path.join(cwd, img)}]]')
                ds[lbl] = []
                ds[lbl].append(os.path.join(cwd, img))
    output = open('ds.json', 'r+')
    json.dump(ds, output, indent=3)
    output.close()

def load_numpy_dict_from_json(ds_filename_dict={}):
    '''
    This function takes in the file paths dataset and turns them into
    numpy dataset
    To scale up change PATH names
    '''
    
    if(ds_filename_dict == {}):
        ds_filename_dict = json.load(open('ds.json', 'r+'))
    for lbl in ds_filename_dict:
        
        for i, path in enumerate (ds_filename_dict[lbl]):
            print(f'reading{i}: {path}')
            filename = path.split('/')[-1].split('.')[0]
            image_file = imageio.imread(path)
            im_array = numpy.array(image_file)
            Path(f'subset_numpy/{filename}.npy').touch(exist_ok=True)
            numpy.save(f'subset_numpy/{filename}.npy', im_array)
    
    

if __name__ == "__main__":
    load_dataset()
