# coding:utf-8
# @Author:xb
# @Time: 2024/5/15 9:17
# @File:scikit——learn.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
data = load_iris()
x = data.data
y = data.ta
# print(data,type(data))
train_x,test_x,train_y,text_y = train_test_split(x,y,test_size=50,random_state=0)