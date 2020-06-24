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
                 href='/mats'),
        # dcc.ConfirmDialogProvider(
        #     children=dcc.Link(
        #         dbc.Button(
        #             'Click here when finished',
        #             color='primary'
        #         ),
        #         href='/mats'
        #     ),
        #     id='goto-mats',
        #     message='Are you finished entering your Servants?'
        # )
    ]
)

column2 = dbc.Col(
    [
        dbc.ListGroup(id='servant-display',
                      children=[
                          dbc.ListGroupItem('placeholder', id='placeholder',
                                            style={'display': 'none'}, active=False)
                      ],
        ),
        dcc.Markdown('Upload a CSV from a previous sesson:'),
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and drop or ',
                html.A('click here to select files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            }
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
        dcc.Link(dbc.Button('Get a CSV copy of your servant data',
                            id='download-servants', n_clicks=0, color='primary'),
                 href='/servants-csv'),
        dbc.Table(id='final-table', bordered=True)
    ]
)

mats_needed_layout = column4

### Mats CSV layout

column5 = dbc.Col(
    [
        html.P(id='mats-csv-text')
    ]
)

mats_csv_layout = column5

### Servants CSV layout

column6 = dbc.Col(
    [
        html.P(id='servants-csv-text')
    ]
)

servants_csv_layout = column6
