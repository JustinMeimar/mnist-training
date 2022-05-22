import gzip
import pickle
import numpy as np
import os


def load_train_images():

    f = gzip.open("train-images-idx3-ubyte.gz", "rb")
    f.read(2)
    
    encoding = int.from_bytes(f.read(1), "little")
    dimension = int.from_bytes(f.read(1), "little")
    print(encoding, dimension)
  
    n_imgs = int.from_bytes(f.read(4), "big")
    print(n_imgs)

    n_rows = int.from_bytes(f.read(4), "big")
    print(n_rows)

    n_cols = int.from_bytes(f.read(4), "big")
    print(n_cols)
    
    for i in range(0, n_rows):
        print("\n")
        for j in range(0, n_cols):
            pix = int.from_bytes(f.read(1), "big")
            print(pix, end=" ")

if __name__ == "__main__":
    load_train_images()







#for i in range(0, size):
    #    byte = int.from_bytes(f.read(1), "big")
    #    print(byte, end=" ")


