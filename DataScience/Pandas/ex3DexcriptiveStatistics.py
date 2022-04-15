import pandas as pd
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv(url, names=names)
print(data.head(5))
print(data.info)
print(data.columns.values)
print(data.shape)
print(data.dtypes)
print(data.tail(4))
print(data.index.values)
print(data.describe())
pd.set_option('display.width', 100)
pd.set_option('precision', 3)
print(data.head(5))
print(data.describe())
print(data.groupby('class').size())
print(data.corr(method = 'pearson'))