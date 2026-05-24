# coding:utf-8
# @Author:xb
# @Time: 2024/3/9 15:24
# @File:get_huamaobizhi_jpg.py
import re

import requests
from tqdm import tqdm

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}
for url_page in range(1,10):
    url = f'https://huamaobizhi.com/pictures/?category=377&page={url_page}&orientation=0&order_by=0&time_range=0&size=0&purity=0&remember_filter=1&lang=zh-CN'
    response = requests.get(url=url,headers=headers)
    jpgs = re.findall('''v-lazy="'(.*?)'">''',response.text)
    titles = re.findall('class="preview" title="(.*?)">',response.text)

    # print(jpgs)
    # print(titles[2])
    i=0
    for jpg_url in tqdm(jpgs):
        jpg_data = requests.get(url=jpg_url,headers=headers).content
        title = re.sub(r'[^\w.-]+', '', titles[i])
        with open('video\\image\\'+title+'.jpg',mode='wb')as f:
            f.write(jpg_data)
            i+=1