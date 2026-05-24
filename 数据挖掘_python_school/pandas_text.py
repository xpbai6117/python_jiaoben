# coding:utf-8
# @Author:xb
# @Time: 2024/3/13 8:29
# @File:pandas_text.py
import pandas as pd
# x = pd.Series([1,3,5,7])
#index标签内容可以指定
# x = pd.Series([1,3,5,7],index=['a','b','c','d'])
#每一列的名称作为字典的键，形成的Dataftame列的Series作为字典的值
# data = {'a':[1,2,3,4],'b':[5,6,7,8]}
# x = pd.DataFrame(data)
data = {'a':[1,2,3,4],'b':[5,6,7,8]}
x = pd.DataFrame(data,columns=['b','a'])
print(x)
