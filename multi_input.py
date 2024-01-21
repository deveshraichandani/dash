import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas as pd
from dash import Input,Output

df = pd.read_csv("data/mpg.csv")

app = dash.Dash()
#list of columns in df
features = df.columns

app.layout = html.Div([
                html.Div(children=[dcc.Dropdown(id="x_axis",
                    options = [{'label' : i,'value' : i} for i in features],
                    value="mpg"
                )],style={'width' : "48%",
                          'display' : 'inline-block'}),
                html.Div([dcc.Dropdown(id="y_axis",
                    options = [{'label' : i,'value' : i} for i in features],
                    value="displacement"
                )],style={'width' : "48%",
                          'display' : 'inline-block'}),
                dcc.Graph(id = "Graph")
                                     
                    ],style={'padding' : 10}
                    )

@app.callback(
    Output(component_id="Graph",component_property="figure"),
    [Input(component_id="x_axis",component_property="value"),
     Input(component_id="y_axis",component_property="value")]
)
def graph_update(xaxis_name,yaxis_name):
    return {'data' : [go.Scatter(x = df[xaxis_name],
                                 y = df[yaxis_name],
                                 mode="markers",
                                 marker = dict(
                                    size = 9,
                                    opacity=0.3,
                                    line = dict(width = 0.5,
                                                color = 'white')
                                 ),
                                 text = df["name"],
                                 )
                        ],
            'layout' : go.Layout(title = "Dashboard for all Car's MPG",
                                 xaxis = {'title' : xaxis_name},
                                 yaxis = {'title' : yaxis_name}
                                )
            } 

if __name__ == '__main__':
    app.run_server(debug = True)
                                 