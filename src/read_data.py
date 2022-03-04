# this module reads data into numpy dataframe for further modeling
import numpy as np
import pandas as pd
from PIL import Image
import os
from data_preprocessing import get_path

def read_picture(file_name):
    """
    Reads a picture from a file
    :param file_name: name of the file
    :return: picture as a numpy array
    """
    return np.array(Image.open(file_name))




def get_last_folder(path):
    """
    Returns the last folder in the path
    :param path: path to the folder
    :return: name of the folder
    """
    return path.split('\\')[-1]


def code_label(label, code_dict):
    """
    Converts label to a number
    :param label: label
    :return: number
    """
    return code_dict[label]




def read_data(path):
    """
    Reads data from the given path
    :param path: path to the folder with data
    :return: dataframe with data
    """
    
    # code dict

    code_dict={
        'dew': 0,
        'fogsmog': 1,
        'frost': 2,
        'glaze':3,
        'hail': 10,
        'lightning': 4,
        'rain':5,
        'rainbow': 6,
        'rime': 7,
        'snow': 8,
        'sandstorm': 9
    }


    data = []
    
    labels =[]



    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".jpg"):
                data.append(read_picture(os.path.join(subdir, file)))
                labels.append(
                                code_label
                                (
                                            get_last_folder(subdir),
                                            code_dict
                                )
                            )
    data = np.array(data)
    labels = np.array(labels)
    np.save('labels.npy',labels)
    np.save('data.npy',data)
    print(data)



if __name__=='__main__':
    print('statring to read data')
    read_data(get_path())
    #print(get_last_folder('C:\\PROJECTS\\weather-recognition\\weather-recognition\\data\\dew'))
    print('done')