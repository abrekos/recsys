import os
import pickle

def load(path: str):
    with open(os.path.join(path), "rb") as f:
        return pickle.load(f)