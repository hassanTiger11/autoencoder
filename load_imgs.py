'''
This file '''
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import pathlib
import json
from tifffile import memmap
DS_PATH = os.path.join(os.getcwd(), "mutant_plots")
def create_filname_dict():
    ds = {}
    labels = os.listdir(DS_PATH)
    for lbl in labels:
        cwd = os.path.join(DS_PATH, lbl)
        images = os.listdir(cwd)
        for img in images:
            if(lbl in ds):
                ds[lbl].append(os.path.join(cwd, img))
            else:
                ds[lbl] = []
                ds[lbl].append(os.path.join(cwd, img))
    output = open('ds.json'm 'r+')
    json.dump(ds, output, indent=3)
    output.close()

create_filname_dict()
