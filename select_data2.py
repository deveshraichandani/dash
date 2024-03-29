import dash
from dash import dcc 
from dash import html 
from dash import Input,Output
import numpy as np
from plotly import graph_objs as go
import pandas as pd

np.random.seed(10)

#arrays needed for dataframe
x1 = np.linspace(0.1,5,50)
x2 = np.linspace(5.1,10,50)
y = np.random.randint(0,50,50)

df1 = pd.DataFrame({"x" : x1, 'y' : y})
df2 = pd.DataFrame({"x" : x1, 'y' : y})
df3 = pd.DataFrame({"x" : x2, "y" : y})

df = pd.concat([df1,df2,df3])

app = dash.Dash()

app.layout = html.Div([
    html.Div([
        dcc.Graph(id="plot",
            figure = {
            'data' : [go.Scatter(x=df['x'],
                                y=df['y'],
                                mode = "markers")],
            'layout' : go.Layout(title="Scatter Plot")                    
        }
        
        )
    ],style={'width' : '30%', 'display' : 'inline-block'}
    ),
    html.Div([
        html.H1(id="density",style={"paddingTop" : 34,})
        ],
        style={"width" : '30%',
               "display" : "inline-block",
               "verticalAlign" : "top"}
        )
])


@app.callback(
    Output(component_id="density",component_property="children"),
    Input(component_id="plot",component_property="selectedData")
)
def find_density(selectedData):
  if selectedData == None:
    return dash.no_update

  # Calculate density
  pts = len(selectedData["points"])
  rng_or_lp = list(selectedData.keys())
  rng_or_lp.remove("points")
  max_x = max(selectedData[rng_or_lp[0]]["x"])
  min_x = min(selectedData[rng_or_lp[0]]["x"])
  max_y = max(selectedData[rng_or_lp[0]]["y"])
  min_y = min(selectedData[rng_or_lp[0]]["y"])
  area = (max_x - min_x) * (max_y - min_y)
  d = pts / area
  return f"Density = {d:.2f}"

if __name__ == '__main__':
  app.run_server(debug = True)
