import gzip
import pickle
import numpy as np
import os
import sys
from time import time
from functools import wraps
from train_labels import *

glbl_c = 10

def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        ts = time()
        result = f(*args, **kwargs)
        te = time()
        dif = round(te - ts, 5)
        print(f"{f.__name__} completed in .. {dif} secs")
        return result
    return wrap

@timing
def load_train_images():

    f = gzip.open("train-images-idx3-ubyte.gz", "rb")
    f.read(2)
    
    lbls = load_train_labels() 

    encoding = int.from_bytes(f.read(1), "little")
    dimension = int.from_bytes(f.read(1), "little")
    print(encoding, dimension)
  
    n_imgs = int.from_bytes(f.read(4), "big")//10
    n_imgs = glbl_c #overwrite for testing purpouse 
    n_rows = int.from_bytes(f.read(4), "big")
    n_cols = int.from_bytes(f.read(4), "big") 
    imgs = np.zeros(shape=[n_imgs, 1], dtype=np.ndarray)
    
    for k in range(0, n_imgs):

        img = np.zeros(shape=[28,28], dtype=np.uint8) #declacre unsigned byes as datatype 
        for i in range(0, n_rows):  
            for j in range(0, n_cols):
                pix = int.from_bytes(f.read(1), "big") 
                img[i][j] = pix 
        
        imgs[k] = [(img, lbls[k*n_imgs + i][0])]
    
    return imgs

if __name__ == "__main__":
    load_train_images()
