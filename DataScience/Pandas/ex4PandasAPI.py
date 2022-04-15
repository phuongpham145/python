import pandas as pd
from nba_api.stats.static import teams
t = teams.get_teams()
print(len(t))
print(t[0])
def oneDict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key: [] for key in keys}
    for _dict in list_dict:
        for key, value in _dict.items():
            out_dict[key].append(value)
    return out_dict
oneDiction = oneDict(t)
df = pd.DataFrame(oneDiction)
print(df.head(4))
print(df.info)
print(df.columns.values)
print(df['nickname'])
temp = df[df['nickname'] == 'Warriors']
print(temp)

