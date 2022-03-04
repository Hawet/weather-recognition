#This notebook contains the code for the data augmentation of the weather data
from PIL import Image
import numpy as np
import os
from data_preprocessing import get_path


def augment_image(image):
    """
    Augment image by rotating it by angle degrees
    """
    image_open = Image.open(image)
    #image = image.rotate(angle)
    
    for angle in ([-20,20,45,90,-45]):
        image_rotated = image_open.rotate(angle)
        image_rotated.save(f'{image}_rotated_{angle}.jpg')





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
                print(os.path.join(subdir, file))
                augment_image(os.path.join(subdir, file))





if __name__=='__main__':
    print('statring to augment images')
    main()
    print('done')