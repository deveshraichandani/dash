import dash as d3js
from dash import dcc
from dash import html
from dash import Input,Output
import pandas as pd
import base64

df = pd.read_csv("data/wheels.csv")

app = d3js.Dash()

def encode_img(image_file):
    encoded = base64.b64encode(open(image_file,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())


app.layout = html.Div([
                        dcc.RadioItems(id = "wheels",
                                       options=[{'label' : i,
                                                 'value' : i} for i in [1,2,3]],
                                       value=1,
                                       inline=True),
                        html.Div(id = 'wheel-output'),

                        html.Hr(),

                        dcc.RadioItems(id = "color",
                                       options=[{'label' : i,
                                                 'value' : i} for i in ['red','blue','yellow']],
                                       value='blue',
                                       inline=True), 
                        html.Div(id = 'color-output'),

                       html.Img(id = "image",height=300,style={'display': 'block',
                                                               'margin-left': 'auto',
                                                               'margin-right': 'auto',
                                                               'padding' : 100
                                                               })    
                        
                    
], style={'fontFamily' : "Jokerman", 'fontSize' : 20,'textAlign':'center'})

@app.callback(
        Output(component_id="wheel-output",component_property="children"),
        Input(component_id="wheels",component_property="value")
)
def output_no(no_of_wheels):
    if(no_of_wheels == 1):
        return "You selected {} wheel".format(no_of_wheels)
    return "You selected {} wheels".format(no_of_wheels)


@app.callback(
        Output(component_id="color-output",component_property="children"),
        Input(component_id="color",component_property="value")
)
def output_col(color):
    return "You selected {} color".format(color)


@app.callback(
    Output(component_id="image",component_property="src"),
    [Input(component_id="wheels",component_property="value"),
     Input(component_id="color",component_property="value")]
)
def output_image(no_of_wheels,color_of_vehicle):
    path = "data/images/"
    return encode_img(path + df[(df["wheels"] == no_of_wheels) & (df["color"] == color_of_vehicle)]['image'].values[0])


# print(df[(df['wheels'] == 1) & (df['color'] == 'blue')]['image'])

if __name__ == '__main__':
    app.run_server(debug = True,port = 8051)