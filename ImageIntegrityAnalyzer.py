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
    
    def store_hashes(self):
        store_hash = input("Do you want to store the image hashes for security? (y/n): ")
        if store_hash.lower() == "y":
            db_name = input("Enter a name for the database: ")
            self.db = DB(db_name)
            
    def protect_directory(self):
        protect_dir = input("Do you want to protect a directory? (y/n): ")
        if protect_dir.lower() == "y":
            directory_path = input("Enter the path of the directory to protect: ")
            self.scan_directory(directory_path)
            
    def scan_directory(self, directory_path):
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                if self.is_tampered(file_path):
                    print(f"The file '{file}' has been tampered with.")
                elif self.is_previously_tampered(file_path):
                    print(f"The file '{file}' has been previously tampered with.")
                else:
                    print(f"The file '{file}' is not tampered.")
                    
    def is_tampered(self, image_path):
        image_hash = self.calculate_image_hash(image_path)
        if image_hash == self.original_hash:
            return False  # Image has not been tampered with
        else:
            if self.db:
                self.db.add(image_path, image_hash)
            return True  # Image has been tampered with

    def is_previously_tampered(self, image_path):
        if self.db:
            image_hash = self.calculate_image_hash(image_path)
            stored_hash = self.db.find(image_path)
            if stored_hash is not None and image_hash != stored_hash:
                return True  # Image has been previously tampered with
        return False  # Image has not been previously tampered with

    def close_db(self):
        if self.db:
            self.db.close()


original_image_path = '(path of the original image)'

analyzer = ImageIntegrityAnalyzer(original_image_path)
analyzer.store_hashes()
analyzer.protect_directory()

analyzer.close_db()
