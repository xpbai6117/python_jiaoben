# coding:utf-8
# @Author:xb
# @Time: 2024/6/13 9:27
# @File:期末(3).py
import pandas as pd
from sklearn import preprocessing

# 读取数据集
df = pd.read_excel('D:/principal_component.xls')

# 最小-最大规范化
min_max_scaler = preprocessing.MinMaxScaler()
min_max_scaled = min_max_scaler.fit_transform(df)

# 零-均值规范化
z_score_scaler = preprocessing.StandardScaler()
z_score_scaled = z_score_scaler.fit_transform(df)

# 小数定标规范化
robust_scaler = preprocessing.RobustScaler()
robust_scaled = robust_scaler.fit_transform(df)

print("最小-最大规范化:")
print(min_max_scaled)
print("\n零-均值规范化:")
print(z_score_scaled)
print("\n小数定标规范化:")
print(robust_scaled)
