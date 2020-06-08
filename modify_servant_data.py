import pandas as pd
from servants import servants


def set_mats_data(df, asc_level, skill_levels):
    asc_col_clear = []
    for i in range(2, asc_level+1):
        if i == 5:
            i = 'Max'
        asc_col_clear.append(f'Asc{i}')
    for col in asc_col_clear:
        df2[col] = [0] * df.shape[0]
    for i in range(2, 11):
        col_name = f'Skl{i}'
        mult = 0
        for level in skill_levels:
            if i <= level:
                mult += 1
        for j in range(len(df)):
            amount = df.loc[j, col_name]
            subtract = (amount // 3) * mult
            df.loc[j, col_name] = amount - subtract

    return df


df = pd.read_csv('./full_servant_data/all_servants.csv')
df_new = pd.DataFrame()
for servant in servants:
    df2 = df[df['Name'] == servant.name].reset_index(drop=True)
    if len(df2) == 0:
        print('ERROR:', servant.name)
    df2 = set_mats_data(df2, servant.ascension, servant.skills)
    df_new = pd.concat([df_new, df2])

df_new = df_new.reset_index(drop=True)
df_new.to_csv('./my_servant_data/all_servants.csv', index=None)
