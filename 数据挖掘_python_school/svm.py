# coding:utf-8
# @Author:xb
# @Time: 2024/5/15 9:35
# @File:svm.py
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


data = load_iris()
x = data.data
y = data.target
# print(data,type(data))
train_x,test_x,train_y,text_y = train_test_split(x,y,test_size=50,random_state=0)
svm_model = SVC()
svm_model.fit(train_x,train_y)

pred1 = svm_model.predict(train_x)
acc = accuracy_score(train_y,pred1)
print('%.4f'%acc)

pred2 = svm_model.predict(train_x)
acc = accuracy_score(train_y,pred2)
print('%.4f'%acc)

gb_modle = GaussianNB()
gb_modle.fit()


from sklearn.neural_network import MLPRegressor
from sklearn.metrics import accuracy_score

mlp = MLPRegressor(hidden_layer_sizes=(300,),max_iter=1000,random_state=1)
mlp.fit(train_x,train_y)

mlped1 = mlp.predict(train_x)
mlppaccu1 = accuracy_score(train_y,mlped1)

print(mlppaccu1)
mlped2 = mlp.predict(test_x)

mlpauu = accuracy_score(mlped2)
print(mlpauu)

from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
svm_mode  = SVC()
svm_mode.fit(train_x,train_y)





















