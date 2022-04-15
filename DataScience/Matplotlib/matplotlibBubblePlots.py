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
df_t = df[years].transpose()
df_t.index = map(int, df_t.index)
df_t.index.name = 'year'
df_t.reset_index(inplace=True)
df_t.head()
norm_Brazil = (df_t['Brazil'] - df_t['Brazil'].min()) / \
    (df_t['Brazil'].max() - df_t['Brazil'].min())
norm_Argentina = (df_t['Argentina'] - df_t['Argentina'].min()) / \
    (df_t['Argentina'].max() - df_t['Argentina'].min())
ax0 = df_t.plot(kind='scatter', x='year', y='Brazil', figsize=(
    14, 8), alpha=0.5, color='green', s=norm_Brazil * 2000 + 10, xlim=(1975, 2015))
ax1 = df_t.plot(kind='scatter', x='year', y='Argentina', alpha=0.5,
                color='blue', s=norm_Argentina * 2000 + 10, ax=ax0)
ax0.set_ylabel('Y')
ax0.set_title('This is title')
ax0.legend(['Brazil', 'Argentina'], loc='upper left', fontsize='x-large')
plt.show()
