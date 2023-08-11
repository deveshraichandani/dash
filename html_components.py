import dash
from dash import html

app = dash.Dash()
app.layout = html.Div(children = ["This is outermost div",
                                  html.Div(id="div2",children=["Hello inner division 1"],
                                           style= {'color' : 'blue','textAlign' : 'center', 'border' : '2px solid' }),
                                  html.Div(id="div3",children=["Hello inner div 2"],
                                           style= {'color' : 'green', 'border' : '2px solid',"fontSize" : '1.5rem' })],
                                  style={"color" : "red",
                                         'border' : '3px dashed red '})

if __name__ == '__main__':
    app.run_server(debug = True)


