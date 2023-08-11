import dash
from dash import dcc
from dash import html
from dash import Input,Output,State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id="inputNum",value=1,style={"font-size": 25}),

    html.Button(id = "submit-button",
                n_clicks=0,
                children=["Submit"],
                style={"fontSize" : 25}),

    html.H1(id = "outputNum")
])


@app.callback(
        Output(component_id="outputNum",component_property="children"),
        [Input(component_id="submit-button",component_property="n_clicks")],
        State(component_id="inputNum",component_property="value")

        )
def Output_callback(n_clicks,number):
    return ("You submitted : ", number," and submit button was clicked " , n_clicks , " times")


if __name__ == '__main__':
    app.run_server(debug = True)