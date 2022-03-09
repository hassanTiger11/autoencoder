'''
This file '''
import numpy 
import os
from PIL import Image
from scipy import misc
import imageio
#import tensorflow as tf
#import tensorflow_datasets as tfds
import pathlib
import json
from tifffile import memmap
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
    output = open('ds.json', 'w+')
    json.dump(ds, output, indent=3)
    output.close()

def load_numpy_dict_from_json(ds_filename_dict={}):
    '''
    This function takes in the file paths dataset and turns them into
    numpy arrays with labels
    '''
    counter = 1
    if(ds_filename_dict == {}):
        ds_filename_dict = json.load(open('ds.json', 'r+'))
    for lbl in ds_filename_dict:
        for i, path in enumerate (ds_filename_dict[lbl]):
            print(f'reading{counter}: {path}')
            image_file = imageio.imread(path)
            im_array = numpy.array(image_file)
            ds_filename_dict[lbl][i] = im_array
            counter+=1
    ds_numpy = ds_filename_dict
    output = open('ds_numpy.json', 'r+')
    json.dump(ds_numpy, output, indent=3)
    output.close()

if __name__ == "__main__":
    create_filname_dict()
    
    #load_numpy_dict_from_json({})
