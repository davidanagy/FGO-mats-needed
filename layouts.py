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

# skl_options = [{'label': f'Level {n}', 'value': n} for n in range(1,11)]

pri_options = [
    {'label': 'Max everything', 'value': 1},
    {'label': 'Max ascend, skills to 6/6/6', 'value': 2},
    {'label': 'Not planning to use', 'value': 3}
]

# https://dash.plotly.com/dash-core-components/dropdown

row1 = dbc.Row(
    [
        dcc.Markdown(
            """
            Welcome to FGO Mats Needed! You can use this app to automatically
            calculate how many materials you'll need to upgrade your Servants
            to the levels you want.

            To start, use the tools on the left to enter the relevant information
            for all your Servants (though you can skip any fully-upgraded Servants,
            since they don't need additional mats anwyway). Alternately, you can
            upload a CSV or Excel file from a previous session (or one suitably
            modified that still keeps the same column format).

            If you make a mistake inputting your Servant's data, just re-input it
            and the old data will be overwritten.
            """
        )
    ]
)

column1 = dbc.Col(
    [
        dcc.Dropdown(id='servant-selector', placeholder='Search for your Servant'),
        dcc.Dropdown(id='ascension-selector', options=asc_options,
                     placeholder='Select ascension level', searchable=False),
        dcc.Markdown("Input Servant's current skill levels:"),
        dcc.Input(id='skill-selector-1', type='number', placeholder='Skill 1',
                  min=1, max=10, step=1),
        dcc.Input(id='skill-selector-2', type='number', placeholder='Skill 2',
                  min=1, max=10, step=1),
        dcc.Input(id='skill-selector-3', type='number', placeholder='Skill 3',
                  min=1, max=10, step=1),
        dcc.Markdown("Input your goal level for each skill:"),
        dcc.Input(id='skill-1-goal', type='number', placeholder='Skill 1',
                  min=1, max=10, step=1),
        dcc.Input(id='skill-2-goal', type='number', placeholder='Skill 2',
                  min=1, max=10, step=1),
        dcc.Input(id='skill-3-goal', type='number', placeholder='Skill 3',
                  min=1, max=10, step=1),
        # dcc.Dropdown(id='skill-selector-1', options=skl_options,
        #              placeholder='First skill level', searchable=False),
        # dcc.Dropdown(id='skill-selector-2', options=skl_options,
        #              placeholder='Second skill level', searchable=False),
        # dcc.Dropdown(id='skill-selector-3', options=skl_options,
        #              placeholder='Third skill level', searchable=False),
        # dcc.Dropdown(id='priority-selector', options=pri_options,
        #              placeholder='Upgrade priority', searchable=False),
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

row2 = dbc.Row([column1, column2])

index_layout = dbc.Col([row1, row2])

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
        dcc.Markdown(
            """
            Now, input the amount of each material you currently have.
            Note that if you leave a field blank, or type something that
            isn't a number, it will count as 0.
            """
        ),
        table,
        dbc.Button('Click here when finished', id='get-final-table', n_clicks=0, color='primary')
    ]
)

mats_layout = column3

### Final table page layout

column4 = dbc.Col(
    [
        dcc.Markdown(
            """
            Click the buttons below to get a CSV copy of the table (so you can
            save it to e.g. Google Drive) or of your Servants data (so you can
            upload it to this app again and skip past the first page).

            Scroll down to the bottom for an explanation of the columns.
            """
        ),
        dcc.Link(dbc.Button('Get a CSV copy of this table',
                            id='download-mats', n_clicks=0, color='primary'),
                 href='/mats-csv'),
        dcc.Link(dbc.Button('Get a CSV copy of your servant data',
                            id='download-servants', n_clicks=0, color='primary'),
                 href='/servants-csv'),
        dbc.Table(id='final-table', bordered=True),
        dcc.Markdown(
            """
            Explanations of columns:

            * "Material": Name of the material

            * "Have": The amount of each material you have, obtained from the previous page

            * "Need": The amount that you need to upgrade all your priority Servants

            * "Want": The amount to fully upgrade all your Servants

            * "Need_Diff": 'Need' minus 'Have'; the table is sorted by this column

            * "Want_Diff": 'Want' minus 'Have'
            """
        )
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
