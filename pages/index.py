import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import pandas as pd

from app import app

all_servants = pd.read_csv('csvs/all_servants.csv')
names = set(all_servants['Name'])

options = [{'label': name, 'value': name} for name in names]

# https://dash.plotly.com/dash-core-components/dropdown

column1 = dbc.Col(
    [
        dcc.Dropdown(id='servant-selector', placeholder='Search for your Servant'),
        html.Button(id='submit-servant-button', n_clicks=0, children='Select'),
        # HIdden Div
        html.Div(id='servant-storage', style={'display': 'none'}, children=[])
    ]
)

column2 = dbc.Col(
    [
        html.Div(id='servant-display')
    ]
)

@app.callback(
    Output('servant-selector', 'options'),
    [Input('servant-selector', 'search_value')],
)
def update_options(search_value):
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value in o['label']]


@app.callback(
    Output('servant-storage', 'children'),
    [Input('submit-servant-button', 'n_clicks')],
    [State('servant-selector', 'value'),
     State('servant-storage', 'children')]
)
def append_selected_servant(n_clicks, servant, storage):
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

layout = dbc.Row([column1, column2])
