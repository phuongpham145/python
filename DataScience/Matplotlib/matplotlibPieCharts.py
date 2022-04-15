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
df_continents = df.groupby('Continent', axis=0).sum()
df_continents.head(5)
#df_continents['Total'].plot(kind='pie', figsize=(5, 6), autopct='%1.1f%%', startangle= 90, shadow = True)
colors_list = ['gold', 'yellowgreen', 'lightcoral',
               'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1]
df_continents['Total'].plot(kind='pie', figsize=(5, 6), autopct='%1.1f%%', startangle=90,
                            shadow=True, labels=None, pctdistance=1.12, colors=colors_list, explode=explode_list)
plt.title("Immigration to Canada by Continent [1980 - 2013]")
plt.legend(labels=df_continents.index, loc='upper left')
plt.axis("equal")
plt.show()
