import dash
from dash import dcc
from dash import html
from dash import Input,Output

app = dash.Dash()

app.layout = html.Div([
                        dcc.Input(id='inpId',
                                  value="Initial Text",
                                  type= "text",
                                  style=dict(width = "10rem",
                                             height = "5rem",
                                             fontSize = "2rem")),
                        html.Div(id="my-div",
                                 children = ["Hello\t","Yo"],
                                 style={"border" : "2px solid grey"})
])

@app.callback(
        Output(component_id="my-div",component_property="children"),
        Input(component_id="inpId",component_property='value')
)
def update_output_div(input_val):
    return "Text Entered is : {}".format(input_val)

if __name__ == "__main__":
    app.run_server(debug = True)