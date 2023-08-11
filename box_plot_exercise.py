import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

df = pd.read_csv("data/abalone.csv")

y1 = np.random.choice(df["rings"],200,replace="False")
y2 = np.random.choice(df["rings"],150,replace="False")

data = [go.Box(y = y1, name = "Sample 1"),
        go.Box(y = y2, name = "Sample2")]

layout = go.Layout(title = "Comparison of two samples", title_x = 0.5,
                   yaxis = dict(title = "Ring Size"))

fig = go.Figure(data= data , layout= layout)
pyo.plot(fig,filename="box_plot_exercise.html")
