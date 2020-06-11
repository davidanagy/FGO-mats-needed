from collections import namedtuple
import dash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import pandas as pd

from app import app


all_servants = pd.read_csv('csvs/all_servants.csv')
names = set(all_servants['Name'])
options = [{'label': name, 'value': name.lower()} for name in names]

Servant = namedtuple('Servant', ['name', 'ascension', 'skills', 'priority'])


@app.callback(
    Output('servant-selector', 'options'),
    [Input('servant-selector', 'search_value')],
)
def update_options(search_value):
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value.lower() in o['value']]


@app.callback(
    Output('servant-storage', 'children'),
    [Input('submit-servant-button', 'n_clicks')],
    [State('servant-selector', 'value'),
     State('ascension-selector', 'value'),
     State('skill-selector-1', 'value'),
     State('skill-selector-2', 'value'),
     State('skill-selector-3', 'value'),
     State('priority-selector', 'value'),
     State('servant-storage', 'children')]
)
def append_selected_servant(n_clicks, name, asc, skl1, skl2, skl3, priority, storage):
    servant = Servant(name, asc, (skl1, skl2, skl3), priority)
    storage.append(servant)
    return storage


@app.callback(
    Output('servant-display', 'children'),
    [Input('servant-storage', 'children')]
)
def display_servants(l):
    s = ''
    for servant in l:
        s += f'{servant}; '
    return s


@app.callback(
    Output('servant-display-2', 'children'),
    [Input('url', 'pathname'),
     Input('servant-storage', 'children')]
)
def display_servants_on_mats_page(pathname, servants):
    if pathname == '/mats':
        s = ''
        for servant in servants:
            s += f'{servant}; '
        return s
