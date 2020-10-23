
import numpy as np
from itertools import chain
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from keras.models import load_model
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.python.util import deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
import cv2





def getPrediction(img_path):
    img = cv2.imread(img_path)
    dim = (224, 224)
    #What is interpolation
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    #Why to use preprocess_input
    x = preprocess_input(x)

    class_names = ['Goggles', 'Hat', 'Jacket', 'Shirt', 'Shoes', 'Shorts', 'T-Shirt', 'Trouser', 'Wallet', 'Watch']
    model = load_model("fashion.h5")

    preds = model.predict(x)
    #preds will be in ndarray 2D ,so to make dict ... making it in list
    print('preds is:',preds,type(preds))
    print(preds[0][0])
    # preds_unlist will be a list in float... 0.0,1.0
    preds_unlist = list(chain(*preds))
    print('preds_unlist is ',preds_unlist,type(preds_unlist))
    #making the float to int
    preds_int = [int((round(i, 2))) for i in preds_unlist]
    print('preds_int is',preds_int,type(preds_int))
    # self.final_pred_unused = dict(zip(self.class_names,self.preds_int))
    #Making dictionary of labels and the output
    final_pred = dict(zip(class_names, preds_int))
    print('final_pred',final_pred,type(final_pred))
    # finale = final_pred[1]
    print(100 * '-')
    #Inverting to value,key to dict.... multiple 0 values are gonna merge to single ... so there would be one 0 and one 1
    inverse_final_pred={v:k for k,v in final_pred.items()}
    apparel=inverse_final_pred[1]
    print('apparel',apparel)
    return apparel


def get_dict():
    a={'Goggles': 0, 'Hat': 0, 'Jacket': 0, 'Shirt': 0, 'Shoes': 0, 'Shorts': 0, 'T-Shirt': 0, 'Trouser': 1, 'Wallet': 0, 'Watch': 0}
    return(a)

