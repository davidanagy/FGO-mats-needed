import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import os
import pandas as pd
from collections import namedtuple
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State

from app import app
from functions import make_servants_table, calculate_mats


all_servants = pd.read_csv('csvs/all_servants.csv')
names = set(all_servants['Name'])
options = [{'label': name, 'value': name} for name in names]


@app.callback(
    Output('servant-selector', 'options'),
    [Input('servant-selector', 'search_value')],
)
def update_options(search_value):
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value.lower() in o['value'].lower()]


@app.callback(
    [Output('servant-storage', 'data'),
     Output('servant-display', 'children')],
    [Input('submit-servant-button', 'n_clicks')],
    [State('servant-selector', 'value'),
     State('ascension-selector', 'value'),
     State('skill-selector-1', 'value'),
     State('skill-selector-2', 'value'),
     State('skill-selector-3', 'value'),
     State('priority-selector', 'value'),
     State('servant-storage', 'data'),
     State('servant-display', 'children')]
)
def append_selected_servant(n_clicks, name, asc, skl1, skl2, skl3, priority, storage, display):
    if n_clicks == 0:
        return storage, display
    servant = {'name': name, 'ascension': asc, 'skills': [skl1, skl2, skl3], 'priority': priority}
    for servant2 in storage:
        if servant['name'] == servant2['name']:
            storage.remove(servant2)
            for item in display:
                if item['props']['id'] == servant['name']:
                    display.remove(item)
    storage.append(servant)
    pri_dict = {
        1: 'Max everything',
        2: 'Skills to 6/6/6',
        3: "Don't upgrade"
    }
    s = f'{name}: Asc {asc}; Skills {skl1},{skl2},{skl3}; {pri_dict[priority]}'
    for item in display:
        if item['props']['active']:
            print('change active to False')
            item['props']['active'] = False
            print(item)
    new_item = dbc.ListGroupItem(id=servant['name'], children=s, active=True)
    display.append(new_item)
    return storage, display


with open('mat_names.txt') as f:
    mat_names_file = f.read()
mat_names = mat_names_file.split('\n')[:-1]
Servant = namedtuple('Servant', ['name', 'ascension', 'skills', 'priority'])
Material = namedtuple('Material', ['name', 'amount'])

make_final_table_states = [State('servant-storage', 'data')]
for name in mat_names:
    states.append(State(f'have-input-{name}', 'value'))


@app.callback(
    Output('final-table', 'children'),
    [Input('get-final-table', 'n_clicks')],
    make_final_table_states
)
def make_final_table(n_clicks, servant_data, *args):
    mats = []
    for i, name in enumerate(mat_names):
        amount = args[i]
        mat = Material(name, amount)
        mats.append(mat)

    servants_df = make_servants_table(servant_data)
    df = calculate_mats(servants_df, mats)
    cols = df.columns().tolist()

    table_header = [
        html.Thead(html.Tr([html.Th(col) for col in cols]))
    ]

    rows = []
    for i in range(len(df)):
        row = []
        for col in cols:
            row.append(html.Td(df.loc[i, col]))
        rows.append(html.Tr(row))

    table_body = [html.Tbody(rows)]

    return table_header + table_body
    # i = 0
    # while os.path.exists(f'/user_csvs/user-csv-{i}'):
    #     i += 1

    # df.to_csv(f'/user_csvs/user_csv-{i}', index=None)


# @app.callback(
#     Output('servant-display-2', 'children'),
#     [Input('url', 'pathname'),
#      Input('servant-storage', 'data')]
# )
# def display_servants_on_mats_page(pathname, servants):
#     if pathname == '/mats':
#         s = ''
#         for servant in servants:
#             s += f'{servant}; '
#         return s
