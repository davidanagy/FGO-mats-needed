from bs4 import BeautifulSoup
import pandas as pd
import requests
#from servants import servants


def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def fill_table(df, rows, asc):
    mat_class = 'paragraph paragraph--type--required-materials paragraph--view-mode--default'
    amount_class = 'field field--name-field-number-of-materials field--type-integer field--label-hidden field__item'
    
    for row in rows:
        if asc:
            number = row.find('td', attrs={'class': 'ascension-header'}).contents[0]
            col_name = f'Asc{number}'
        else:
            number = row.find('td', {'class': 'Skill-header'}).contents[0][-1]
            if number == '0':
                number = '10'
            col_name = f'Skl{number}'

        mat_divs = row.find_all('div', attrs={'class': mat_class})
        for div in mat_divs:
            item = div['data-item']
            try:
                amount = int(div.find('div', attrs={'class': amount_class})['content'])
                if not asc:
                    amount *= 3
                df.loc[item, col_name] = amount
            except:
                continue


def scrape_servant_data(name):
    asc_names = [f'Asc{i}' for i in range(2,5)]
    asc_names.append('AscMax')
    skill_names = [f'Skl{i}' for i in range(2,11)]
    cols = asc_names + skill_names
    df = pd.DataFrame(columns=cols)
    
    url_name = name[0]
    full_name = name[1]
    soup = get_soup(f'https://gamepress.gg/grandorder/servant/{url_name}')
    ascension_table = soup.find('table', attrs={'id': 'ascension-materials-table'})
    ascension_rows = ascension_table.find_all('tr', attrs={'class': 'ascension-row'})
    fill_table(df, ascension_rows, asc=True)
    skill_table = soup.find('table', {'id': 'Skill-materials-table'})
    skill_rows = skill_table.find_all('tr', {'class': 'skill-row'})
    fill_table(df, skill_rows, asc=False)
    df = df.fillna(0)
    df = df.reset_index()
    df = df.rename(columns={'index': 'Material'})
    name_col = [full_name] * len(df)
    df.insert(0, 'Name', name_col)
    
    return df


def get_servant_names():
    soup = get_soup('https://gamepress.gg/grandorder/servants')
    servant_table = soup.find('table', attrs={'id': 'servants-new-list'})
    servant_rows = servant_table.find_all('tr', attrs={'class': 'servants-new-row'})
    servants = []
    for row in servant_rows:
        td = row.find('td', attrs={'class': 'servant-title'})
        span = td.find('span', attrs={'class': 'servant-list-title'})
        url = span.a.get('href')
        url_name = url.split('/servant/')[1]
        full_name = span.get_text().strip('\n').strip('\n').strip()
        servants.append((url_name, full_name))
        #print(f'URL: {url}; url_name: {url_name}; full_name: {full_name}')
    return servants


servant_names = get_servant_names()
df = pd.DataFrame()
for name in servant_names:
    try:
        df2 = scrape_servant_data(name)
        #print('SUCCESS:', url_name)
    except:
        print('ERROR:', name)
    df = pd.concat([df, df2])

df = df.reset_index(drop=True)
df.to_csv('./full_servant_data/all_servants.csv', index=None)
