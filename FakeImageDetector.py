import os
import numpy as np 
import cv2
from ManTraNet.src import modelCore
from PIL import Image

# Get the ManTraNet model from the subdirectory
manTraNet_root = './ManTraNet/'
manTraNet_srcDir = os.path.join( manTraNet_root, 'src' )
manTraNet_modelDir = os.path.join( manTraNet_root, 'pretrained_weights' )
manTraNet = modelCore.load_pretrain_model_by_index( 4, manTraNet_modelDir )

def decode_an_image_array( rgb, manTraNet ) :
    x = np.expand_dims( rgb.astype('float32')/255.*2-1, axis=0 )
    y = manTraNet.predict(x)[0,...,0]
    return y

def checkImages(folder_name) :
    # response = requests.get(url)
    img = Image.open('./ManTraNet/data/forged/I05_clefa92_0.jpg')
    img = np.array(img)
    if img.shape[-1] > 3 :
        img = img[...,:3]
    mask =  decode_an_image_array( img, manTraNet )
    cv2.imwrite('mask.jpg', np.round(np.expand_dims(mask,axis=-1) * img).astype('uint8'))
    cv2.imwrite('forged.jpg', mask)
