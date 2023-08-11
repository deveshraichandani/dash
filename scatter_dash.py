import dash 
from dash import dcc
from dash import html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()
np.random.seed(42)

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100) 
random_x1 = np.random.randint(1,101,100) + 10
random_y1 = np.random.randint(1,101,100) + 5


data = [go.Scatter(x = random_x,y = random_y,mode="markers",opacity = 0.5,
                   marker=dict(size = 10,
                               symbol = "square",
                               line = dict(width = 2))),
        go.Scatter(x = random_x1,y = random_y1,mode="markers",opacity=0.5,
                   marker=dict(size = 10,
                               symbol = "circle",
                               line = dict(width = 2),))]

layout = go.Layout(title="Scatter Dashboard",
                   xaxis={"title" : "random points from 1 to 110 -->"},
                   yaxis={"title" : "random points from 1 to 105 -->"}
                   )                   

app.layout = html.Div([dcc.Graph(id="scatterPlot",
                                 figure={'data' : data,
                                         'layout' : layout })
               ] )

if __name__ == '__main__' :  
    app.run_server(debug = True)