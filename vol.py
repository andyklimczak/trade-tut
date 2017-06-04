import pandas_datareader as pdr
import numpy as np
import datetime
import matplotlib.pyplot as plt

aapl = pdr.get_data_yahoo('AAPL',
                          start=datetime.datetime(2006, 10, 1),
                          end=datetime.datetime(2012, 1, 1))

daily_close = aapl[['Adj Close']]
daily_pct_change = daily_close.pct_change()
daily_pct_change.fillna(0, inplace=True)
print(daily_pct_change)
daily_log_returns = np.log(daily_close.pct_change() + 1)
print(daily_log_returns)

min_periods = 75

vol = daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods)
vol.plot(figsize=(10, 8))
plt.show()
