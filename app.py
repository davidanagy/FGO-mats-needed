import dash
import dash_bootstrap_components as dbc
# from flask_caching import Cache


external_stylesheets = [
    dbc.themes.CERULEAN, # Bootswatch theme
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css', # for social media icons
]

meta_tags=[
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
app.config.suppress_callback_exceptions = True
app.title = 'FGO Mats Needed' # appears in browser title bar
server = app.server

# https://dash.plotly.com/sharing-data-between-callbacks PART 4
# cache = Cache(app.server, config={
#     'CACHE_TYPE': 'filesystem',
#     'CACHE_DIR': 'cache-directory',
#     'CACHE_THRESHOLD': 200
# })
