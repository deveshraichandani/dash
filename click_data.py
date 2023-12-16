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
                                                                        'size' : 16 }
                                                                    )
                                                            ],
                                                'layout' : go.Layout(title="Hello")}
                                        )
                             ],style={'width' : '30%',"float" : 'left','paddingTop' : 35}),
                             
                    html.Div(children=[html.Img(id = "img",src = "children",height=300)],
                    
                    style={'width' : '30%','paddingTop' : 140,"display" : 'flex'})
                        
                        ])


@app.callback(
    Output(component_id="img",component_property="src"),
    Input(component_id="graph",component_property="clickData")
)
def callback_img(clickData):

    if clickData == None:
        # If there is no hover data, return dash.no_update to prevent updating the image
        return dash.no_update
    
    wheels = clickData["points"][0]["y"]
    color = clickData["points"][0]["x"]
    path = "data/images/"
    return encode_image(path + df[(df["wheels"] == wheels)
                            & (df["color"] == color)]['image'].values[0])



if __name__ == '__main__':
    app.run_server(debug = True,port = 8051)