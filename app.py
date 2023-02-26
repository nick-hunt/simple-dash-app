from dash import Dash, html, dcc

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1('Hello Dash')
])

if __name__ == '__main__':
    app.run_server(debug=True)
