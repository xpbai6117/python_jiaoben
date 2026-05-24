# coding:utf-8
# @Author:xb
# @Time: 2024/6/13 9:59
# @File:jj.py
import random
import pandas as pd

# 定义数据
data = []
for i in range(100):
    feature1 = random.uniform(1, 10)
    feature2 = random.uniform(2, 11)
    feature3 = random.uniform(3, 12)
    label = random.randint(0, 1)
    data.append({'Feature 1': feature1, 'Feature 2': feature2, 'Feature 3': feature3, 'label': label})

# 创建DataFrame
df = pd.DataFrame(data)

# 将DataFrame保存到Excel文件中
df.to_excel('D:/product.xlsx', index=False)
