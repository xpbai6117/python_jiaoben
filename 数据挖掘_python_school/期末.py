# coding:utf-8
# @Author:xb
# @Time: 2024/6/13 9:03
# @File:期末.py
import numpy as np

# 创建一个长度为10的一维随机数组，元素值范围为0-10
random_array = np.random.randint(0, 11, size=10)
print("原始随机数组:", random_array)

# 对数组进行升序排列
sorted_array = np.sort(random_array)
print("升序排列后的数组:", sorted_array)

# 获取最大值和最小值
max_value = np.max(sorted_array)
min_value = np.min(sorted_array)

print("最大值:", max_value)
print("最小值:", min_value)

