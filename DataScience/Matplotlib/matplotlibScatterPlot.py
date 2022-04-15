import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
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
# df_tot = pd.DataFrame(df[years].sum(axis=0))
# df_tot.index = map(int , df_tot.index)
# df_tot.reset_index(inplace=True)
# df_tot.columns = ['year', 'total']
# #Ke duong mumpy
# x = df_tot['year']
# y = df_tot['total']
# fit = np.polyfit(x, y, deg = 1)
# #
# df_tot.plot(kind='scatter', x= 'year', y= 'total', figsize=(10, 6), color = 'darkblue')
# plt.title('Total Immigration to Canada')
# plt.xlabel('Years')
# plt.ylabel('Number of Immigration')
# plt.plot(x , fit[0] * x + fit[1], color = 'red')
# plt.annotate('y = {0:.0f} x +  {1:.0f}'.format(fit[0], fit[1]), xy = (2000, 150000))
# plt.show()
df_countries = df.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
df_total = pd.DataFrame(df_countries.sum(axis=1))
df_total.reset_index(inplace=True)
df_total.columns = ['year', 'total']
df_total['year'] = df_total['year'].astype(int)
df_total.plot(kind='scatter', x = 'year' ,y = 'total', figsize = (10, 6), color = 'darkblue')
plt.title('This is title')
plt.xlabel("year")
plt.ylabel("total")
plt.show()