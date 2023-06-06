# class to check if images have been tampered with
# Attributes:

from DB import DB
import imagehash
from PIL import Image

class ImageIntegrityAnalyzer:
    def __init__(self, original_image_path):
        self.original_image_path = original_image_path
        self.original_hash = self.calculate_image_hash(original_image_path)
        self.db = DB('image_hashes')

    def calculate_image_hash(self, image_path):
        image = Image.open(image_path)
        image_hash = str(imagehash.average_hash(image))
        return image_hash

    def is_tampered(self, image_path):
        image_hash = self.calculate_image_hash(image_path)
        if image_hash == self.original_hash:
            return False  # Image has not been tampered with
        else:
            self.db.add(image_path, image_hash)
            return True  # Image has been tampered with

    def is_previously_tampered(self, image_path):
        image_hash = self.calculate_image_hash(image_path)
        stored_hash = self.db.find(image_path)
        if stored_hash is not None and image_hash != stored_hash:
            return True  # Image has been previously tampered with
        else:
            return False  # Image has not been previously tampered with

    def close_db(self):
        self.db.close()

# Usage example:
original_image_path = 'path/to/original/image.jpg'
tampered_image_path = 'path/to/tampered/image.jpg'

analyzer = ImageIntegrityAnalyzer(original_image_path)
tampered = analyzer.is_tampered(tampered_image_path)

if tampered:
    print("The image has been tampered with.")
else:
    print("The image is not tampered.")

previously_tampered = analyzer.is_previously_tampered(tampered_image_path)

if previously_tampered:
    print("The image has been previously tampered with.")
else:
    print("The image has not been previously tampered.")

analyzer.close_db()
