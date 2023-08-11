import dash 
from dash import dcc
from dash import html

app = dash.Dash()
app.layout = html.Div([
                       html.Label("Dropdown"),
                       dcc.Dropdown(options=[{
                           "label" : "New Delhi",
                           "value" : "ND"},
                           {"label" : "Tamil Nadu",
                            "value" : 'TD'}
                       ], value = "ND"),

                       html.Label('Slider'),
                       dcc.Slider(min=0,max = 15,step=0.5,value=7,
                                  marks={i: str(i) for i in range(0,16)}),

                       html.Br(),
                       html.Label("Radio items :"),
                       dcc.RadioItems(options = [{
                           'label' : "Pao Bhaji",
                           'value' : "PB"},
                           {'label' : "Burger",
                            'value' : 'BG'}
                       ], value="BG"

                       )           
                       
                       
                       ])


if __name__ == '__main__':
    app.run_server(debug = True)