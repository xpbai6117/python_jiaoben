# coding:utf-8
# @Author:xb
# @Time: 2024/3/27 10:26
# @File:tianmao.py
import requests
url = "https://h5api.m.tmall.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/?jsv=2.6.3&appKey=12574478&t=1711506652150&sign=12796db887b0c66adf4b4235972a027b&api=mtop.relationrecommend.WirelessRecommend.recommend&v=2.0&timeout=10000&type=jsonp&dataType=jsonp&callback=mtopjsonp9&data=%7B%22appId%22%3A%2240282%22%2C%22params%22%3A%22%7B%5C%22floorId%5C%22%3A73133%2C%5C%22count%5C%22%3A7%7D%22%7D"
html = requests.get(url)
print(html.text)
