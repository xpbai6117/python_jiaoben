# coding:utf-8
# @Author:xb
# @Time: 2024/3/6 22:27
# @File:get_bilibili_video.py
# 1.明确采集网站，及数据内容 url = 'https://www.bilibili.com/video/BV1dy421q7ri/'
#   视频画面和视频音频
# 2.技术步骤：
#         1.打开开发者工具 F12
#         2.刷新网页
#         3.搜索bilibili用:.m4s的来源地址：网页源代码 1455618377-1-30280.m4s  再在找响应内容是视频源码的，不是那种乱码
#         它包含视频和音频，video和audio  他们的网址是Basurl
#
# 3.代码实现步骤：
#         1.发送请求
#         2.获取数据
#         3.解析数据
#         4.保存数据
"""
    'r'：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    'w'：以写入方式打开文件。如果文件已存在，则将其覆盖。如果文件不存在，则创建新文件。
    'a'：以附加方式打开文件。文件的指针将会放在文件的末尾。如果文件不存在，则创建新文件。
    'rb'：以二进制格式打开文件用于只读。
    'wb'：以二进制格式打开文件用于写入。
    'ab'：以二进制格式打开文件用于追加。
"""
import requests
import re
import json
import pprint

headers = {
    #常用于检测是否登录
    'Cookie':'buvid3=B8CAB4A3-E3D9-565F-0415-2D54686DEE0325024infoc; b_nut=1703054825; CURRENT_FNVAL=4048; _uuid=BC7910EFC-1F10C-B618-15D4-534443E6D62227403infoc; buvid4=5C775A03-CB57-3D8C-E18A-1A3A3AA474F126733-023122006-TrWzV6HRzu%2FbAH%2FmMCOpBhZIgcRs3dXBZZS5TAdHObDNJHmC1Rk9ceEfeCnPw0u%2B; buvid_fp=8b41a07525f89dc8aba4b243e8741100; rpdid=0zbfVGWPhH|1PQfzArV|kFh|3w1RfQmf; enable_web_push=DISABLE; FEED_LIVE_VERSION=V_FAVOR_WATCH_LATER; header_theme_version=CLOSE; home_feed_column=5; browser_resolution=1920-957; sid=7k8gwjrr; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDk5MDg3MTksImlhdCI6MTcwOTY0OTQ1OSwicGx0IjotMX0.uXst1iZV96uRcYm79vFZi339DawKsJJerVKlIhSUjkY; bili_ticket_expires=1709908659; bmg_af_switch=1; bmg_src_def_domain=i1.hdslb.com; PVID=1; b_lsid=1B2B65B4_18E13E2DA27',
    #防盗链 告诉地址 从哪里来的
    'Referer':'https://www.bilibili.com/v/popular/rank/all',
    #请求浏览器基本信息
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',

}
#请求链接
url = 'https://www.bilibili.com/video/BV1E44y1B7J5/'
#1.发送请求
respones = requests.get(url=url,headers=headers)
#2.获取数据
html = respones.text
#3.解析视频，提取视频标题，用正则表达式
# title = re.findall('<h1 title="(.*?)" class="video-title" data-v-4f1c0915>',html)[0]
# #如果标题有widows不合法的字符 再自动创建mp3和mp4文件会报错  这条代码是把不合法的字符都去掉的
# title = re.sub(r'[^\w.-]+', '', title)
# title = re.sub('[\\//:*?"<>|]', '', title)
#4.提取信息内容
video_info = re.findall('<script>window.__playinfo__=(.*?)</script>',html)[0]
# vinfo = respose.json()['vinfo']
# #把json字符串转成数据字典类型
json_data = json.loads(video_info)

print(video_info)
# print(json_data)
pprint.pprint(json_data)
# print(title)
print(type(json_data))
print(type(video_info))
#字典取值 先取音频
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
# #字典取值 取视频
video_url = json_data['data']['dash']['video'][0]['baseUrl']
#
# print(title)
# print(audio_url)
# print(video_url)
# #现在可以下载音频和视频之后就是用另外软件把音频和  还有如果是403说明没有防盗链
#
#
# #现在获取视频/音频的二进制
audio_content = requests.get(url=audio_url,headers=headers).content
video_content = requests.get(url=video_url,headers=headers).content

with open('video\\'+'jj'+'.mp3',mode='wb') as audio:
    audio.write(audio_content)
with open('video\\'+'jj'+'.mp4',mode='wb') as video:
    video.write(video_content)




    