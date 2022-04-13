import base64
from PIL import Image
import io
import re

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


base_str = 'data:image/jpeg;base64,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'

base64_pil(base_str).show()