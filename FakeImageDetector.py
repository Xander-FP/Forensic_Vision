import os
import numpy as np 
import cv2
import sys
from ManTraNet.src import modelCore

from PIL import Image
from io import BytesIO
from matplotlib import pyplot


manTraNet_root = './ManTraNet/'
manTraNet_srcDir = os.path.join( manTraNet_root, 'src' )
sys.path.insert( 0, manTraNet_srcDir )
manTraNet_modelDir = os.path.join( manTraNet_root, 'pretrained_weights' )

manTraNet_dataDir = os.path.join( manTraNet_root, 'data' )
sample_file = os.path.join( manTraNet_dataDir, 'samplePairs.csv' )
assert os.path.isfile( sample_file ), "ERROR: can NOT find sample data, check `manTraNet_root`"
with open( sample_file ) as IN :
    sample_pairs = [line.strip().split(',') for line in IN.readlines() ]
L = len(sample_pairs)
print("INFO: in total, load", L, "samples")
    
def get_a_random_pair() :
    idx = np.random.randint(0,L)
    return ( os.path.join( manTraNet_dataDir, this ) for this in sample_pairs[idx] ) 

manTraNet = modelCore.load_pretrain_model_by_index( 2, manTraNet_modelDir )
# ManTraNet Architecture 
# print(manTraNet.summary(line_length=120))

from datetime import datetime 
def read_rgb_image( image_file ) :
    rgb = cv2.imread( image_file, 1 )[...,::-1]
    return rgb
    
def decode_an_image_array( rgb, manTraNet ) :
    x = np.expand_dims( rgb.astype('float32')/255.*2-1, axis=0 )
    t0 = datetime.now()
    y = manTraNet.predict(x)[0,...,0]
    t1 = datetime.now()
    return y, t1-t0

def decode_an_image_file( image_file, manTraNet ) :
    rgb = read_rgb_image( image_file )
    mask, ptime = decode_an_image_array( rgb, manTraNet )
    return rgb, mask, ptime.total_seconds()
     

def get_image_from_url(url, xrange=None, yrange=None) :
    # response = requests.get(url)
    img = Image.open('Images/backpack1.png')
    img = np.array(img)
    if img.shape[-1] > 3 :
        img = img[...,:3]
    ori = np.array(img)
    if xrange is not None :
        img = img[:,xrange[0]:xrange[1]]
    if yrange is not None :
        img = img[yrange[0]:yrange[1]]
    mask, ptime =  decode_an_image_array( img, manTraNet )
    ptime = ptime.total_seconds()
    # show results
    if xrange is None and yrange is None :
        pyplot.figure( figsize=(15,5) )
        pyplot.title('Original Image')
        pyplot.subplot(131)
        pyplot.imshow( img )
        pyplot.title('Forged Image (ManTra-Net Input)')
        pyplot.subplot(132)
        pyplot.imshow( mask, cmap='gray' )
        pyplot.title('Predicted Mask (ManTra-Net Output)')
        pyplot.subplot(133)
        pyplot.imshow( np.round(np.expand_dims(mask,axis=-1) * img).astype('uint8'), cmap='jet' )
        pyplot.title('Highlighted Forged Regions')
        pyplot.suptitle('Decoded {} of size {} for {:.2f} seconds'.format( url, img.shape, ptime ) )
        pyplot.show()

get_image_from_url('https://www.stockvault.net/blog/wp-content/uploads/2015/08/july-2.jpg')