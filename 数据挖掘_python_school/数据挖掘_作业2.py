# coding:utf-8
# @Author:xb
# @Time: 2024/4/11 9:05
# @File:数据挖掘_作业2.py
import re

# user_name = input("请输入姓名：")
# # user_password = input("请输入密码：")
# # user_tel = input("请输入电话：")
#
# if re.match('(\w+)',user_name) is None:
#     print("姓名错误")
import requests
url = 'https://www.maoyan.com/films'
headers = {
    'Cookie': 'uuid_n_v=v1; uuid=32E539B0F7A211EE819FC935B2C3306BA53BAC4EC02346BFBF82506BE8AB0264; _csrf=186609be3453bc65e3b65cd204e3666ff521649591c0a1a2421f08725cdd0006; _lxsdk_cuid=18ecac15259ba-034531f8effee-2c29204a-1fa400-18ecac1525ac8; _lxsdk=32E539B0F7A211EE819FC935B2C3306BA53BAC4EC02346BFBF82506BE8AB0264; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1712798651; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1712801411; __mta=217964073.1712798652386.1712801112789.1712801411112.9; _lxsdk_s=18ecac1525b-e21-f9-35%7C%7C18'
,'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/105'}

response = requests.get(url=url,headers=headers)
# print(response.text)
title = re.findall('<span class="name ">(.*?)</span>',response.text)[0]
print(title)

file_type = re.findall('<span class="hover-tag">类型:</span>.*(.*?).*</div><div class="movie-hover-title"',response.text)[0]
if file_type:
    file_type = file_type[0]
    print(file_type)
else:
    print("No match found")
# integer = re.findall('<span class="score channel-detail-orange"><i class="integer">(.*?)</i><i ',response.text)[1]
# fraction = re.findall('class="fraction">(.*?)</i></span>',response.text)[1]











