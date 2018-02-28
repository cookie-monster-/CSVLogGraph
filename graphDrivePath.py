import plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import numpy as np
import pandas as pd

read = pd.read_csv('DriveLog.csv')
df = read[read.driveMode == 'PATH_FOLLOWING']
startPoint = read.shape[0] - df.shape[0]
startTime = df.ix[startPoint, 'sysTime']
xaxis=(df['sysTime']-startTime)*10E-10 #should be 10E-9 but that makes our time 10x too long?????
layout = Layout(title='DriveLog.csv graph', plot_bgcolor='rgb(230, 230,230)')#,height=1500,width=1500)

def data(arg):
	return Scatter(x=xaxis, y=df[arg], mode='lines', name=arg)

#position data
leftPathPos = data('leftPathPos')
leftEncoder = data('leftEncoder')
rightPathPos = data('rightPathPos')
rightEncoder = data('rightEncoder')

#velocity data
leftPathVel = data('leftPathVel')
leftEncoderVel = data('leftEncoderVel')
rightPathVel = data('rightPathVel')
rightEncoderVel = data('rightEncoderVel')

#heading data
pathHdg = data('pathHdg')
gyroYaw = data('gyroYaw')

#set up which data should be graphed together
pos = Figure(data=[leftPathPos, leftEncoder, rightPathPos, rightEncoder], layout=layout)
vel = Figure(data=[leftPathVel, leftEncoderVel, rightPathVel, rightEncoderVel], layout=layout)
hdg = Figure(data=[pathHdg, gyroYaw], layout=layout)

#graph data
py.offline.plot(pos,filename="pos.html")
py.offline.plot(vel,filename="vel.html")
py.offline.plot(hdg,filename="hdg.html")
