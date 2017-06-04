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

monthly = aapl.resample('BM').apply(lambda x: x[-1])
monthly.pct_change()
quarter = aapl.resample("4M").mean()
print(quarter.pct_change())
print(daily_pct_change.describe())
cum_daily_return = (1 + daily_pct_change).cumprod()
cum_monthly_return = cum_daily_return.resample("M").mean()
cum_monthly_return.plot(figsize=(12, 8))
plt.show()
