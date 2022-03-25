from dash import Dash, html, dcc


app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}



app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)