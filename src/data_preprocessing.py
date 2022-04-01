# this module contains data preprocessing functions for the weather data
import numpy as np
import pandas as pd
from PIL import Image
import os



def get_path():
    
    script_path = os.path.realpath(__file__)
    parent_path = os.path.dirname(script_path)
    parent_path = os.path.dirname(parent_path)
    return parent_path


def preprocess_images(filename: str):
    """
    Preprocess images in the given folder.
    args: folder - name of the folder with images outside of src folder
    """   
    image = Image.open(filename).convert('L')
    new_image = image.resize((128, 128))
    new_image.save(filename)




def main():
    """
    Main function
    """
    script_path = os.path.realpath(__file__)
    parent_path = os.path.dirname(script_path)
    parent_path = os.path.dirname(parent_path)
    
    for subdir, dirs, files in os.walk(get_path()):
        for file in files:
            if file.endswith(".jpg"):
                preprocess_images(os.path.join(subdir, file))
    




if __name__=='__main__':
    print('statring to preprocess images')
    main()
    print('done')

