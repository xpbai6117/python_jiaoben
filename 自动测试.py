# coding:utf-8
# @Author:xb
# @Time: 2024/3/1 21:02
# @File:自动测试.py
from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.baidu.com")

input = driver.find_element_by_css_selector('#kw')
input.send_keys("苍老师照片")

button = driver.find_element_by_css_selector('#su')
button.click()