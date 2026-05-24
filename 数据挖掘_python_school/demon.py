# coding:utf-8
# @Author:xb
# @Time: 2024/3/27 8:22
# @File:demon.py
# 编写一个函数demo，通过调用函数传递一个字符串，返回一个元组，其中第一个元素为大写字母个数，第二个为小写字母个数
def demo(s):
    count_uppercase = sum([1 for char in s if char.isupper()])
    count_lowercase = sum([1 for char in s if char.islower()])
    return (count_uppercase, count_lowercase)

# Example usage
s = "Hello World!"
result = demo(s)
print(result)  # Output: (2, 8)