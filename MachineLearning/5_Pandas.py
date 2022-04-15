import pandas as pd
import numpy as np
df = pd.read_csv('test.csv', header=None)
print(df)
print(df[3])
df = df[3]
df.to_csv('phuong.csv')