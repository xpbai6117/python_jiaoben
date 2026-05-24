# coding:utf-8
# @Author:xb
# @Time: 2024/3/29 15:27
# @File:get_video_test.py
url = 'https://v26-web.douyinvod.com/1e93cf17973dfa327a95bc2d5a43a098/66068232/video/tos/cn/tos-cn-ve-15/ocKvGly0TCFIAAL7bBlE7vsVK5BfASehIoEGIe/?a=6383&ch=11&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1963&bt=1963&cs=0&ds=6&ft=bvTKJbQQqUUDfd8Zmo0OqY8hFgpiBD9NUjKJghrk1N0P3-I&mime_type=video_mp4&qs=1&rc=ZzU1NGc3ZztlZDtkODllZEBpMzV5bXA5cjUzbzMzNGkzM0BhXjQxYjViNjAxLTRhYi01YSNzMmtyMmRjXm1gLS1kLTBzcw%3D%3D&btag=e00038000&cquery=100o&dy_q=1711697598&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20240329153317A6184B7EF929431347D5'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60'}

import requests

response = requests.get(url=url,headers=headers)
with open('video\\'+'荒野求生'+'.mp4',mode='wb') as f:
    f.write(response.content)

