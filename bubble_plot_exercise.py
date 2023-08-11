import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/mpg.csv")

data = [go.Scatter(x = df["model_year"],
                   y = df["acceleration"],
                   text = df["name"],
                   mode = "markers",
                   marker = dict(
                      size = (df["displacement"]/10),
                      
                      color = df["displacement"],
                      showscale = True, 
                      colorbar=dict(title='Displacement')                    
                                )         
                    )
         ]

layout = go.Layout(title="Bubble chart exercise",
                   xaxis=dict(
                       title = "Year of Model"
                   ),
                   yaxis={"title" : "acceleration"})

fig = go.Figure(data = data, layout= layout)

pyo.plot(fig,filename = "bubble_exercise.html")

