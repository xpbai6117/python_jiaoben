# coding:utf-8
# @Author:xb
# @Time: 2024/2/29 16:16
# @File:dangdangT500books.py

import re
import urllib
import parsel;
import requests


def request_dangdang(url):
    try:
        respose=requests.get(url)
        if respose.status_code == 200:
            print("url 解析完成")
            return respose.text

    except requests.RequestException as e:
        print(e)
        return None


def pares_result(html):
    pattern=re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span class="price_n">&yen;(.*?)</span>.*?</li>',re.S)

    items = re.findall(pattern,html)
    selector = parsel.Selector(html)
    select = selector.css()


    print("分析页面代码")
    for item in items :
        yield {
        'range': item[0],
        'iamge': item[1],
        'title': item[2],
        'recommend': item[3],
        'author': item[4],
        'times': item[5],
        'price': item[6]
    }

def main(page):
    url='http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html=request_dangdang(url)
    items=pares_result(html)
    # for item in items:
    #     write_item_to_file(item)
    for item in items:
        print(item)

if __name__ == "__main__":
    main(1)