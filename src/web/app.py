from dash import Dash, html, dcc


app = Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}



app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Weather recognition service',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='this weather recognition service will help you automate weather recognition. \n Don\'t want to look at window? Just use this app!', style={
        'textAlign': 'center',
        'color': colors['text']
    }
    ),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'color': colors['text']
        },
        # Allow multiple files to be uploaded
        multiple=True)
])

if __name__ == '__main__':
    app.run_server(debug=True)