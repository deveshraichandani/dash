import dash 
from dash import html
from dash import dcc
from dash import Input,Output,State
import plotly.graph_objs as go
import pandas_datareader.data as web
from datetime import datetime
import pandas as pd
import json 

nsdq = pd.read_csv('data/NASDAQcompanylist.csv')
nsdq.set_index('Symbol',inplace=True)
options = []

for symbol in nsdq.index:
    mydict = {}
    mydict['label'] = nsdq.loc[symbol]["Name"] + " " + symbol
    mydict['value'] = symbol
    options.append(mydict)

app = dash.Dash()

app.layout = html.Div(children=[
                html.H1("Stock Ticker Dashboard",style={'textAlign' : 'center',
                                                        'color' : 'blue'}),

                html.Div([html.H3("Enter a stock symbol",style={'paddingRight' : '30px'}),
                          dcc.Dropdown(id = "stockPicker",
                            value=["TSLA"],
                            options=options,
                            multi=True)],

                        style={"display":'inline-block','verticalAlign' : 'top','width' : '30%'}), 

                html.Div([html.H3("Select start and end date : "),
                          dcc.DatePickerRange(
                              id = "datePicker",
                              min_date_allowed=datetime(2015,1,1),
                              max_date_allowed=datetime.today(),
                              start_date=datetime(2022,2,4),
                              end_date=datetime.today()
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

    ],style={'background-color' : 'crimson'})


@app.callback(
    Output(component_id="lineGraph",component_property="figure"),
    [State(component_id="stockPicker",component_property="value"),
     State(component_id="datePicker",component_property="start_date"),
     State(component_id="datePicker",component_property="end_date")
    ],
    Input(component_id="submitBtn",component_property="n_clicks")
)
def update_graph(stockList,start_date,end_date,n_clicks):

    try:

        start = datetime.strptime(start_date[:10],"%Y-%m-%d")
        end = datetime.strptime(end_date[:10],"%Y-%m-%d")
        traces =[]

        for stock in stockList:
            df = web.DataReader(stock,'iex',start,end,api_key = 'pk_7043bd6b931949f49fead7e39b17e03e')
            traces.append(go.Scatter(
                x =  df.index,
                y =  df['close'],
                name=stock)
                )
            
        layout = ""
        count = 0

        for symbol in stockList:
            layout += " , " + symbol 

        layout = layout[2:]          

        figure={
            'data' : traces,
                
            'layout' : go.Layout(title = layout)
            
        }    
       
        return figure

    except Exception :
        return Exception



if __name__ == '__main__':
    app.run_server(debug = True)
