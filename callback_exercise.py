import dash
from dash import Input,Output
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div([
    html.Div([dcc.RangeSlider(id = "rangeSlider",min = -5, max = 5,step=1,value = [-5,5])],style={
                                                                                                  'width' : '100%'}),
    html.Div(id = "answer")
])

@app.callback(
    Output(component_id="answer",component_property="children"),
    Input(component_id="rangeSlider",component_property="value")
)
def output_mult(value_array):
    return value_array[0] * value_array[1]

if __name__ == '__main__':
    app.run_server(debug = True, port = 8051)