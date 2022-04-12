from numpy import imag
import requests
#from api import get_weather_by_key
from PIL import Image
import io


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


def get_model_result(image):
    """
    this function sends http request to mode lservice to classify picture
    """
    URL = 'http://localhost:5000/predict'
    buf = io.BytesIO()

    image = image.resize((128, 128))
    image.save(buf, format='PNG')
    buf.seek(0)
    rs = requests.post(URL, files={'image': ('image', buf, 'image/png')})
    return rs.json()


import base64
from io import BytesIO
from PIL import Image
 
def base64_pil(msg):
  """
  base 64 img to Pil
  """
  #msg = msg[msg.find(b"<plain_txt_msg:img>")+len(b"<plain_txt_msg:img>"):msg.find(b"<!plain_txt_msg>")]
  msg = base64.b64decode(msg)
  
  buf = io.BytesIO(msg)
  img = Image.open(buf)
  return img


if __name__=='__main__':
    image = Image.open('test.png')
    print(get_model_result(image))




