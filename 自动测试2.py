# coding:utf-8
# @Author:xb
# @Time: 2024/3/1 22:44
# @File:自动测试2.py
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

search_box = driver.find_element_by_css_selector('#kw')
search_box.send_keys("苍老师照片")

search_button = driver.find_element_by_css_selector('#su')
search_button.click()
