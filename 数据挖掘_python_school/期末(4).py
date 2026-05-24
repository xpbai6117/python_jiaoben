# coding:utf-8
# @Author:xb
# @Time: 2024/6/13 9:49
# @File:期末(4).py
import pandas as pd
from sklearn.model_selection import train_test_split

# 读取数据集
df = pd.read_excel('D:/product.xlsx')

# 按照2:8比例划分训练集和测试集
train_data, test_data, train_labels, test_labels = train_test_split(df, df.pop('label'), test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeClassifier

# 使用ID3决策树算法构建分类模型
model = DecisionTreeClassifier(criterion='entropy')
model.fit(train_data, train_labels)

from sklearn.metrics import accuracy_score, precision_score, recall_score

# 使用准确率、精确率、召回率等指标评估模型性能
train_predictions = model.predict(train_data)
train_accuracy = accuracy_score(train_labels, train_predictions)
train_precision = precision_score(train_labels, train_predictions, average='weighted')
train_recall = recall_score(train_labels, train_predictions, average='weighted')

test_predictions = model.predict(test_data)
test_accuracy = accuracy_score(test_labels, test_predictions)
test_precision = precision_score(test_labels, test_predictions, average='weighted')
test_recall = recall_score(test_labels, test_predictions, average='weighted')

print("训练集准确率：", train_accuracy)
print("训练集精确率：", train_precision)
print("训练集召回率：", train_recall)
print("\n测试集准确率：", test_accuracy)
print("测试集精确率：", test_precision)
print("测试集召回率：", test_recall)

print("测试集预测标签：", test_predictions)