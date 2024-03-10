import dash
from dash import html
from dash import dcc 
from dash import Input,Output
import plotly.graph_objs as go
import pandas as pd
import json
import base64

def encode_image(imgFile):
    encoded  = base64.b64encode(open(imgFile,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

df = pd.read_csv("data/wheels.csv")

app = dash.Dash()

app.layout = html.Div([
                    html.Div([dcc.Graph(id = "graph",
                                        figure={'data' : [go.Scatter(x = df["color"],
                                                                     y = df['wheels'],
                                                                     mode = "markers",
                                                                     dy = 1,
                                                                    marker = {
                                                                        'size' : 14 }
                                                                    )
                                                            ],
                                                'layout' : go.Layout(title="Hello")}
                                        )
                             ],style={'width' : '30%',"float" : 'left'}),
                             
                    html.Div(html.Pre(
                        id = "selection",
                        style={'paddingTop' : 32}),
                    
                    style={'width' : '30%'})
                        
                        ])


@app.callback(
    Output(component_id="selection",component_property="children"),
    Input(component_id="graph",component_property="selectedData")
)
def callback_img(selectedData):
    return json.dumps(selectedData,indent=2)

if __name__ == '__main__':
    app.run_server(debug = True)