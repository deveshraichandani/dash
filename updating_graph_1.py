import dash as d3js
from dash import dcc, html, Input,Output
import pandas as pd 
from numpy import random
import plotly.graph_objs as go 

df = pd.read_csv('data/mpg.csv')

df["year"] = random.randint(-4,5,len(df["model_year"])) * 0.1 + df["model_year"]

app = d3js.Dash()

app.layout = html.Div([
    dcc.Graph(id = "scatterPlot",
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
              }) 
])

if __name__ =='__main__':
    app.run_server(debug = True) 
