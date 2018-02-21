import plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import numpy as np
import pandas as pd

df = pd.read_csv('graphTest.csv')

trace1 = Scatter(
                    x=df['x'], y=df['y=x'], # Data
                    mode='lines', name='y=x' # Additional options
                   )
trace2 = Scatter(x=df['x'], y=df['y=x^2'], mode='lines', name='y=x^2' )
trace3 = Scatter(x=df['x'], y=df['y=x^3'], mode='lines', name='y=x^3' )

layout = Layout(title='Simple Plot from csv data',
                   plot_bgcolor='rgb(230, 230,230)')#,height=1500,width=1500)

fig0 = Figure(data=[trace1, trace2, trace3], layout=layout)
fig1 = Figure(data=[trace2, trace1], layout=layout)

py.offline.plot(fig0,filename="test0.html")
py.offline.plot(fig1,filename="test1.html")

#plotly.offline.plot({
#    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#    "layout": Layout(title="hello world")
#})