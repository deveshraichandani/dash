import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data/OldFaithful.csv")

data = [go.Scatter(x = df["X"], 
                   y = df["Y"],
                   mode="markers")]

layout = go.Layout(title = "Old Faithful Eruptions Analysis", titlefont=dict(color = "red"),
                xaxis= dict(title = "Duration of current eruption (minutes) -->"),
                yaxis= dict(title = "Time till next eruption (minutes) -->")
)

app = dash.Dash()
app.layout = html.Div([html.H1("Python Dashboard",style={"textAlign" : "center",
                                                         "color" : "darkblue"}),
                       dcc.Graph(id="Old Faithful",
                                 figure={
                                    "data" : data,
                                    "layout" : layout
                                 }) 
                        ])

if __name__ == '__main__':
    app.run_server()