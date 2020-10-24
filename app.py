from flask import Flask, request, jsonify, render_template
#from apparel_detection import get_dict 
import base64
from werkzeug.utils import secure_filename
import sys
import os
##In krish cotton static folder is also needed.

import numpy as np
from itertools import chain
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from keras.models import load_model
import os
import tensorflow as tf
import cv2























app=Flask(__name__)

@app.route('/')
def func():
    return(render_template('index.html'))

@app.route("/predict", methods=['POST'])
def predict_route():
    # Get the file from post request
    f = request.files['file']

    # Save the file to ./uploads
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(
        basepath, 'uploads', secure_filename(f.filename))
    f.save(file_path)
    return('I changed again')


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()




if __name__=='__main__':
    app.run(debug=True)


