# -*- encoding=utf8 -*-
#内容：社区——热门作品-反应大挑战2（已登录）
#编写人：钟俊
#修改时间：2020-10-22
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

using(r"common.air")
from common import common
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = common.login()#进入网页并登录
def main():
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/ul/li[6]/a").click()#进入社区 
    ele = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div[2]/div[1]/div[9]/div[1]/h2')
    driver.execute_script("arguments[0].scrollIntoView();",ele)
    #查看反应大挑战2模块
    driver.assert_template(Template(r"tpl1601343158429.png", record_pos=(3.53, 5.25), resolution=(100, 100)), "反应大挑战2模块显示正常")
    #鼠标移动到作品图片上
    pic = driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[8]/div[2]/div/div/div[1]/div/div[1]/a/img")
    ActionChains(driver).move_to_element(pic).perform()
    #截图
    driver.snapshot()
    sleep(3)
    #点击作者名称或头像，进入该作者详情页
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div[8]/div[2]/div/div/div/div/div[3]/p/a").click()
    driver.assert_template(Template(r"tpl1601343379686.png", record_pos=(3.57, 4.55), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
    driver.assert_template(Template(r"tpl1601343408897.png", record_pos=(5.27, 3.705), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
    #点击作品图片，进入作品页面
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/div/div[1]/a/img').click()
    driver.switch_to_new_tab()
    driver.assert_template(Template(r"tpl1601343521209.png", record_pos=(12.345, 2.57), resolution=(100, 100)), "点击作品图片，进入作品页面")
    driver.close()#关闭标签
    driver.switch_to_previous_tab()
    driver.back()   
    driver.quit()
    return
try:
    main()
except:
    driver.quit()