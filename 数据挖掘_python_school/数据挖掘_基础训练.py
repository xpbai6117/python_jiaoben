# coding:utf-8
# @Author:xb
# @Time: 2024/3/28 8:58
# @File:数据挖掘_基础训练.py

from itertools import permutations

# 定义数字列表
digits = [1, 2, 3, 4]

# 生成所有三位数的排列组合
perms = permutations(digits, 3)

# 打印所有三位数
for perm in perms:
    num = int(''.join(map(str, perm)))
    print(num)


# 输入三个整数
num1 = int(input("请输入第一个整数: "))
num2 = int(input("请输入第二个整数: "))
num3 = int(input("请输入第三个整数: "))

# 排序
sorted_nums = sorted([num1, num2, num3])

# 输出结果
print("从小到大排列的结果为:", sorted_nums)




for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print(f'{i} x {j} = {result}')
    print()


