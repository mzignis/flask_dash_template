import dash_bootstrap_components as dbc
import dash_html_components as html

from dash_app.navbar import navbar


def create_index_layout(username):
    return html.Div([
        navbar,
        dbc.Container([
            html.Br(),
            html.H1(f'Hello {username}!')
        ]),
    ])


index_layout = html.Div([
    navbar,
    dbc.Container([
        html.Br(),
        html.H1(f'Hello World!')
    ]),
])


page1_layout = html.Div([
    navbar,
    dbc.Container([
        html.Br(),
        html.H1('Page 1')
    ]),
])


page2_layout = html.Div([
    navbar,
    dbc.Container([
        html.Br(),
        html.H1('Page 2')
    ]),
])


error_404_layout = html.Div([
    html.Center(
        html.Div([
            html.H1('404'),
            html.H3('Page not found'),
            html.P('The requested URL was not found on the server.'),
            html.P('If you entered the URL manually please check your spelling and try again.'),

        ], style={'margin-top': '25vh', 'margin-left': '10vw', 'margin-right': '10vw'})
    ),
])
