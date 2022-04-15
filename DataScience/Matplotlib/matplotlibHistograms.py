import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.core.reshape.reshape import stack
mpl.style.use('ggplot')
df = pd.read_excel('Canada.xlsx', "Canada by Citizenship",
                   skiprows=range(20), skipfooter=2)
print(df.head(4))
df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
df.rename(columns={'OdName': 'Country',
          'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
df.columns = list(map(str, df.columns))
df.set_index('Country', inplace=True)
df['Total'] = df.sum(axis=1)
years = list(map(str, range(1980, 2014)))
df.sort_values(['Total'], ascending=False, inplace=True)
df['2013'].head()
count, bin_adges = np.histogram(df['2013'])
print(count)
print(bin_adges)
#df['2013'].plot(kind = 'hist', figsize = (8, 5))
df_t = df.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
#df_t.plot(kind='hist', figsize=(10, 6))
df_t.plot(kind='hist', figsize=(10, 6), bins=15, alpha=0.75,
          xticks=bin_adges, color=['coral', 'darkslateblue', 'mediumseagreen'])
plt.title("This is title")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
