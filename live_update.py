import dash
from dash import html, dcc, Input, Output
import requests

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Iframe(src="https://www.flightradar24.com/29.32,71.42/6", height=500, width=1200)
    ]),
    
    html.Div([
        html.H4(id="count_text", children=["Active flights worldwide"]),
        dcc.Interval(id="interval_component", interval=60000, n_intervals=0)
    ])
])

@app.callback(
    Output("count_text", "children"),
    Input("interval_component", "n_intervals")
)
def update_layout(n):
    try:
        url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
        res = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
})
        res.raise_for_status()  # Raise an exception for non-2xx responses
        data = res.json()
        counter = sum(data["stats"]["total"].values())
        return f"Active flights worldwide: {counter}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run_server(debug=True)
