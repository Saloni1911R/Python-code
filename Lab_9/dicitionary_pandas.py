#Convert Dictionary to Pandas Series
import pandas as pd
import numpy as np
my_dict = {'a': 100, 'b': 200, 'c': 300}
s = pd.Series(my_dict)
print("\nDictionary to Series:")
print(s)
