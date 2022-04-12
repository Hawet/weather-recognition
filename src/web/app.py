from dash import Dash, html, dcc
from params import get_weather_by_key, get_model_result, base64_pil
from dash.dependencies import Input, Output, State
from PIL import Image
import re
import io

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
            'height': '450px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '0px',
            'textAlign': 'center',
            'margin': '0px',
            'color': colors['text']
        },
        # Allow multiple files to be uploaded
        multiple=False),
        html.Div(
                    id='output-data-upload',
                    children=html.Div(
                                        children ='Here will be the result',
                                        style={
                                                'textAlign': 'center',
                                                'color': colors['text'],
                                                'height': '200px',
                                                'width': '100%',
                                                'fontSize': '25px'
                                                }
                                        ),
                    style={
                        'textAlign': 'center',
                        'color': colors['background']
                    }
        )
])

@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(contents, filename, last_modified):
    """
    Ingesting Input file into model for prediction
    """
    if contents is not None:
        # base 64 decode contents
        #print((contents))        
        image = Image.open(base64_pil(contents))
        image.save('test.jpg', 'JPEG')


if __name__ == '__main__':
    app.run_server(debug=True)