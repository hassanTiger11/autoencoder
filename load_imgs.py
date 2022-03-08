'''
This file works on preprocessing the tiff images
1) I create a json file that keeps track of the file names of my ds
        {
            ds:
                label:
                    [img1, img2, ....]
                ...

        }
2) I create a numpy folder containing all of the images converted to numpy arrays
    It follows the same structure as before
    
3) I pull the numpy arrays into a tensorflow dataset
    WARNING: I apply a reshape transformation on the arrays so I can fit them into 
    a dataset
    
    Note to self:
    load_dataset has a problem when being use with fitting the network'''
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
    '''
    WARNING: This function uses reshape so I can fit the data into a tf dataset obj
    '''
    print(f'filename: {item}')
    path = os.path.join(os.getcwd(), 'subset_numpy', item)
    data = np.load(path)
    
    print(f'{path}=\n{np.shape(data)}', file=open('shapes', 'a+'))
    return data.astype(np.float32)

def create_generator(list_of_arrays):
    for i in list_of_arrays:
        yield i

def load_dataset():
    print('---------load_dataset----------')
    PATH = os.path.join(os.getcwd(), 'subset_numpy')
    file_list = os.listdir(PATH)
    dataset = {}

    for elem in file_list:
        print(f'type: {type(elem)} --> {elem}')
        filename_without_extension = elem.split('.')[0]
        dataset[filename_without_extension]= read_npy_file(elem)

    
    for elem in dataset:
        print(f'type: {type(elem)} --> {elem}')
    dataset = tf.data.Dataset.from_generator(lambda: create_generator(tuple(dataset)),output_types= tf.float32, output_shapes=(None,4))
    #dataset = tf.data.Dataset.from_tensor_slices(tuple(dataset))
    print(f'dataset = {dataset}')
    return dataset

def load_dataset2():
    print('---------load_dataset2----------')
    PATH = os.path.join(os.getcwd(), 'subset_numpy')
    file_list = os.listdir(PATH)
    dataset =  tf.data.Dataset.from_tensor_slices(file_list)
    dataset = dataset.map(lambda item: read_npy_file(item))
    dataset = dataset.shuffle(100)
    dataset.padded_batch(35)
    dataset = dataset.repeat()
    print(f'dataset: {dataset}')
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
    load_dataset2()
