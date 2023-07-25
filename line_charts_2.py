import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/nst-est2017-alldata.csv')
print(df.head())