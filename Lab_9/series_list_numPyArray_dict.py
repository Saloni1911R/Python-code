import pandas as pd
import numpy as np

list_data = [10, 20, 30, 40]
s_list = pd.Series(list_data)
print("\nSeries from List:")
print(s_list)

array_data = np.array([1, 2, 3, 4, 5])
s_array = pd.Series(array_data)
print("\nSeries from NumPy Array:")
print(s_array)

# From dictionary
dict_data = {'x': 10, 'y': 20, 'z': 30}
s_dict = pd.Series(dict_data)
print("\nSeries from Dictionary:")
print(s_dict)
