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
df_iceland = df.loc['Iceland', years]
# #df_iceland.plot(kind='bar', figsize = (10, 6))
# df_iceland.plot(kind='bar', figsize=(10, 6), rot=90)
# plt.title("This is title")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.annotate('', xy=(32, 70), xytext=(28, 20), xycoords='data', arrowprops=dict(
#     arrowstyle='->', connectionstyle='arc3', color='blue', lw=2))
# plt.annotate('Tang rat nhanh', xy=(28, 30),
#              rotation='72.5', va='bottom', ha='left')
# plt.show()
df.sort_values(['Total'], ascending= True, axis= 0, inplace=True)
df_top15 = df['Total'].tail(15)
df_top15.plot(kind='barh', figsize= (12, 12), color='blue')
for index, value in enumerate(df_top15):
    label = format(int(value), ',')
    plt.annotate(label, xy = (value - 4700, index - 0.01), color = 'white')
plt.show()