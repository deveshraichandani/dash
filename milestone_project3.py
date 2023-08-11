import dash 
from dash import html
from dash import dcc
from dash import Input,Output
import plotly.graph_objs as go
import pandas as pd
import pandas_datareader.data as web
from datetime import datetime

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


@app.callback(
    Output(component_id="lineGraph",component_property="figure"),
    Input(component_id="stockPicker",component_property="value")
)
def update_graph(inputVal):
    try:
        start = datetime(2017,1,1)
        end = datetime(2017,12,31)
        df = web.DataReader(inputVal,'iex',start,end,api_key = 'pk_7043bd6b931949f49fead7e39b17e03e')

        figure={
            'data' : [go.Scatter(
                x =  df.index,
                y =  df['close'])
                ],
                
            'layout' : go.Layout(title=inputVal)
            
        }    
       
        return figure

    except Exception :
        return dash.no_update



if __name__ == '__main__':
    app.run_server(debug = True)
