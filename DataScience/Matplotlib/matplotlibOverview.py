import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('Canada.xlsx', sheet_name='Canada by Citizenship',
                   skiprows=range(20), skipfooter=2)
# print(mpl.__version__)
# print(plt.style.available)
#preproccess data
df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis= 1, inplace=True)
df.rename(columns = {'OdName': 'Country', 'AreaName': 'Continent', 'RegName' : 'Region'}, inplace=True)
df.columns = list(map(str, df.columns))
df.set_index('Country', inplace=True)
df['Total'] = df.sum(axis= 1)
years = list(map(str, range(1980, 2014)))
print(df.head(4))
# haiti = df.loc['Haiti', years]
# print(haiti.head())
# haiti.plot()
# haiti.index = haiti.index.map(int)
# haiti.plot(kind = 'line')
# plt.title("This is title")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.text(1000, 2000, "Pham Line Pot")
#plt.show()
df_CI = df.loc[['China', 'India'], years]
df_CI = df_CI.transpose()
print(df_CI.head(4))
df_CI.index = df_CI.index.map(int)
df_CI.plot(kind = 'line')
plt.title("This is title")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()