import numpy as np
import pandas as pd
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

vertical = pd.concat([s1, s2])
print("\nStacked Vertically:")
print(vertical)

# Horizontal (side by side as columns)
horizontal = pd.concat([s1, s2], axis=1)
print("\nStacked Horizontally:")
print(horizontal)
