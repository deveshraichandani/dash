import dash
from dash import html,dcc,Input,Output
import requests

app = dash.Dash()

app.layout = html.Div([
    html.Div([html.Iframe(src="https://www.flightradar24.com",
                          height=500,width=1200)]),
    
    html.Div([
        html.H4(id = "count_text",
                children=["Active flights worldwide"]),
        dcc.Interval(id = "interval_component",
                     interval=6000,
                     n_intervals=0)
    ])
])

a = []
ba = []
def up():
    return ba