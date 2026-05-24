# coding:utf-8
# @Author:xb
# @Time: 2024/3/12 21:24
# @File:get_tencent_vip_video.py
import requests
from pprint import pprint
from DrissionPage import ChromiumPage
#虾米接口+视频地址
url = 'https://jx.xmflv.com/?url='
#https://v.qq.com/x/cover/mzc00200v91asqh/i0048i8nzei.html

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/105'
}

driver = ChromiumPage()
video_url = input('请输入电影的url：')
driver.get(url+video_url)


