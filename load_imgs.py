'''
This file '''
import numpy as np
import os
import PIL
from PIL import Image
from scipy import misc

#import tensorflow as tf
#import tensorflow_datasets as tfds
import pathlib
import json
from tifffile import memmap
DS_PATH = os.path.join(os.getcwd(), "mutant_plots")
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
    numpy arrays with labels
    '''
    if(ds_filename_dict == {}):
        ds_filename_dict = json.load(open('ds.json', 'r+'))
    for lbl in ds_filename_dict:
        for i, path in enumerate (ds_filename_dict[lbl]):
            os.chdir()
            image_file = Image.open(path)
            im_array = misc.imread(image_file)
            ds_filename_dict[lbl][i] = im_array
    ds_numpy = ds_filename_dict
    output = open('ds_numpy.json', 'r+')
    json.dump(ds_numpy, output, indent=3)
    output.close()

create_filname_dict()
