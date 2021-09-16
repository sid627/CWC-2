import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from datetime import datetime
import plotly.graph_objects as go


with open('Stock List.json') as f:
    data = json.load(f)

close=[]
ope=[]
high=[]
low=[]
dates=[]

#just done for first stock.
#can also do it for all stocks by looping it through.

close.append(data[0]['close'])
close.append(data[0]['uClose'])
close.append(data[0]['fClose'])

ope.append(data[0]['open'])
ope.append(data[0]['uOpen'])
ope.append(data[0]['fOpen'])


high.append(data[0]['high'])
high.append(data[0]['uHigh'])
high.append(data[0]['fHigh'])


low.append(data[0]['low'])
low.append(data[0]['uLow'])
low.append(data[0]['fLow'])

    
dates.append(datetime.strptime(data[0]['date'], '%Y-%m-%d'))

fig = go.Figure(data=[go.Ohlc(x=dates,
                          open=ope, high=high,
                          low=low, close=close)])
fig.show()
