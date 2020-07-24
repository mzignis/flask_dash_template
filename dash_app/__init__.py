import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output

from dash_app.navbar import navbar
from flask_app import create_flask_app
from flask_login import current_user
from dash_app.layouts import index_layout, page1_layout, page2_layout, error_404_layout, create_index_layout
# import dash.callbacks

flask_app = create_flask_app()
dash_app = Dash(__name__, server=flask_app, url_base_pathname='/dash/', external_stylesheets=[dbc.themes.BOOTSTRAP])

dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@dash_app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dash/':
        return create_index_layout(str(current_user))
    elif pathname == '/dash/page1':
        return page1_layout
    elif pathname == '/dash/page2':
        return page2_layout
    elif pathname == '/dash/logout':
        return dcc.Location(id='logout-location', href='/logout', refresh=True)
    else:
        return error_404_layout
