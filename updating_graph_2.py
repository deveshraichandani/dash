import dash as d3js
from dash import dcc, html, Input,Output
import pandas as pd 
from numpy import random
import plotly.graph_objs as go 

#range function of layout

df = pd.read_csv('data/mpg.csv')

df["year"] = random.randint(-4,5,len(df["model_year"])) * 0.1 + df["model_year"]

app = d3js.Dash()

app.layout = html.Div([
    html.Div([dcc.Graph(id = "scatterPlot",
              figure= {
                  'data' : [go.Scatter(x = df["year"] + 1900,
                                       y = df["mpg"],
                                       mode = 'markers',
                                       text = df["name"],
                                       hoverinfo='text + x + y')],

                  'layout' : go.Layout(title="MPG data",
                                       xaxis=dict(
                                           title = "Model Year ->"
                                       ),
                                       yaxis=dict(
                                           title = 'Miles per Gallon ->'
                                       )) 
              })], style= {'width' : '50%', 'display' : "inline-block"}),

    html.Div([
        dcc.Graph(id = "mpg_line",
                  figure={
                      'data' : [go.Scatter(x=[0,1],
                                           y=[0,1],
                                           mode="lines"),
                                           ],
                      'layout' : go.Layout(title="Hover over any point on graph",
                                           margin = {"l" : 0},
                                           xaxis={'visible' : False},
                                           yaxis={'visible' : False})  
                  })
    ],style={'width':'30%','height' : '30%',"display" : "inline-block"}) 
])

@app.callback(
    Output(component_id="mpg_line", component_property="figure"),
    Input(component_id="scatterPlot", component_property="hoverData")
)
def updateLine(hoverData):
    if hoverData is None:
        return d3js.no_update
    vehicle_index = hoverData['points'][0]["pointIndex"]

    figure = {"data" : [go.Scatter(x=[0,1],
                                   y=[0,60/df.iloc[vehicle_index]["acceleration"]],
                                   mode="lines")],
              'layout' : go.Layout(title=df.iloc[vehicle_index]["name"] + "'s acceleration is " + str(df.iloc[vehicle_index]['acceleration']),
                                   margin={'l' : 0},
                                   height=300,
                                   xaxis={'visible' : False},
                                   yaxis={'visible' : False,
                                          'range' : [0,60/df['acceleration'].min()]}
                                   )
             }

    return figure

# 60/df.iloc[vehicle_index]["acceleration"] -> this is the time(sec) taken to reach to 0-60 mph 




    

if __name__ =='__main__':
    app.run_server(debug = True) 
