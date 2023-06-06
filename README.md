# Forensic_Vision
Combines tools from the following repos:
     https://github.com/Xander-FP/DOI/tree/master/doi and https://github.com/ISICV/ManTraNet/blob/master/Readme.md

This tool was tested with python 3.11.3

create a virtual environment:
    python3.7 -m venv "forensics_vision"

Start the virtual environment:
    forensics_vision\Scripts\Activate

Install the following using pip:
    pip install numpy opencv-python pillow matplotlib keras==2.2.0 tensorflow==1.13.1 h5py==2.10.0 protobuf==3.20.*
    pip install Pillow 
    pip install imagehash 
    
Put weights files in folder config/weights. Download at least one from:
    http://pjreddie.com/media/files/yolov3.weights (recomended, for default configuration)
    
