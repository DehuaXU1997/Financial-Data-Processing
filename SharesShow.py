# -*- coding = utf-8 -*-
# @Time : 2021/6/20 11:18
# @Author : Dehua XU
# @File : gupiaoShow.py
# @software : PyCharm

# 股票的收盘价格趋势图

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.figsize'] = (15,6)

import tushare as ts
ts.set_token('c08c36d7c8e88d0eb52d893d201af3a8e7856559821e6f04bd1224cc')
# 初始化pro接口
pro = ts.pro_api()


df = pro.daily(ts_code='000002.sz', start_date='20090101', end_date='20210619')

# 将数据的每一列表示什么列出来
print(df.dtypes)

# df.to_csv('万科A股价数据。xls', index=False)
# df.set_index('trade_date', inplace=True)
print(df)

# 转换时间戳格式
from datetime import datetime
df['trade_date'] = df['trade_date'].apply(lambda x:datetime.strptime(x, '%Y%m%d'))

plt.plot(df['trade_date'],df['close'],label='万科A股收盘价格',color='black',linewidth=2)
plt.legend(loc='upper left')
plt.show()



