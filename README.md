# Forensic_Vision
Combines tools from the following repos:
     https://github.com/Xander-FP/DOI/tree/master/doi

This tool was tested with python 3.11.3

create a virtual environment:
    python -m venv "forensics_vision"

Start the virtual environment:
    forensics_vision\Scripts\Activate

Install the following using pip:
    pip install numpy opencv-python pillow

Put weights files in folder config/weights. Download at least one from:
    http://pjreddie.com/media/files/yolov3.weights (recomended, for default configuration)