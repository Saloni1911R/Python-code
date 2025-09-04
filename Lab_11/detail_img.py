#a.	Write a Python program to display details of an image (dimension of an image, shape of an image, min pixel value at channel B).
from PIL import Image
import numpy as np

img = Image.open(r"C:\Users\saloni\Pictures\Nagi.jpg")

img_array = np.array(img)

width, height = img.size
print(f"Dimensions: {width} x {height}")

print(f"Shape: {img_array.shape}") 

min_blue = img_array[:, :, 2].min()
print(f"Minimum pixel value in Blue channel: {min_blue}")
