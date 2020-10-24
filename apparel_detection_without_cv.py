
import numpy as np
from itertools import chain
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from keras.models import load_model



def getPrediction(img_path):

    test_image = image.load_img(img_path, target_size=(224,224))
    test_image = image.img_to_array(test_image)
    x = np.expand_dims(test_image, axis=0)
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

# img_path=r'uploads/0ba3d536-8732-4ea1-b3e1-a1be86e5dc6a___RS_Erly.B_9499.JPG'
# getPrediction(img_path)

