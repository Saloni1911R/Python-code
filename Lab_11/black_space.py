#b.	Write a Python program to padding black spaces 
from PIL import Image
import numpy as np

img = Image.open(r"C:\Users\saloni\Pictures\Nagi.jpg")
image_np = np.array(img)
top, bottom, left, right = 50, 50, 100,100
padded_image = np.pad(image_np,((top,bottom),(left,right),(0,0)),constant_values = 0)
image = Image.fromarray(padded_image)

image.show(title="Black Padded Image")