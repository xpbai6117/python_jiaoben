import json
import time
import urllib

# url = 'https://www.douyin.com/user/MS4wLjABAAAAtJgfxkU4tElRYAnvqpeZamA8j4nRSe-y5w96O4Y-X-4?modal_id=7348793140469386533'


# uurl = re.findall("playApi': '//(.*?)', 'playAddrH265",json_data)
# print(uurl)
import re
import requests
headers = {
    'Cookie':
        'douyin.com; ttwid=1%7C7fOMZllfC-3_judevXH6KK8GuD3zuhKhTHeMe8ADB4I%7C1711502099%7C300c74f4ce25e8b0ba5e0e033391d70d58adc660c8fc6be2e196c315ada5e4d7; douyin.com; device_web_cpu_core=12; device_web_memory_size=8; architecture=amd64; dy_swidth=1920; dy_sheight=1080; csrf_session_id=37b11971f67491d2b77272eca88cf9bc; strategyABtestKey=%221711502103.327%22; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; passport_csrf_token=4b0906201d974fe3b832fc25bdf64d50; passport_csrf_token_default=4b0906201d974fe3b832fc25bdf64d50; bd_ticket_guard_client_web_domain=2; odin_tt=5a922ed135b8e9f1a1362676135a54d5cc778bfe81e4d2be7f4d492f3eecbb18902df0859afcf6d6b6a1216cfac40c993706d06a30c378cc7dbd27a3bea234293ff190a306418d944f53171ecb4fecab; xgplayer_user_id=795784490318; download_guide=%223%2F20240327%2F0%22; pwa2=%220%7C0%7C3%7C0%22; xg_device_score=7.683680908103623; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A12%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCUEVVZDB0UlUrTVhncUFGNm9wdGM2THZqaUtJdDk0RHFGeDhsWmU4NFE3Q2pWa1lTVDhTaHJqOHkrdWFQb1ZNNnNoZ3diaHdMUnh6cm5sa0hIc3ZkNkk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=uqNHaqeQwYiI0rI7NBH61jh5pb4lKB44U_BpAlnx1s-ELp5inXpkUBKnsW0x4N0sZrwfvf13B8atCoWtrHdDldsEu2ZsZuM0HaN959VqHDdx2SaXdRvM_kHZi9Ui; tt_scid=3Vhm7zHwdpCZDu2josTf4IGmi8SbiwyDNgUdH2rro5rgAVSgOxyvVY1kOWQKLh-qe035; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A1%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; msToken=1nm_slgI2lsMamf_d7AbZCwVlkJctMN-esKgEcrNusEnM9jTMvIzEQzokHfnuiAaO4CXIe8cLOVGPdX9rYIzKXaGxSqhYMH_8dTuUdPPE2j8WHOY-p1ouNcTax7A; IsDouyinActive=false; __ac_nonce=06604c48d00031f253735; __ac_signature=_02B4Z6wo00f017VURNwAAIDAiP1eQAVW5du1dEBAAItaVENApEox9Rhb9IXKJ8CfCkAvr.BR5DC6kpS3KEjl8T.0iLlmYcIOr.e3rkrxFXPyLgCqqBNiVP40AtQ2fevhJo.VPYhv8R2B0L6D7e; __ac_referer=__ac_blank',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

# def drop_dwon:
#     '''执行滚动条操作'''
#     for x in range(1,12,2):#1 3 5 7 9 在你不断下拉过程 高度也会变化
#         time.sleep(1)
#         j = x/9 #1/9 3/9 5/9/ 9/9
#         #document.documentElement.scrollTop  指点滚动条位置
#         #document.documentElement.scrollHight  指点浏览器页面最大高度
#         js = 'document.documentElement.scrollTop = document.documentElement.scrollHight * %f' % j
#         driver.execute_script(js)
from selenium import webdriver
#
driver = webdriver.Chrome()
driver.get("https://www.douyin.com/user/MS4wLjABAAAAtJgfxkU4tElRYAnvqpeZamA8j4nRSe-y5w96O4Y-X-4")
driver.implicitly_wait(20)
lis = driver.find_elements_by_css_selector('.niBfRBgX')

for li in lis:
    href = li.find_element_by_css_selector('a').get_attribute('href')
    video_id = href.split('/')[-1]
    url = f'https://www.douyin.com/user/MS4wLjABAAAAtJgfxkU4tElRYAnvqpeZamA8j4nRSe-y5w96O4Y-X-4?modal_id={video_id}'
    response = requests.get(url=url,headers=headers)
    #先找到视频媒体，搜索唯一的rc，到新的链接在搜rc 拿到视频链接 和名字
    data = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>',response.text)
    #title直接在那个视频链接中搜
    title = re.findall(r'"desc\\":\\"(.*?)\\",\\"authorUserId',response.text)
    # new_title = re.sub('[\\//:*?"<>|]', '', title)
    # print(data)la
    print(title)
    print(data)
    # info = urllib.parse.unquote(data[0])
    # json_data = json.loads(info)
    # video_url = 'https:'+json_data['app']['videoDetail']['video']['bitRateList'][0]['playAddr'][0]['src']
    # print(video_url)
#18个视频的合集贝爷河红茶url=https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAA3cQTDOcrCkN7Dl5pwUlLocWgFxCO8RJd3SLA5lkc_ZY&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.60&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7350838697497904640&msToken=hHfpctO3g9mRmjYc5c4i8bTVFk8qSHdrUTGj38GAXJgOtBEZt1MgEpB4cDsxZAZpO4vk0F5iCqbWAWBF4vLI_d6Pl-FfR6O1svAsqSQywSlBMsKKhVh7Gis3zLmZgRY=&X-Bogus=DFSzswVOI4sANyA/t-siMcppgim0
#刷新后贝爷和红茶的     url=https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAA3cQTDOcrCkN7Dl5pwUlLocWgFxCO8RJd3SLA5lkc_ZY&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.60&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=6&effective_type=4g&round_trip_time=50&webid=7350838697497904640&msToken=ERSlxrmpIoKS8P_yODDRBsXeOF4mQI1EPtgdVwpuQDHTOiKuqQAMUswSr8z41Hlbwj4XDMcYS7DpfP6AhtIQgUr5Z3ovzsemkliZWaWJtGESWwePMLyX7v0PAshpfjY=&X-Bogus=DFSzswVY/8zANChSt-susOppgiu4
#又一个18个视频童年减速带url=https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAA3cQTDOcrCkN7Dl5pwUlLocWgFxCO8RJd3SLA5lkc_ZY&max_cursor=1709365800000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.60&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7350838697497904640&msToken=CMtskCDkAPbsXpdbolwPVoyGVh_I1KblGHnkv4bLwfcFb-7YGJYi07iTbO_4zIkGVaTWJxorKuj-kPMjmRozggLvlthrQuxMUIG9YBoxWsJGqKonRBB6Mr7etCjGp3o=&X-Bogus=DFSzswVYw/hANChSt-s72cppgiu3
#童年减速带            url=https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAA3cQTDOcrCkN7Dl5pwUlLocWgFxCO8RJd3SLA5lkc_ZY&max_cursor=1709365800000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.60&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7350838697497904640&msToken=CMtskCDkAPbsXpdbolwPVoyGVh_I1KblGHnkv4bLwfcFb-7YGJYi07iTbO_4zIkGVaTWJxorKuj-kPMjmRozggLvlthrQuxMUIG9YBoxWsJGqKonRBB6Mr7etCjGp3o=&X-Bogus=DFSzswVYw/hANChSt-s72cppgiu3
#我现在刷新在搜童年减速带url=https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAA3cQTDOcrCkN7Dl5pwUlLocWgFxCO8RJd3SLA5lkc_ZY&max_cursor=1709365800000&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.60&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=6&effective_type=4g&round_trip_time=50&webid=7350838697497904640&msToken=u9y8aUE5NL9Dm72GL2jk7GcCv3znSv_zMA212EAl_Q_pSCrC-137a7SaJ73X1x0U_D-lp9028xtUAzcrT32y6NF2tcDge4LG5KAscetXuGdW5knYRIRY84VO8YWDo4E=&X-Bogus=DFSzswVYdviANChSt-suMOppgiFS
#发现mstoken和max_course不一样  那我就首先搜token
#发现和to一样的url=https://www.douyin.com/aweme/v1/web/external/notification/?device_platform=webapp&aid=6383&channel=channel_pc_web&os=2&client_type=1&scene=admin_pc_push&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=117.0.2045.60&browser_online=true&engine_name=Blink&engine_version=117.0.0.0&os_name=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7350838697497904640&msToken=CMtskCDkAPbsXpdbolwPVoyGVh_I1KblGHnkv4bLwfcFb-7YGJYi07iTbO_4zIkGVaTWJxorKuj-kPMjmRozggLvlthrQuxMUIG9YBoxWsJGqKonRBB6Mr7etCjGp3o=&X-Bogus=DFSzswVOSviANyA/t-si/cppgiz5















