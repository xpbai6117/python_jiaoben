# coding:utf-8
# @Author:xb
# @Time: 2024/3/4 22:26
# @File:biquge_xiaoshuo.py
from selenium import webdriver
import requests,re,os,time,shutil,threading,queue
from lxml import etree
import pandas as pd

# 定义一个函数来获取小说章节目录的URL和章节名
def get_chapter_urls(url, visited_urls, value):
    global tot_title
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    html = etree.HTML(response.text)
    chapter_elements = html.xpath("//div[@class='listmain']//dd/a")
    chapter_elements.pop(10)
    tot_title = html.xpath("//div[@class='info']/h1/text()")
    chapter_urls = []
    for element in chapter_elements:
        chapter_name = element.text
        chapter_url = 'https://www.biqg.cc'+element.get('href')
        if chapter_url not in visited_urls:
            value +=1
            chapter_urls.append((chapter_name, chapter_url, value))
            visited_urls.add(chapter_url)
    return chapter_urls

# 定义一个函数来获取小说具体章节的内容
def get_chapter_content(url):
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    html = etree.HTML(response.text)
    content_element = html.xpath("//div[@id='chaptercontent']/text()")[:-1]
    pattern = r'\r\n        \xa0\xa0\xa0\xa0|\s'
    content = [re.sub(pattern, '', sub_text) for sub_text in content_element]
    return content

# 定义一个函数来处理每个章节的爬取任务
def process_chapter(chapter_queue):
    global time_start
    time_start = time.time()
    while not chapter_queue.empty():
        chapter_name, chapter_url, value = chapter_queue.get()
        print("正在爬取章节：", chapter_name)
        content = get_chapter_content(chapter_url)
        # 在这里可以将内容保存到文件或进行其他处理
        folder_path = f'{tot_title[0]}'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        with open(f'{tot_title[0]}/{value}.txt', 'w', encoding='utf-8') as f:
            f.write('\n'+chapter_name+'\n')
            for data in content:
                f.write(data + '\n')
            f.write('\n\n')
        chapter_queue.task_done()

#合并下载的TXT文件
def merge_txt_files(folder_path, output_file):
    txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
    txt_files.sort(key=lambda x: int(x[:-4]))

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for txt_file in txt_files:
            with open(os.path.join(folder_path, txt_file), 'r', encoding='utf-8') as infile:
                content = infile.read()
                outfile.write(content)

#搜索小说，并选择所需要下载的小说
def search_novel():
    #chrome_options = webdriver.ChromeOptions()
    # 后台静默运行
    #chrome_options.add_argument('--headless')
    #print('浏览器已打开')
    #browser = webdriver.Chrome(options=chrome_options)
    browser = webdriver.Chrome()
    name_input = input('输入小说名或作者：')
    browser.get(f'https://www.biqg.cc/s?q={name_input}')
    time.sleep(3)
    # 输出网页源代码
    html=browser.page_source
    browser.close()
    #print('浏览器已关闭')
    html = etree.HTML(html)
    name = html.xpath("//div[@class='type_show']//div//a/text()")#/html/body/div[5]/div/div/div[1]/div/div[2]/h4/a
    link = html.xpath("//div[@class='type_show']//div//h4/a/@href")#/html/body/div[5]/div/div/div[2]/div/div[2]/h4/a
    author = html.xpath("//div[@class='type_show']//div[@class='author']/text()")#/html/body/div[5]/div/div/div[1]/div/div[2]/div[1]
    num = [i+1 for i in range(0, len(name))]#/html/body/div[5]/div/div/div[1]/div/div[1]/a/img
    data = {'序号':num, '小说':name, '作者':author, '链接':link}#/html/body/div[5]/div/div/div[1]/div/div[2]/h4/a
    df = pd.DataFrame(data)
    if df.empty:
        print('搜索数据为空，请重新搜索')
        search_novel()
    else:
        print(df)
        sx_input = int(input('请输入序号选择下载的小说：'))
        novel_link = 'https://www.biqg.cc' + link[sx_input-1]
        return novel_link

def search_continue():
    input_continue = input('请输入y/n选择是否继续下载小说：')
    if input_continue == 'y':
        main()
    else:
        return

def main():
    directory_url = search_novel()
    # 获取小说章节目录的URL和章节名
    visited_urls = set()
    value = 0
    chapter_urls = get_chapter_urls(directory_url, visited_urls, value)
    # 创建一个队列来存储待爬取的章节信息
    chapter_queue = queue.Queue()
    for chapter_name, chapter_url, value in chapter_urls:
        chapter_queue.put((chapter_name, chapter_url, value))
    # 创建多个线程来并发爬取章节内容
    print('='*64)
    print('线程数建议在10-30之间，避免对目标服务器造成过大压力')
    sum = int(input('输入线程数：'))
    num_threads = sum  # 设置线程数量，根据需要进行调整
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=process_chapter, args=(chapter_queue,))
        thread.daemon = False
        thread.start()
        threads.append(thread)
    # 等待所有线程完成任务
    chapter_queue.join()
    # 等待所有线程结束
    for thread in threads:
        thread.join()
    print("所有章节爬取完成！")
    time_end = time.time()
    print('章节爬取花费时间：', time_end-time_start)
    print('='*64)
    print('开始合并所有TXT文件')
    folder_path_1 = f'{tot_title[0]}/'  # 请替换为实际文件夹路径
    output_file = f'{tot_title[0]}.txt'  # 输出文件名
    merge_txt_files(folder_path_1, output_file)
    print('合并所有TXT文件成功')
    print(f'{tot_title[0]}下载成功')
    shutil.rmtree(tot_title[0])
    print('='*64)
    search_continue()

# 主程序入口
if __name__ == "__main__":
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 HBPC/12.1.3.306'}
    main()