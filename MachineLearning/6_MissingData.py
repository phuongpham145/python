import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
data = pd.read_csv('missingData6.csv', header=None)
print(data)
X = data.values
imp = SimpleImputer(missing_values= np.nan, strategy='mean') # lay trung binh
imp.fit(X)
result = imp.transform(X)
print(result)