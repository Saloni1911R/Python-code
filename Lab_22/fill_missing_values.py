import pandas as pd
import numpy as np

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 2. Fill missing values with the mean of the Age column
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("\nDataFrame After Filling Missing Values:")
print(df)
