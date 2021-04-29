# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  Copyright (c) 2021. Reda Bouadjenek, Deakin University                      +
#     Email:  reda.bouadjenek@deakin.edu.au                                    +
#                                                                              +
#  Licensed under the Apache License, Version 2.0 (the "License");             +
#   you may not use this file except in compliance with the License.           +
#    You may obtain a copy of the License at:                                  +
#                                                                              +
#                 http://www.apache.org/licenses/LICENSE-2.0                   +
#                                                                              +
#    Unless required by applicable law or agreed to in writing, software       +
#    distributed under the License is distributed on an "AS IS" BASIS,         +
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  +
#    See the License for the specific language governing permissions and       +
#    limitations under the License.                                            +
#                                                                              +
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


import sys, os, h5py
import numpy as np
import tensorflow as tf
from keras.preprocessing import image
from tensorflow.keras import models
from tensorflow.python.keras.saving import hdf5_format
from tensorflow.keras import layers
from tensorflow import keras

if __name__=="__main__":
    if len(sys.argv)==1:
        input_dir = '.'
        output_dir = '.'
    else:
        input_dir = os.path.abspath(sys.argv[1])
        output_dir = os.path.abspath(sys.argv[2])
        
    print("Using input_dir: " + input_dir)
    print("Using output_dir: " + output_dir)
    print(sys.version)
    print("Tensorflow version: " + tf.__version__)

    # Loading the model.
    model = 'model.h5'
    with h5py.File(model, mode='r') as f:
        model_loaded = hdf5_format.load_model_from_hdf5(f)
        print(model_loaded.summary())
        try:
            class_names = f.attrs['class_names']
        except: 
            class_names = ['abraham_grampa_simpson', 'apu_nahasapeemapetilon', 
            'bart_simpson', 'charles_montgomery_burns', 'chief_wiggum', 'comic_book_guy', 
            'edna_krabappel', 'homer_simpson', 'kent_brockman', 'krusty_the_clown', 
            'lenny_leonard', 'lisa_simpson', 'marge_simpson', 'mayor_quimby', 
            'milhouse_van_houten', 'moe_szyslak', 'ned_flanders', 'nelson_muntz', 
            'principal_skinner', 'sideshow_bob']


    input_shape = model_loaded.input_shape
    image_size = np.array(input_shape[1:3])

    print('Size of inputs images: ' + str(image_size))
    # Reading test images.    
    files = []
    images = []
    for file in os.listdir(input_dir):
        if file.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            img = image.load_img(os.path.join(input_dir, file), 
                target_size=image_size)
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            images.append(x)
            files.append(file)
    images = np.vstack(images)
    
    # Making predictions!
    batch_size = 16
    y_proba = model_loaded.predict(images, batch_size=batch_size)
    y_predict = np.argmax(y_proba,axis=1)
    # Writting predictions to file.
    with open(os.path.join(output_dir, 'answer.txt'), 'w') as result_file:
        for i in range(len(files)):    
            result_file.write(files[i] + ',' + class_names[y_predict[i]] + '\n')
