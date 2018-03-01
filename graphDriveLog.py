import plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import numpy as np
import pandas as pd

df = pd.read_csv('DriveLog.csv')
xaxis=(df['sysTime']*10E-10) #should be 10E-9 but that makes our time 10x too long?????
layout = Layout(title='DriveLog.csv graph', plot_bgcolor='rgb(230, 230,230)')#,height=1500,width=1500)


def data(arg):
	return Scatter(x=xaxis, y=df[arg], mode='lines', name=arg)
	
def plot_cols(cols,filename):
	cols_data = []
	for head in cols:
		col = data(head)
		cols_data.append(col)
	fig = Figure(data=cols_data,layout=layout)
	py.offline.plot(fig,filename=filename)

hdg = ['gyroYaw','pathHdg']
pos = ['leftEncoder','rightEncoder','leftPathPos','rightPathPos']
vel = ['leftEncoderVel','rightEncoderVel','leftPathVel','rightPathVel']
acc = ['leftPathAcc','rightPathAcc']
motor = ['leftMotorPercent','rightMotorPercent','leftMotorVoltage','rightMotorVoltage','leftMotorCurrent','rightMotorCurrent'
	,'driveStick','turnStick','leftBusVoltage','rightBusVoltage']
misc = ['leftTemp','rightTemp','pathStep0','pathStep1']
	
plot_cols(hdg,'hdg.html')
plot_cols(pos,'pos.html')
plot_cols(vel,'vel.html')
plot_cols(acc,'acc.html')
plot_cols(motor,'motor.html')
plot_cols(misc,'misc.html')