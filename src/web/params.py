import requests
#from api import get_weather_by_key



def get_weather_by_key(key):
    """
    Getting weather name by key
    """    
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

    code_reversed = dict((v, k) for k, v in code_dict.items())        
    return code_reversed[key]



def get_model_result(url, img):
    """
    Getting model result
    """
    # get the image
    img = np.array(Image.open(img).convert('L'))

    
    # return the result
    return None





