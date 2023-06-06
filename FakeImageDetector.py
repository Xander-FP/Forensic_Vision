import os
import numpy as np 
import cv2
from Mantranet.src import modelCore
from PIL import Image

class FakeImageDetector:
    def __init__(self) -> None:
        # Get the ManTraNet model from the subdirectory
        manTraNet_root = './ManTraNet/'
        manTraNet_modelDir = os.path.join( manTraNet_root, 'pretrained_weights' )
        self.__manTraNet = modelCore.load_pretrain_model_by_index( 4, manTraNet_modelDir )

    def __decode_an_image_array(self, rgb, manTraNet ) :
        x = np.expand_dims( rgb.astype('float32')/255.*2-1, axis=0 )
        y = manTraNet.predict(x)[0,...,0]
        return y

    def analyzeImages(self,folder_name) :
        count = 0
        for filename in os.listdir(folder_name):
            if not 'results' in filename:
                continue
            if not filename.endswith(".jpg"):
                continue
            img = Image.open(os.path.join(folder_name, filename))
            print('Analyzing image: ' + filename)
            img = np.array(img)
            if img.shape[-1] > 3 :
                img = img[...,:3]
            mask = self.__decode_an_image_array( img, self.__manTraNet )
            cv2.imwrite(os.path.join('./results', 'FI'+filename), np.round(np.expand_dims(mask,axis=-1) * img).astype('uint8'))
            count += 1