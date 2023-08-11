import dash
from dash import Input,Output
from dash import html
from dash import dcc
import pandas as pd
import  plotly.graph_objs as go


df = pd.read_csv("data/gapminderDataFiveYear.csv")

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(id = "graph"),
    dcc.Dropdown(id = "Year list",
                 options=[
                     {'label' : str(i) , 'value' : i}
                     for i in df["year"].unique()
                 ],
                 value=df["year"].min())
])


@app.callback(
    Output(component_id="graph",component_property="figure"),
    Input(component_id="Year list", component_property="value") 
)
def update_graph(Selected_Year):
    traces = []
    df_by_year = df[df["year"] == Selected_Year]
    for continent in df_by_year['continent'].unique():
        df_by_continent = df_by_year[df_by_year['continent'] == continent]
        traces.append(go.Scatter(
                                 x = df_by_continent['gdpPercap'],
                                 y = df_by_continent['lifeExp'],
                                 name = continent,
                                 opacity=0.7,
                                 mode="markers",
                                 marker = dict(
                                 size = 15
                                 ),
                                 text = df_by_year['country']
                                )
                        )
        
    return {'data' :traces,'layout': go.Layout(title="My Plot",
                                               xaxis=dict(title = "GDP per Capita", type = "log"),
                                               yaxis={'title' : 'Life Expectancy'})}


if __name__ == '__main__':
    app.run_server(debug = True)