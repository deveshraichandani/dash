import dash
from dash import dcc # dash core components
from dash import html # html components

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1("Hello yo Dash!!!"),
    html.Div(children = ["Dashboard hello there !! how you doin",html.H2("hello bye-bye")]) ,
    html.Div("Dashboard hello there !! how you doin'") ,
    html.Div("Dashboard hello there !! how you doin'") ,
    html.Div("Dashboard hello there !! how you doing'") ,
    dcc.Graph (id="Example Graph",
               figure = {'data' : 
                        [{'x' : [1,2,3] ,'y' : [4,2,3],'type' : 'bar', 'name' : 'N.Delhi'},
                         {'x' : [1,2,3] ,'y' : [2,4,1],'type' : 'bar', 'name' : 'N.York'}],
                         "layout": 
                         {'title' : "Bar plots!!!"}})
]) 
if __name__ == '__main__':
    app.run_server()




