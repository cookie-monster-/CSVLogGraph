import plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import numpy as np
import pandas as pd

df = pd.read_csv('DriveLog.csv')
xaxis=df['sysTime']*10E-9
layout = Layout(title='DriveLog.csv graph', plot_bgcolor='rgb(230, 230,230)')#,height=1500,width=1500)

#position data
leftPathPos = Scatter(x=xaxis, y=df['leftPathPos'], mode='lines', name='leftPathPos')
leftEncoder = Scatter(x=xaxis, y=df['leftEncoder'], mode='lines', name='leftEncoder')
rightPathPos = Scatter(x=xaxis, y=df['rightPathPos'], mode='lines', name='rightPathPos')
rightEncoder = Scatter(x=xaxis, y=df['rightEncoder'], mode='lines', name='rightEncoder')

#velocity data
leftPathVel = Scatter(x=xaxis, y=df['leftPathVel'], mode='lines', name='leftPathVel')
leftEncoderVel = Scatter(x=xaxis, y=df['leftEncoderVel'], mode='lines', name='leftEncoderVel')
rightPathVel = Scatter(x=xaxis, y=df['rightPathVel'], mode='lines', name='rightPathVel')
rightEncoderVel = Scatter(x=xaxis, y=df['rightEncoderVel'], mode='lines', name='rightEncoderVel')

#heading data
pathHdg = Scatter(x=xaxis, y=df['pathHdg'], mode='lines', name='pathHdg')
gyroYaw = Scatter(x=xaxis, y=df['gyroYaw'], mode='lines', name='gyroYaw')

#set up which data should be graphed together
pos = Figure(data=[leftPathPos, leftEncoder, rightPathPos, rightEncoder], layout=layout)
vel = Figure(data=[leftPathVel, leftEncoderVel, rightPathVel, rightEncoderVel], layout=layout)
hdg = Figure(data=[pathHdg, gyroYaw], layout=layout)

#graph data
py.offline.plot(pos,filename="pos.html")
py.offline.plot(vel,filename="vel.html")
py.offline.plot(hdg,filename="hdg.html")