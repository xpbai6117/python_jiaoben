# coding:utf-8
# @Author:xb
# @Time: 2024/3/8 18:33
# @File:get_scp2_scrap.py
import requests
import re

url = 'https://spa2.scrape.center/api/movie/?limit=10&offset=0&token=NTI0NTllMTYxMDhlNzJhYzc4MDc4MzQwNjBjZmFmZGIwYTdiMjE4ZSwxNzA5ODkzODEx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/105',
    'Referer' : 'https://spa2.scrape.center/page/1'
}
respose = requests.get(url=url,headers=headers)
print(respose) #<Response [401]>被反爬了