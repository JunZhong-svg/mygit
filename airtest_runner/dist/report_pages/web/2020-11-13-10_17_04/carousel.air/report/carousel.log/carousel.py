# -*- encoding=utf8 -*-
#内容：社区——轮播页（已登录）
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
from selenium.webdriver import ActionChains

driver = common.login()#进入网页并登录
def main():
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/ul/li[6]/a").click()#进入社区
    #banana页3页轮播图片
    driver.assert_template(Template(r"tpl1604285556713.png", record_pos=(-0.002, -0.047), resolution=(1920, 1080)), "第一张图片")


    driver.assert_template(Template(r"tpl1602207106319.png", record_pos=(7.795, 2.345), resolution=(100, 100)), "第二张图片")
    driver.assert_template(Template(r"tpl1602207146720.png", record_pos=(6.795, 2.32), resolution=(100, 100)), "第三张图片")
    #点击banana页图片
    driver.find_element_by_xpath("//img[@src='https://qgcdn0.gtimg.com/common_manage/2782/ImgUrl_fc92ec4fac16a5803e1e8e695f6943be.png']").click()
    driver.switch_to_new_tab()
    driver.assert_template(Template(r"tpl1602207414351.png", record_pos=(6.145, 3.36), resolution=(100, 100)), "跳转至对应链接")
    driver.close()#关闭标签
    driver.switch_to_previous_tab()
    #点击banana页下方白色选择按钮
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/span").click()
    driver.assert_template(Template(r"tpl1604285556713.png", record_pos=(-0.002, -0.047), resolution=(1920, 1080)), "第一张图片")
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/span[2]").click()
    driver.assert_template(Template(r"tpl1602207106319.png", record_pos=(7.795, 2.345), resolution=(100, 100)), "第二张图片")
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/span[3]").click()
    driver.assert_template(Template(r"tpl1602207146720.png", record_pos=(6.795, 2.32), resolution=(100, 100)), "第三张图片")
    driver.quit()
    return
try:
    main()
except:
    driver.quit()

    
    
