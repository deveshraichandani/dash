import dash
from dash import html,dcc,Input,Output

app = dash.Dash()

crash_free = 0

app.layout = html.Div([
    dcc.Interval(id = "interval",
                 interval=3000,
                 n_intervals=-1),
    html.Div(id = "outputdiv",
             children=["Hi I'm going to disappear!!"])
])

@app.callback(
    Output(component_id="outputdiv",component_property="children"),
    [Input(component_id="interval",component_property="n_intervals")]
)
def interval_print(interval_number):
    return "Refreshed {} times".format(interval_number)

if __name__ == "__main__":
    app.run_server(debug = True)
