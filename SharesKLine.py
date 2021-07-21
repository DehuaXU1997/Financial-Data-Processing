# -*- coding = utf-8 -*-
# @Time : 2021/6/20 15:52
# @Author : Dehua XU
# @File : gupiaoKLine.py
# @software : PyCharm

import pandas as pd
import tushare as ts
ts.set_token('c08c36d7c8e88d0eb52d893d201af3a8e7856559821e6f04bd1224cc')
# 初始化pro接口
pro = ts.pro_api()
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.figsize'] = (20, 8)
import mplfinance as mpf
import seaborn as sns
# 激活seaborn，激活图表美化库
sns.set()

# 利用tusahre库获得万科A股价数据
df = pro.daily(ts_code='000002.sz', start_date='202105022', end_date='20210620')

# 对每一列数据格式需要
times = pd.DatetimeIndex(df['trade_date'].values)
df_data = pd.DataFrame({'Open': df['open'].values,
                        'Date': times,
                        'Close': df['close'].values,
                        'High': df['high'].values,
                        'Low': df['low'].values,
                        'Volume': df['vol'].values})

print(times)
df_data.set_index('Date', inplace=True)
print(df_data)

df_data = df_data[:: -1]

print(df_data)

mc = mpf.make_marketcolors(up='r', down='g')
s = mpf.make_mpf_style(marketcolors=mc, mavcolors=['#4f8a8b', '#fbd46d', '#87556f'],gridaxis='both', gridstyle='-',)
mpf.plot(df_data, type='candle', volume=True, show_nontrading=True, figratio=(20,8), mav=(3,6,9), style=s, title='000002.sz K Lines, Author:xdh', ylabel='OHLC Candles', ylabel_lower='Shares\nTraded Volume')
