import sys
import time 
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt
import json
from PIL import Image
import argparse






class_name = {}

def process_im(im): 
    im_size= 224
    im = tf.cast(im, tf.float32)
    im= tf.image.resize(im, (im_size, im_size))
    im /= 255
    return im.numpy()
    

def predict(im_path, model, top_k=5):
    
    im = Image.open(im_path)
    im = np.asarray(im)
    im = process_im(im)
    im= np.expand_dims(im,  axis=0)
    pre_list= = model.predict(im)
    
    
    clas= = []
    prob = []
    
    rank = pre_list[0].argsort()[::-1]
    
    for i in range(top_k):
        
        index = rank[i] + 1
        clas = class_name[str(index)]
        
        prob.append(pre_list[0][index])
        clas.append(clas)
    
    return probs, classes


if __name__ == '__main__':
    print('predict.py, running')
    
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1')
    parser.add_argument('arg2')
    parser.add_argument('--top_k')
    parser.add_argument('--category_names') 
    
    
    arg = parser.parse_args()
    print(arg)
    
    print('arg1:', arg.arg1)
    print('arg2:', arg.arg2)
    print('top_k:', arg.top_k)
    print('category_names:', arg.category_names)
    
    im_path = arg.arg1
    with open(args.category_names, 'r') as f:
        class_name = json.load(f)
    
    reloaded_model = tf.keras.models.load_model(arg.arg2 ,custom_objects={'KerasLayer':hub.KerasLayer} )
    top_k = arg.top_k
    
    prob, clas= predict(im_path, model, top_k)
    
    print ('Top {} Classes '.format(top_k))
    print('Probability:{}'.format(prob))
    print('Class name:{}'.format(clas))