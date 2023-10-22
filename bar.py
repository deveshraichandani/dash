import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("data/2018WinterOlympics.csv")
trace1 = go.Bar(x = df["Name of Coun."],
                y = df["Gold"],
                name = "gold medals",
                marker = {"color" :"#FFD700"})
                
trace2 = go.Bar(x = df["NOC"],
                y = df["Silver"],
                name = "silver medals",
                marker=dict(color = "#B2B9AE"))

trace3 = go.Bar(x = df["NOC"],
                y = df["Bronze"],
                name = "bronze-medals",
                marker={"color" : "#8F6409"})

data = [trace1,trace2,trace3]

layout = go.Layout(title = "Medal Count By Country Name",
                   title_x = 0.5, barmode="stack")

fig = go.Figure(data = data, layout = layout)
pyo.plot(fig,filename="bar_chart.html")