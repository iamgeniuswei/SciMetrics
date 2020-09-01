#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 19:41
# @Author  : Geniuswei
# @Email   : iamgeniuswei@sina.com
# @File    : fund.py
# @Desc    :

import pandas as pd

file = 'F:\\002-测试数据\\fund\\zz500.xlsx'

prices = []

csv_file = pd.read_excel(file)
max_rows = csv_file.shape[0]
for index in range(0, max_rows):
    print(csv_file.iloc[index].values[1])
    prices.append(csv_file.iloc[index].values[1])

src_fund = 0
every_fund = 1000
count = 0
for price in prices[0:200:1]:
    count += every_fund / price
    src_fund += every_fund
print('总份额： {}'.format(count))

last_value = prices[0] * count
print('当前价格：{}'.format(prices[0]))
print('原始投资：{}'.format(src_fund))
print('最后价值：{}'.format(last_value))
print('收益率：{}'.format((last_value-src_fund)/src_fund))