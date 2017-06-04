import pandas_datareader as pdr
import numpy as np
import datetime
import matplotlib.pyplot as plt

aapl = pdr.get_data_yahoo('AAPL',
                          start=datetime.datetime(2006, 10, 1),
                          end=datetime.datetime(2012, 1, 1))

adj_close_px = aapl['Adj Close']
# moving_avg = adj_close_px.rolling(window=40).mean()
aapl['42'] = adj_close_px.rolling(window=40).mean()
aapl['252'] = adj_close_px.rolling(window=252).mean()
aapl[['Adj Close', '42', '252']].plot()
plt.show()
