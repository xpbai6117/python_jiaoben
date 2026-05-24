# coding:utf-8
# @Author:xb
# @Time: 2024/3/10 20:59
# @File:get_yemuvip_of_interface.py
import urllib
from pprint import pprint
from selenium import webdriver
import requests

url = 'https://www.yemu.xyz/?url=http://v.qq.com/x/cover/8kw2uo89elwb7as/v0030gvdd5b.html'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
respose = requests.get(url, headers=headers)

pprint(respose.text)


