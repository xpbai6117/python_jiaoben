# coding:utf-8
# @Author:xb
# @Time: 2024/4/17 10:26
# @File:get_ip.py
import requests
import threading

# 代理 IP 地址列表
proxy_list = [
    "1.1.1.1:80",
    "2.2.2.2:80",
    "3.3.3.3:80",
    # ... 添加更多代理 IP 地址
]

# 要测试的 URL
test_url = "https://www.example.com"

# 有效的代理 IP 地址列表
valid_proxies = []

# 测试代理 IP 地址的函数
def test_proxy(proxy):
    try:
        # 使用代理 IP 地址发送 HTTP 请求
        response = requests.get(test_url, proxies={"http": proxy, "https": proxy}, timeout=5)

        # 如果请求成功，则将代理 IP 地址添加到有效列表中
        if response.status_code == 200:
            valid_proxies.append(proxy)
    except:
        pass

# 创建线程池，并发地测试代理 IP 地址
threads = []
for proxy in proxy_list:
    thread = threading.Thread(target=test_proxy, args=(proxy,))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

# 打印有效的代理 IP 地址
print("Valid proxies:")
for proxy in valid_proxies:
    print(proxy)
