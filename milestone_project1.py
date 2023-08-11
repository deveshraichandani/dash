import dash 
from dash import html
from dash import dcc
from dash import Input,Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

app.layout = html.Div([
                html.H1("Stock Ticker Dashboard"),
                html.H3("Select a stock symbol"),
                dcc.Input(id = "stockPicker",
                          value="TSLA"),

                dcc.Graph(id = "lineGraph",
                          figure={
                              'data' : [go.Scatter(
                                  x =  [0,1,2],
                                  y =  [4,2,6])
                                  ],
                                  
                              'layout' : go.Layout(title="graph")
                          })

    ])



if __name__ == '__main__':
    app.run_server(debug = True)
