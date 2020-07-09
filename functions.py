from bs4 import BeautifulSoup
import pandas as pd
import requests


def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def scrape_mat_names():
    soup = get_soup('https://gamepress.gg/grandorder/materials')
    tables = soup.find('div', attrs={'class': 'view-content'}).find_all('table')
    skill_gem_table = tables[3]
    mats_table = tables[0]
    asc_mats_table = tables[2]
    mat_names = []
    mats_tables = (skill_gem_table, mats_table, asc_mats_table)
    for table in mats_tables:
        rows = table.find_all('tr')
        for row in rows:
            name = [text for text in row.stripped_strings][0]
            mat_names.append(name.strip('\u200b'))

    return mat_names


def set_mats_data(df, asc_level, skill_levels):
    asc_col_clear = []
    for i in range(2, asc_level+1):
        if i == 5:
            i = 'Max'
        asc_col_clear.append(f'Asc{i}')
    for col in asc_col_clear:
        df[col] = [0] * df.shape[0]
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


def make_servants_table(servants):
    df = pd.read_csv('./csvs/all_servants.csv')
    df_new = pd.DataFrame()
    for servant in servants:
        df2 = df[df['Name'] == servant['name']]
        df2 = df2.reset_index(drop=True)
        # if len(df2) == 0:
        #     print('ERROR:', servant['name'])
        df2 = set_mats_data(df2, servant['ascension'], servant['skills'])
        priority_column = [servant['priority']] * len(df2)
        df2.insert(2, 'Priority', priority_column)
        df_new = pd.concat([df_new, df2])

    return df_new.reset_index(drop=True)


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

    mats_df = mats_df.fillna(0)

    mats_df = mats_df.astype('int32')

    mats_df = mats_df.reset_index()
    mats_df = mats_df.rename(columns={'index': 'Material'})

    mats_df = mats_df.sort_values(by='Need_Diff', ascending=False)
    mats_df = mats_df.reset_index(drop=True)

    return mats_df


def calculate_mats_new(df, mats):
    mat_cols = df.columns.tolist()
    for col in ['Name', 'Material', 'Goals']:
        mat_cols.remove(col)
    df = df.rename(cols={'AscMax': 'Asc5'})
    for i in range(len(df)):
        need_amount = 0
        want_amount = 0
        name = df.loc[i, 'Name']
        mat = df.loc[i, 'Material']
        goals = df.loc[i, 'Goals']
        asc_goal = goals[0]
        skl_goals = goals[1]

        for col in mat_cols:
            if col[0:3] == 'Asc':
                if int(col[3]) <= asc_goal:
                    need_amount += df.loc[i, col]
                else:
                    want_amount += df.loc[i, col]

            elif col[0:3] == 'Skl':
                total = df.loc[i, col]
                per_skill = total // 3
                mult = 0
                for goal in skl_goals:
                    if int(col[3]) <= goal:
                        mult += 1
                want_amount += total - per_skill*mult
                need_amount = total - want_amount
            else:
                print(col)


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

    mats_df = mats_df.fillna(0)

    mats_df = mats_df.astype('int32')

    mats_df = mats_df.reset_index()
    mats_df = mats_df.rename(columns={'index': 'Material'})

    mats_df = mats_df.sort_values(by='Need_Diff', ascending=False)
    mats_df = mats_df.reset_index(drop=True)

    return mats_df


# mat_names = scrape_mat_names()

# with open('mat_names.txt', 'w') as f:
#     for name in mat_names:
#         f.write(name + '\n')
