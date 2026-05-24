# coding:utf-8
# @Author:xb
# @Time: 2024/3/7 12:24
# @File:get_tcent_video.py
# 1.明确采集网站，及数据内容 url = 'https://www.bilibili.com/video/BV1dy421q7ri/'
#   视频画面和视频音频
# m3u8:把整个视频分为n个片段
# 2.技术步骤：
#         1.打开开发者工具 F12
#         2.刷新网页
#         3.搜索.m3u8 不是.js文件它用来传输数据  再在代码里搜索.m3u8数据链接 https://--- .m3u8 搜这个链接 下载就是视频片段
#           获得第一次搜到的.m3u8 链接
#         再在filter搜索 00_gzc 得到请求头的链接 和 其他的gzc合并的到10秒钟视频
#
# 3.代码实现步骤：
#         1.发送请求
#         2.获取数据
#         3.解析数据
#         4.保存数据
#   大型网站一般用
"""
    .m3u8 .mp4 .m4s .avi
"""
import requests
import re
from tqdm import tqdm
headers = {

    'cookie': 'tvfe_boss_uuid=dd52a67771b4f893; pgv_pvid=3830745632; appuser=D2B60A2BAF46CF53; RK=R52Mu+AUbZ; ptcz=f84e9c4a86c15476c3b12523a44eafb402160797567d3a725c99efec6d93a4af; o_cookie=1808873958; qq_domain_video_guid_verify=62c40d352016a79456f207d018ab3953; lv_play_index=10; _qimei_fingerprint=971806672d2026ee76742c387bd9ede6; _qimei_h38=8f955ca7ec9aeea30d33e8240200000a817912; _qimei_q36=; o_minduid=cfFUpwmUWkIGYvnIj5bQA8GN68MkEmYM; pgv_info=ssid=s1057670522; video_omgid=62c40d352016a79456f207d018ab3953; vversion_name=8.2.95; Lturn=115; LKBturn=381; LPVLturn=135; LPLFturn=511; LZCturn=875; LPSJturn=83; LBSturn=303; LVINturn=172; LPHLSturn=533; LDERturn=963; LPPBturn=593; qz_gdt=6zfoszibaaaasf5xlzja; LZTturn=463; full_screen_cid_pause_times=7; full_screen_pause_cid_short_times_times=1; full_screen_pause_times=7; full_screen_pause_short_times_times=1',
    'referer': 'https://v.qq.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.1.4031 SLBChan/105',

}

tencent_url = 'https://apd-vlive.apdcdn.tc.qq.com/moviets.tc.qq.com/AzFREYD-Cii1gZKzSTd22yIoaeLuuZE03DzfQ1reCHKM/B_JxNyiJmktHRgresXhfyMeqx-_Vw-n06OMbvXo6yy35cVJsREWYwbdgn_j4PrhJfb/svp_50112/0CWOOCSmDt8LiU4PhHmCL9_F2JXOSBrMwSSwMwT99Zdld-Lyzr_1xpTh59jJOWINQaw7OT_mA4qCED5nd3yj_kJIMDkMgfEKgI2i7ag62pq88akAS7toB0IuVTLaSfUsd7dL78wKa3mudBuFn4Cl9CvsmiWHFM9PHTqd0GuvzSgDTg4JosU4MX5Gf2XIrtIVx0ahD3yk5nXI1APGfUznjKXKKgIMBo7c-mPMV6eYSLkp-yCLQ1BAJWvsFHBLyKGk/gzc_1000102_0b53a4aaaaaar4adfgb3irrmab6daafqabca.f323012.ts.m3u8'

respose = requests.get(url=tencent_url,headers=headers)
# print(respose.text)
#去掉文本中 前缀为‘#’那一行的字符串 就是把哪一行替换为空
html_txt = re.sub('#.*','',respose.text)
# print(html_txt)
ts_list = html_txt.split()
#再终端获取前半段链接，让他们合并在一起
url_0 = 'https://apd-vlive.apdcdn.tc.qq.com/moviets.tc.qq.com/AzFREYD-Cii1gZKzSTd22yIoaeLuuZE03DzfQ1reCHKM/B_JxNyiJmktHRgresXhfyMeqx-_Vw-n06OMbvXo6yy35cVJsREWYwbdgn_j4PrhJfb/svp_50112/0CWOOCSmDt8LiU4PhHmCL9_F2JXOSBrMwSSwMwT99Zdld-Lyzr_1xpTh59jJOWINQaw7OT_mA4qCED5nd3yj_kJIMDkMgfEKgI2i7ag62pq88akAS7toB0IuVTLaSfUsd7dL78wKa3mudBuFn4Cl9CvsmiWHFM9PHTqd0GuvzSgDTg4JosU4MX5Gf2XIrtIVx0ahD3yk5nXI1APGfUznjKXKKgIMBo7c-mPMV6eYSLkp-yCLQ1BAJWvsFHBLyKGk/'
for video in tqdm(ts_list):
    ts_url = url_0+video
    video_content = requests.get(url=ts_url,headers=headers).content
    open('video\\'+'机械师1.mp4',mode='ab').write(video_content)

# for video in ts_list:
#     ts_url = url_0+video
#     # open('video\\'+'机械师1.mp4',mode='ab').write(video_content)
#     print(ts_url)










