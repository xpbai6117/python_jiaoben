# coding:utf-8
# @Author:xb
# @Time: 2024/3/13 10:07
# @File:python_列表.py

# li = ['alex','eric','rain']
# print(len(li))
# li.append('xx')
# print(li)
# li.insert(2,'sa')
# print(li)
# li[2] = 'sb'
# print(li)
# li.remove(li[2])
# print(li)
# li.reverse()
# print(li)
from random import random
import random
li = []
for i in range(40):
    li.append(random.randint(50, 100))
print(li)
li.sort(reverse=True)
print(li)












