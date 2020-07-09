"""Launch the app"""

# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
# from flask import send_file
import json
import io
import pandas as pd

# Imports from this application
from app import app
import callbacks
from layouts import index_layout, mats_layout, mats_needed_layout, mats_csv_layout, servants_csv_layout

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/navbar

NavbarSimple consists of a 'brand' on the left, to which you can attach a link 
with brand_href, and a number nav items as its children. NavbarSimple will 
collapse on smaller screens, and add a toggle for revealing navigation items.

brand (string, optional): Brand text, to go top left of the navbar.
brand_href (string, optional): Link to attach to brand.
children (a list of or a singular dash component, string or number, optional): The children of this component
color (string, optional): Sets the color of the NavbarSimple. Main options are primary, light and dark, default light. You can also choose one of the other contextual classes provided by Bootstrap (secondary, success, warning, danger, info, white) or any valid CSS color of your choice (e.g. a hex code, a decimal code or a CSS color name)
dark (boolean, optional): Applies the `navbar-dark` class to the NavbarSimple, causing text in the children of the Navbar to use light colors for contrast / visibility.
light (boolean, optional): Applies the `navbar-light` class to the NavbarSimple, causing text in the children of the Navbar to use dark colors for contrast / visibility.
sticky (string, optional): Stick the navbar to the top or the bottom of the viewport, options: top, bottom. With `sticky`, the navbar remains in the viewport when you scroll. By contrast, with `fixed`, the navbar will remain at the top or bottom of the page.
"""

server = app.server

navbar = dbc.NavbarSimple(
    brand="FGO Mats Needed",
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('About', href='/about', className='nav-link')), 
    ],
    sticky='top',
    color='primary', 
    light=False, 
    dark=True
)

footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span('David Nagy', className='mr-2'), 
                    html.A(html.I(className='fas fa-envelope-square mr-1'), href='mailto:davidanagy@gmail.com'), 
                    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/davidanagy/nba-assists-prediction'), 
                    html.A(html.I(className='fab fa-linkedin mr-1'), href='https://www.linkedin.com/in/david-nagy-771a3a71/'), 
                    html.A(html.I(className='fab fa-twitter-square mr-1'), href='https://twitter.com/davidanagyds'), 
                ], 
                className='lead'
            )
        )
    )
)

external_stylesheets = [
    dbc.themes.CERULEAN, # United theme
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css', # for social media icons
]

# For more explanation, see: 
# Plotly Dash User Guide, URL Routing and Multiple Apps
# https://dash.plot.ly/urls

# placeholder_servant = [{'name': 'placeholder', 'ascension': 0,
#                         'skills': [0,0,0], 'priority': 0}]
# placeholder_children = json.dumps(placeholder_servant)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'),
    # Storage in a hidden div
    dcc.Store(id='servant-storage', data=[]),
    dcc.Store(id='final-table-storage'),
    html.Div(id='placeholder', style={'display': 'none'}),
    html.Hr(), 
    footer
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index_layout
    elif pathname == '/mats':
        return mats_layout
    elif pathname == '/mats-needed-table':
        return mats_needed_layout
    elif pathname == '/mats-csv':
        return mats_csv_layout
    elif pathname == '/servants-csv':
        return servants_csv_layout
    else:
        return dcc.Markdown('## Page not found')


# https://community.plotly.com/t/allowing-users-to-download-csv-on-click/5550/3
# https://community.plotly.com/t/where-to-save-temporary-file-for-user-to-download/29177/2
# @server.route('/mats-csv-download')
# def download_csv():
#     print('begin download')
#     storage = app.layout.children[4]
#     print(getattr(storage, 'children'))

#         # df = pd.read_json(table)

#         # proxyIO = io.StringIO()
#         # df.to_csv(proxyIO, index=False, encoding='utf-8')

#         # mem = io.BytesIO()
#         # mem.write(proxyIO.getvalue().encode('utf-8'))
#         # mem.seek(0)

#         # return flask.send_file(
#         #     mem,
#         #     mimetype='text/csv',
#         #     attachment_filename='mats-needed.csv',
#         #     as_attachment=True,
#         #     cache_timeout=0
#         # )


if __name__ == '__main__':
    app.run_server(debug=True)
