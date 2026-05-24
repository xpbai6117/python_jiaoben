# coding:utf-8
# @Author:xb
# @Time: 2024/4/10 10:06
# @File:拉格朗日.py

from scipy.interpolate import lagrange

# x = [1,2,3]
# y = [3,5,7]
# a = lagrange(x,y)
# print(a)
# print(a(4))
#
# x = [0,1,2,3,5,6,7,8,9]
# y = [1,2,3,4,6,7,8,9,10]
# a = lagrange(x,y)
# print(a)
# print(a(4))

import pandas as pd
import xlwt
data = pd.read_excel(r'D:\lagerange.xlsx')
print(data['销量'])
# data['销量'][(data['销量']<400)|(data['销量']>5000)]==None

# def ployinterp(s,n,k=5):
#     y = s.iloc[list(range(n-k,n))+list(range(n+1,n+1+k))]
#     y = y[y.notnull()]
#     return lagrange(y.index,list(y))(n)
# def data_lagrange(data):
#     for i in data.columns:
#         for j in range(len(data)):
#             if(data[i].isnull())[j]:
#                 data.loc[i,j] = ployinterp(data[i],j)
#                 return data
# data_lagrange(data)
# data.to_excel(r'D:\lagerange.xlsx',index=False)


