import gzip
import pickle
import numpy as np
import os


def load_test_labels():

    f = gzip.open("t10k-labels-idx1-ubyte.gz", "rb")
    f.read(2)
    
    encoding = int.from_bytes(f.read(1), "little")
    dimension = int.from_bytes(f.read(1), "little")
    print(encoding, dimension)
  
    size = int.from_bytes(f.read(4), "big")
    print(size)

    for i in range(0, size):
        byte = int.from_bytes(f.read(1), "big")
        print(byte, end=" ")

if __name__ == "__main__":
    load_test_labels()
