import numpy as np
from PIL import Image

# create a Canvas class object
class Canvas:
    """A canvas object where all shapes are going to be drawn, we can define the size and color of it"""
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        # 3d numpy array(i,j,k) with all the elements equal to 0 => pixel [0,0,0] equivalent to black in RGB.
        # "uint" is unsigned int => 0 to 255, and "int" => -128 to 127
        self.data = np.zeros((height, width, 3), dtype= np.uint8)
        # change black [0,0,0] to the canvas color that user given
        self.data[:] = color

    # method to create the canvas
    def make(self, img_path):
        np_data = Image.fromarray(self.data, mode="RGB")
        np_data.save(img_path)