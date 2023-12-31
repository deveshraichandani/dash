import dash 
from dash import html
from dash import dcc
from dash import Input,Output,State
import plotly.graph_objs as go
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

                html.Div([html.Button(id = "submitBtn",
                                      n_clicks=0,
                                      children="Submit",
                                      style={"fontSize": 25,"marginLeft" : 30})],style={'display' : "inline-block"}),     

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
    [State(component_id="stockPicker",component_property="value"),
     State(component_id="datePicker",component_property="start_date"),
     State(component_id="datePicker",component_property="end_date")
    ],
    Input(component_id="submitBtn",component_property="n_clicks")
)
def update_graph(inputVal,start_date,end_date,n_clicks):
    try:
        start = datetime.strptime(start_date[:10],"%Y-%m-%d")
        end = datetime.strptime(end_date[:10],"%Y-%m-%d")
        
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
        return Exception



if __name__ == '__main__':
    app.run_server(debug = True)
