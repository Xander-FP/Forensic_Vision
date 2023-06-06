# A class to convert all images to jpeg format
# Stores all ready images in a new folder called processedImages
import os
from PIL import Image
import shutil

class PreProcessor:
    def __init__(self) -> None:
        pass

    def convertToJpeg(self, folder_path):
        # Delete the results folder
        if os.path.exists('results'):
            shutil.rmtree('results')
        os.makedirs('results')
        # Create a new folder to store the processed images
        if not os.path.exists('processedImages'):
            os.makedirs('processedImages')

        for filename in os.listdir(folder_path):
            file_path = os.path.abspath(os.path.join(folder_path, filename))
            image = self.__get_pil_image(file_path)
            if image is not None:
                #if image format not supported
                if image.format not in ['jpg', 'jpeg']:
                    try:
                        converted_im = image.convert()
                        converted_im.save(os.path.join('./processedImages', filename.split('.')[0] + '.jpg'))
                    except:
                        pass
                else:
                    print(filename)
                    image.save(os.path.join('./processedImages', filename))
                image.close()
        return 'processedImages'
                

    def __get_pil_image(self,file_path):
        try:
            return Image.open(file_path)
        except IOError:
            return None
        
    def cleanUp(self):
        if os.path.exists('processedImages'):
            shutil.rmtree('processedImages')