import PIL.Image as Image
import numpy as np

from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from tensorflow.keras.models import load_model

IMG_HEIGHT = 180
IMG_WIDTH = 180
IMG_CHANNEL = 3

model = load_model("drone_model")
classes = ['broadleaf', 'grass', 'soil', 'soybean'] 

def preprocess_image(img_src):
    img = Image.open(img_src).resize([180,180],resample=0)
    X = np.array(img)
    X = X.reshape([1, 180, 180, 3])
    y = classes.index(img_src.split('/')[-2])
    return (X, y)


def predict_image(img_src):
    X, y = preprocess_image(img_src)

    pred = model.predict(X)[0]
    actual = y
    return pred, actual

def control_drone(image_class):
    # make drone descend if the image class is weed
    # Store drones location
    pass

def controller(img_src):
    #img = preprocess_image(img_src)

    #cls = predict_image(img)

    #control_drone(cls)
    pass

