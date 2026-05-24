# coding:utf-8
# @Author:xb
# @Time: 2024/4/3 8:15
# @File:butful.py
import bs4
from bs4 import BeautifulSoup
import requests
re = requests.get('https://www.baidu.com')
re.encoding = 'utf-8'
res = re.text
# print(re.text)
soup = BeautifulSoup(res,'html.parser')
# print(soup)
print(soup.title.string)