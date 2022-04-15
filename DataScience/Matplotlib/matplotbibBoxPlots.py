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
# df_japan = df.loc[['Japan'], years].transpose()
# df_japan.plot(kind= 'box', figsize=(8, 6))
# plt.title("This is title")
# plt.ylabel("Y")
# plt.show()
df_CI = df.loc[['China', 'India'], years].transpose()
df_CI.plot(kind= 'box', figsize=(10, 7), color= 'blue', vert = False)
# plt.title("This is title")
# plt.ylabel("Y")
# plt.show()
#create figure
fig = plt.figure()
ax0 = fig.add_subplot(1, 2, 1)
ax1 = fig.add_subplot(1, 2, 2)
#subplot 1: Box plot
df_CI.plot(kind= 'box', color='blue', vert= False, figsize=(20, 6), ax = ax0)
ax0.set_title('Box Plots of Immigrants form China and India (1980 - 2013)')
ax0.set_xlabel('Number of Immigrants')
ax0.set_ylabel('Countries')
#subplot 2: Line plots
df_CI.plot(kind= 'line', figsize=(20, 6), ax = ax1)
ax1.set_title('Line Plots of Immigrants form China and India (1980 - 2013)')
ax1.set_xlabel('Number of Immigrants')
ax1.set_ylabel('Years')
plt.show()