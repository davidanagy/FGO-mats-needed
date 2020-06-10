import pandas as pd
from servants_mats import materials


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


def calculate_mats(df, mats):
    mat_cols = df.columns.tolist()
    for col in ['Name', 'Material', 'Priority']:
        mat_cols.remove(col)
    priority_3_cols = ['Asc2', 'Asc3', 'Asc4', 'AscMax']
    priority_2_cols = priority_3_cols.copy()
    for i in range(2, 7):
        priority_2_cols.append(f'Skl{i}')
    mats_df = pd.DataFrame(columns=['Have', 'Need', 'Want'])
    for i in range(len(df)):
        need_amount = 0
        want_amount = 0
        name = df.loc[i, 'Name']
        mat = df.loc[i, 'Material']
        pri = df.loc[i, 'Priority']

        for col in mat_cols:
            if pri == 1:
                need_amount += df.loc[i, col]
            elif pri == 2:
                if col in priority_2_cols:
                    need_amount += df.loc[i, col]
                else:
                    want_amount += df.loc[i, col]
            elif pri == 3:
                if col in priority_3_cols:
                    need_amount += df.loc[i, col]
                else:
                    want_amount += df.loc[i, col]
            else:
                want_amount += df.loc[i, col]

        if mat in mats_df.index:
            mats_df.loc[mat, 'Need'] += need_amount
            mats_df.loc[mat, 'Want'] += want_amount
        else:
            mats_df.loc[mat, 'Need'] = need_amount
            mats_df.loc[mat, 'Want'] = want_amount
            mats_df = mats_df.fillna(0)

    for mat in mats:
        mats_df.loc[mat.name, 'Have'] = mat.amount

    mats_df['Need_Diff'] = mats_df['Need'] - mats_df['Have']
    mats_df['Want_Diff'] = mats_df['Want'] - mats_df['Have']

    mats_df = mats_df.astype('int32')

    mats_df = mats_df.reset_index()
    mats_df = mats_df.rename(columns={'index': 'Material'})

    mats_df = mats_df.sort_values(by='Need_Diff', ascending=False)

    return mats_df


# mats_df = pd.DataFrame(columns=['Have', 'Need', 'Want', 'Need_Diff', 'Want_Diff'])
# for servant in servants:
#     csv_name = servant[0].lower().replace(' ', '-')
#     csv_path = f'./my_servant_data/{csv_name}.csv'
#     df = pd.read_csv(csv_path, index_col=0)
#     mats_df = add_to_mats_df(mats_df, df, servant[3])
df = pd.read_csv('./my_servant_data/all_servants.csv')
mats_df = calculate_mats(df, materials)
mats_df.to_csv('./mats_needed.csv', index=None)
