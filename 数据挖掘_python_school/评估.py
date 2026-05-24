# coding:utf-8
# @Author:xb
# @Time: 2024/4/24 9:17
# @File:评估.py
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import  MultinomialNB
from sklearn import metrics
#划分训练集和测试类
x = np.array([[1,1],[0,1],[0,1],[1,0],[0,1],[1,1],[1,0],[1,1]])
y = np.array([1,1,1,0,0,0,0,0])
x_1 = np.array([[0,0]])

x_train,x_text,y_train,y_text = train_test_split(x,y,train_size=0.2,random_state=16)

gnb = MultinomialNB()

gnb.fit(x_train,y_train)

print(gnb.score(x_train,y_train))

y_pred = gnb.predict(x_1)

print(y_pred)