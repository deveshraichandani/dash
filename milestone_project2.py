import dash 
from dash import html
from dash import dcc
from dash import Input,Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
                html.H1("Stock Ticker Dashboard"),
                html.H3("Select a stock symbol"),
                dcc.Input(id = "stockPicker",
                          value="TSLA"),

                dcc.Graph(id = "lineGraph",
                          figure={
                              'data' : [go.Scatter(
                                  x =  [0,1,3],
                                  y =  [4,2,6])
                                  ],
                                  
                              'layout' : go.Layout(title="graph")
                          })

    ])


@app.callback(
    Output(component_id="lineGraph",component_property="figure"),
    Input(component_id="stockPicker",component_property="value")
)
def title_callback(inputVal):
    figure={
        'data' : [go.Scatter(
            x =  [0,1,2],
            y =  [4,2,6])
            ],
            
        'layout' : go.Layout(title=inputVal)
        }    
       
    return figure



if __name__ == '__main__':
    app.run_server(debug = True)
