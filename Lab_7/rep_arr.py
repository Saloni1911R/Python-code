#Write a NumPy program to repeat array elements.
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])
common_values = np.intersect1d(arr1, arr2)
print("Common values:", common_values)
