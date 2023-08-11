import dash
from dash import dcc # dash core components
from dash import html # html components

app = dash.Dash()

colors = dict(background = '#111111', text = '#7fdbff')

app.layout = html.Div(children=[
    html.H1("Hello yo Dash!!!",style={"textAlign" : "center",
                                      'color' : colors['text']}),
       
    dcc.Graph (id="Example Graph",
               figure = {'data' : 
                        [{'x' : [1,2,3] ,'y' : [4,2,3],'type' : 'bar', 'name' : 'N.Delhi'},
                         {'x' : [1,2,3] ,'y' : [2,4,1],'type' : 'bar', 'name' : 'N.York'}
                        ],
                         "layout": 
                         {'title' : "Bar plots!!!",
                          'plot_bgcolor' : colors['background'],
                          'font' : {'color' : colors['text'] },
                          'paper_bgcolor': colors['background']

                          }

                        }
                )
], style= {'backgroundColor' : '#111112',}) 
if __name__ == '__main__':
    app.run_server()





