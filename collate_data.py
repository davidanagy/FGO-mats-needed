import pandas as pd
import os
from servants import servants


# def add_to_mats_df(mats_df, df, need_want):
#     df2 = mats_df.copy()
#     for mat in df.index:
#         for col in df.columns:
#             amount = int(df.loc[mat, col])
#             if mat in df2.index:
#                 df2.loc[mat, need_want] += amount
#             else:
#                 df2.loc[mat, need_want] = amount
#                 df2 = df2.fillna(0)
#     return df2

def calculate_mats():
    df = pd.read_csv('./my_servant_data/all_servants.csv')
    mats_df = pd.DataFrame(columns=['Have', 'Need', 'Want', 'Need_Diff', 'Want_Diff'])
    for i in range(len(df)):
        amount = 0
        name = df.iloc[i, 0]
        mat = df.iloc[i, 1]
        for j in range(2, len(df.columns)-2):
            amount += df.iloc[i, j]
        if name in needs:
            need_want = 'Need'
        elif name in wants:
            need_want = 'Want'
        if mat in mats_df.index:
            mats_df.loc[mat, need_want] += amount
        else:
            mats_df.loc[mat, need_want] = amount
            mats_df = mats_df.fillna(0)

    mats_df = mats_df.reset_index()
    mats_df = mats_df.rename(columns={'index': 'Material'})

    return mats_df


# mats_df = pd.DataFrame(columns=['Have', 'Need', 'Want', 'Need_Diff', 'Want_Diff'])
# for servant in servants:
#     csv_name = servant[0].lower().replace(' ', '-')
#     csv_path = f'./my_servant_data/{csv_name}.csv'
#     df = pd.read_csv(csv_path, index_col=0)
#     mats_df = add_to_mats_df(mats_df, df, servant[3])
mats_df = calculate_mats()
mats_df.to_csv('./mats_needed.csv', index=None)
