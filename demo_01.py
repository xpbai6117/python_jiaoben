# coding:utf-8
# @Author:xb
# @Time: 2024/2/22 15:01
# @File:demo_01.py
# from urllib import request,parse
# import ssl
# context = ssl._create_unverified_context()
# url = 'https://www.csdn.net//action?url=https%3A%2F%2Fwww.csdn.net%2F&pvid=677a035a321d49df85e62177edde1d9e&ref=https%3A%2F%2Fwww.csdn.net%2F&referrer=https%3A%2F%2Fwww.csdn.net%2F&v=3.3.1-saas.2&av=3.3.1-saas.2&did=10_17839453660-1651716788053-686335&uid=m0_65014202&sid=87b567061a154da3bfaae66b7b22a4e4&__s=1708595802422&id=hWg-u0rE5b8&key=Z1Tu5hoKbGw&token=568934913a6343de840a781ca5eaba4b&sh=1080&sw=1920&ps=0&__r=1708596319763'
# headers = {
#     #假装自己是浏览器
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/105'
# }
# dict = {
#     'url':'https://www.csdn.net/',
#                   'pvid': '677a035a321d49df85e62177edde1d9e',
# 'ref':'https://www.csdn.net/',
#               'referrer':'https://www.csdn.net/',
#                                  'v':'3.3.1-saas.2',
# 'av':'3.3.1-saas.2',
# 'did':'10_17839453660-1651716788053-686335',
# 'uid':'m0_65014202',
# 'sid':'87b567061a154da3bfaae66b7b22a4e4',
# '__s':'1708595802422',
# 'id':'hWg-u0rE5b8',
# 'key':'Z1Tu5hoKbGw',
# 'token':'568934913a6343de840a781ca5eaba4b',
# 'sh':'1080',
# 'sw':'1920',
# 'ps':'0',
# '__r':'1708596319763',
# }
# data = bytes(parse.urlencode(dict),'utf-8')
#
# req = request.Request(url,data=data,headers=headers,method='POST')
#
# response = request.urlopen(req,context=context)
# print(response.read().decode('utf-8'))

import urllib.parse
import urllib.request
import ssl

def build_post_data(params):
    """构建 POST 数据字符串"""
    query_string = urllib.parse.urlencode(params)
    encoded_query_string = query_string.encode('utf-8')
    return encoded_query_string

def fetch_page(url, headers, data):
    """获取网页内容"""
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    response = urllib.request.urlopen(req, context=context)
    html = response.read().decode('utf-8')
    return html

if __name__ == '__main__':
    base_url = 'https://www.csdn.net/action'
    params = {
        'url': 'https://www.csdn.net/',
        'pvid': '677a035a321d49df85e62177edde1d9e',
        'ref': 'https://www.csdn.net/',
        'referrer': 'https://www.csdn.net/',
        'v': '3.3.1-saas.2',
        'av': '3.3.1-saas.2',
        'did': '10_17839453660-1651716788053-686335',
        'uid': 'm0_65014202',
        'sid': '87b567061a154da3bfaae66b7b22a4e4',
        '__s': '1708595802422',
        'id': 'hWg-u0rE5b8',
        'key': 'Z1Tu5hoKbGw',
        'token': '568934913a6343de840a781ca5eaba4b',
        'sh': '1080',
        'sw': '1920',
        'ps': '0',
        '__r': '1708596319763',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    data = build_post_data(params)
    full_url = f'{base_url}?{urllib.parse.urlencode(params)}'
    html = fetch_page(full_url, headers, data)
    print(html)
