#a.	Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
import pandas as pd
import numpy as np
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([1, 2, 3, 4])

print("\nAddition:\n", s1 + s2)
print("\nSubtraction:\n", s1 - s2)
print("\nMultiplication:\n", s1 * s2)
print("\nDivision:\n", s1 / s2)
