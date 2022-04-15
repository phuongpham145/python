import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
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
print(df.head(4))
df.sort_values(['Total'], ascending=False, axis=0, inplace=True)
df_top5 = df.head(5)
df_top5 = df_top5[years].transpose()
df_top5.head()
df_top5.index = df_top5.index.map(int)
# df_top5.plot(kind = 'area', alpha=0.75, stacked = False, figsize=(20, 10))
# plt.title('This is title')
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()
ax = df_top5.plot(kind='area', alpha=0.75, stacked=True, figsize=(20, 10))
ax.set_title('This is title')
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()
