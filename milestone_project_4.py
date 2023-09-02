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

                html.Div([html.H3("Enter a stock symbol",style={'paddingRight' : '30px'}),
                          dcc.Input(id = "stockPicker",
                            value="TSLA",
                            style={'fontSize' : '25px', 'width' : 75})],

                        style={"display":'inline-block','verticalAlign' : 'top'}), 

                html.Div([html.H3("Select any stock : "),
                          dcc.DatePickerRange(
                              id = "datePicker",
                              min_date_allowed=datetime(2015,1,1),
                              max_date_allowed=datetime.today(),
                              start_date=datetime(2022,2,4),
                              end_date=datetime(2023,2,5)
                          )],style={'display':'inline-block'}),            

                dcc.Graph(id = "lineGraph",
                          figure={
                              'data' : [go.Scatter(
                                  x =  [0,1,5],
                                  y =  [4,2,6])
                                  ],
                                  
                              'layout' : go.Layout(title="Graph")
                          })

    ])


@app.callback(
    Output(component_id="lineGraph",component_property="figure"),
    [Input(component_id="stockPicker",component_property="value"),
     Input(component_id="datePicker",component_property="start_date"),
     Input(component_id="datePicker",component_property="end_date")
    ]
)
def update_graph(inputValue,start_date,end_date):
    try:
        start = datetime.strptime(start_date[:10],"%Y-%d-%m")
        end = datetime.strptime(end_date[:10],"%Y-%d-%m")
        
        df = web.DataReader(inputValue,'iex',start,end,api_key = 'pk_7043bd6b931949f49fead7e39b17e03e')

        figure={
            'data' : [go.Scatter(
                x =  df.index,
                y =  df['close'])
                ],
                
            'layout' : go.Layout(title=inputValue)
            
        }    
       
        return figure

    except Exception :
        return Exception



if __name__ == '__main__':
    app.run_server(debug = True)
