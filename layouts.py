import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State


asc_options = [
    {'label': 'Ascension 1', 'value': 1},
    {'label': 'Ascension 2', 'value': 2},
    {'label': 'Ascension 3', 'value': 3},
    {'label': 'Ascension 4', 'value': 4},
    {'label': 'Ascension MAX', 'value': 5}
]

skl_options = [{'label': f'Level {n}', 'value': n} for n in range(1,11)]

pri_options = [
    {'label': 'Max everything', 'value': 1},
    {'label': 'Max ascend, skills to 6/6/6', 'value': 2},
    {'label': 'Not planning to use', 'value': 3}
]

# https://dash.plotly.com/dash-core-components/dropdown

column1 = dbc.Col(
    [
        dcc.Dropdown(id='servant-selector', placeholder='Search for your Servant'),
        dcc.Dropdown(id='ascension-selector', options=asc_options,
                     placeholder='Select ascension level', searchable=False),
        dcc.Dropdown(id='skill-selector-1', options=skl_options,
                     placeholder='First skill level', searchable=False),
        dcc.Dropdown(id='skill-selector-2', options=skl_options,
                     placeholder='Second skill level', searchable=False),
        dcc.Dropdown(id='skill-selector-3', options=skl_options,
                     placeholder='Third skill level', searchable=False),
        dcc.Dropdown(id='priority-selector', options=pri_options,
                     placeholder='Upgrade priority', searchable=False),
        html.Button(id='submit-servant-button', n_clicks=0, children='Select'),
        dcc.Link(dbc.Button('Click here when finished',
                            id='goto-mats', n_clicks=0, color='primary'),
                 href='/mats')
    ]
)

column2 = dbc.Col(
    [
        dbc.ListGroup(id='servant-display',
                      children=[
                          dbc.ListGroupItem('placeholder', id='placeholder',
                                            style={'display': 'none'}, active=False)
                      ],
        )
    ]
)

index_layout = dbc.Row([column1, column2])

### Mats page layout

with open('mat_names.txt') as f:
    mat_names_file = f.read()
mat_names = mat_names_file.split('\n')[:-1]

table_header = [
    html.Thead(html.Tr([html.Th('Name'), html.Th('Amount')]))
]

table_rows = []
for name in mat_names:
    td1 = html.Td(name)
    td2 = dbc.Input(id=f'have-input-{name}', type='number')
    table_rows.append(html.Tr([td1, td2]))

table_body = [html.Tbody(table_rows)]

table = dbc.Table(table_header + table_body, id='mats-table', bordered=True)

column3 = dbc.Col(
    [
        table,
        dbc.Button('Click here when finished', id='get-final-table', n_clicks=0, color='primary')
    ]
)

mats_layout = column3

### Final table page layout

column4 = dbc.Col(
    [
        dcc.Link(dbc.Button('Get a CSV copy of this table',
                            id='download-mats', n_clicks=0, color='primary'),
                 href='/mats-csv'),
        dbc.Table(id='final-table', bordered=True)
    ]
)

mats_needed_layout = column4

### Mats CSV layout

column5 = dbc.Col([], id='mats-csv-text')

mats_csv_layout = column5
