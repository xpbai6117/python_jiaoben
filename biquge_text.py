# coding:utf-8
# @Author:xb
# @Time: 2024/4/25 9:27
# @File:biquge_text.py
from selenium import webdriver
import requests,re,os,time,shutil,threading,queue
from lxml import etree
import pandas as pd
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
# url = 'https://www.bigee.cc/book/1891/'
url = 'https://www.bigee.cc/book/1891/1.html'
response = requests.get(headers=headers,url=url)
# print(response.text)
#获取了小说每个章节的所以链接地址 /book/1891/1.html
# soup = BeautifulSoup(response.text, 'lxml')
# list = soup.find(class_="listmain").find_all('a')
# for item in list:
#     item_link = item.get('href')
#     print(item_link)

soup = BeautifulSoup(response.text, 'lxml')
noval = soup.find(class_="Readarea ReadAjax_content").text
with open('video\\image\\'+"yushou"+'.txt','w',encoding='utf-8')as f:
    f.write(noval)
print(noval)



