# class to check if images have been tampered with
# Attributes:

import imagehash #need to install imagehash (pip install imagehash)
from PIL import Image #need to install PIL (pip install Pillow)
from DB import DB

class ImageIntegrityAnalyzer:
    def __init__(self, original_image_path):
        self.original_image_path = original_image_path
        self.original_hash = self.calculate_image_hash(original_image_path)

    def calculate_image_hash(self, image_path):
        image = Image.open(image_path)
        image_hash = imagehash.average_hash(image)
        return image_hash

    def is_tampered(self, image_path):
        image_hash = self.calculate_image_hash(image_path)
        if image_hash == self.original_hash:
            return False  # Image has not been tampered with
        else:
            return True  # Image has been tampered with

# An example:
original_image_path = '(path of the original image)'
tampered_image_path = '(path of tempered image)'

analyzer = ImageIntegrityAnalyzer(original_image_path)
tampered = analyzer.is_tampered(tampered_image_path)

if tampered:
    print("The image has been tampered with.")
else:
    print("The image is not tampered.")
