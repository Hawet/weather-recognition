# flask API
import flask
from flask import request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from params import get_weather_by_key
import warnings

# ignore gpu memalloc warnings
warnings.filterwarnings('ignore')

# initialize model
model = load_model('model.h5')



# simple flask rest api
app = flask.Flask(__name__)
#app.config["DEBUG"] = True


# endpoint to predict image
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # get the image
        img = np.array(Image.open(request.files['image'].stream).convert('L'))

        # predict the image
        list_of_probas = model.predict(img.reshape(1,128,128,1)).flatten()
        index_max = max(range(len(list_of_probas)), key=list_of_probas.__getitem__)
        final_predict = get_weather_by_key(index_max)

        # return the result
        print(list_of_probas)
        print(index_max)
        return jsonify(final_predict)


# endpoint to get model details
@app.route('/model', methods=['GET'])
def model_details():
    if request.method == 'GET':
        return jsonify(model.to_json())


if __name__ == '__main__':
    app.run(debug=True)

