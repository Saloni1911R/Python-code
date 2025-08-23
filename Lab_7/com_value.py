#c.	Write a NumPy program to find common values between two arrays.
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])
a = np.intersect1d(arr1, arr2)
print("value:", a)
