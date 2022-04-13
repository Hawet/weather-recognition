from numpy import imag
import requests
import io
import base64
from PIL import Image
import re


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


def base64_pil(msg):
    """
    base 64 img to Pil
    """
    #msg = msg[msg.find(b"<plain_txt_msg:img>")+len(b"<plain_txt_msg:img>"):msg.find(b"<!plain_txt_msg>")]
    #Using standard Base64 in URL requires encoding of '+', '/' and '=' characters into special percent-encoded hexadecimal 
    #sequences ('+' becomes '%2B', '/' becomes '%2F' and '=' becomes '%3D'), which makes the string unnecessarily longer.
    # see more at https://en.wikipedia.org/wiki/Percent-encoding
    if (msg.find("%")!=-1):
        #Replace "%2F" par  "/"
        msg = msg.replace("%2F", "/")
        msg = msg.replace("%2B", "+")
        #codec = codec.replace("%3D", "=")

    base64_data = re.sub('^data:image/.+;base64,', '', msg)

    msg = base64.b64decode(base64_data)

    buf = io.BytesIO(msg)
    buf.seek(0)
    img = Image.open(buf)
    return img



if __name__=='__main__':
    image = Image.open('test.png')
    print(get_model_result(image))




