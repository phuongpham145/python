import pandas as pd
import numpy as np
S = pd.Series(np.random.randint(100, size = 4))
print(S)
print(S.index)
print(S.values)
print(type(S))
keyValue = ['Kien truc', 'Xay dung', 'CNTT', 'Du Lich']
value = [317, 369, 588, 341]
S = pd.Series(value, index = keyValue)
print(S)
print(S.index)
print(S.values)
dict = {
    'a':[11, 21, 31, 15, 4],
    'b':[12.5, 22.9, 32.3, 71.7, 3.4],
    'c':['v1', 'v2', 'v3', 'v4', 'v8']
}
df = pd.DataFrame(dict)
print(df)
print(type(df))
print(df.info())
print(df.head(2))
print(df.tail(3))
print(df.columns.values)
print(df.index.values)
print(df.shape)