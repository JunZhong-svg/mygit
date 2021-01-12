# -*- encoding=utf8 -*-
#内容：社区——作品-小小编程家（已登录）
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
    driver.assert_template(Template(r"tpl1601349318096.png", record_pos=(13.94, 5.515), resolution=(100, 100)), "显示作者名称，头像，作品数，获赞数无误")
    driver.assert_template(Template(r"tpl1601349343326.png", record_pos=(13.78, 6.455), resolution=(100, 100)), "显示作者名称，头像，作品数，获赞数无误")
    driver.assert_template(Template(r"tpl1601349351231.png", record_pos=(14.355, 6.48), resolution=(100, 100)), "显示作者名称，头像，作品数，获赞数无误")
    #点击作者头像或名称
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/ul/li/div/div/p/a").click()
    driver.assert_template(Template(r"tpl1601349494849.png", record_pos=(3.51, 4.53), resolution=(100, 100)), "页面进入作者详情页")
    driver.assert_template(Template(r"tpl1601349507991.png", record_pos=(9.015, 3.64), resolution=(100, 100)), "页面进入作者详情页")
    driver.quit()
    return
   
    driver.quit()
    return
try:
    main()
except:
    driver.quit()
    
    