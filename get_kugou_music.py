# coding:utf-8
# @Author:xb
# @Time: 2024/3/21 14:18
# @File:get_kugou_music.py
'''
    音乐的链接
    https://webfs.hw.kugou.com/202403211402/94919b0140319477333f353bc381401e/v2/8909e1809908cd8e3bf6cf85d98b93f0/part/0/960115/G365/M07/39/80/clip_TZUEAGVAgu6ACPkTADaTXKBluUY046.mp3
    但一个一个获取太麻烦  所以要找到他的数据包
    就直接搜索这个链接-->
    找到一个songinfo的数据包  里面有歌曲的所以数据  发现每个songinfo的载荷参数不同的有clienttime:encode_album_audio_id:signature:
    clienttime:用time.time()函数  encode_album_audio_id:是他的歌曲id，之后找的数据包里有
    signature:0ed1f6bcd421268f29cf112ec8c09d22  签名  发现是一个32位的md5 需要破译
'''
import json
import time
import MD5加密

import requests
import hashlib
header = {
    'Cookie': 'kg_mid=d883995a1c69e128c82c30da1a653671; kg_dfid=1txQjF11nqGw2Bu4s31ACHIK; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1710999595; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; KuGooRandom=66291710999863367; kg_mid_temp=d883995a1c69e128c82c30da1a653671; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1711000815',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

date = int(time.time()*1000)
music_id ='j410q60'
signature = MD5加密.get_data(date,music_id)
data = {
    'srcappid':'2919',
    'clientver':'20000',
    'clienttime':date,
    'mid':'d883995a1c69e128c82c30da1a653671',
    'uuid':'d883995a1c69e128c82c30da1a653671',
    'dfid':'1txQjF11nqGw2Bu4s31ACHIK',
    'appid':'1014',
    'platid':'4',
    'encode_album_audio_id':music_id,
    'token':'',
    'userid':'0',
    'signature':signature,
}
url = 'https://wwwapi.kugou.com/play/songinfo'

# print(data)
response = requests.get(url,params=data,headers=header)
html = response.text
ree = json.loads(html)
audio_name = ree['data']['audio_name']
play_url = ree['data']['play_url']
print(ree['data']['audio_name'])
print(ree['data']['play_url'])
# print(ree)
# res = requests.get(play_url,headers=header).content

# with open('video\\'+audio_name+'.mp3',mode='wb')as f:
#     f.write(res)