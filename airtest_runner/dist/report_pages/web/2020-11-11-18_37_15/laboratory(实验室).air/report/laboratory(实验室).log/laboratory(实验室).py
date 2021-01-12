# -*- encoding=utf8 -*-
#内容：社区——实验室（已登录）
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
    #创意实验室
    driver.assert_template(Template(r"tpl1601285915155.png", record_pos=(5.335, 5.915), resolution=(100, 100)), "显示实验室图片")

    driver.assert_template(Template(r"tpl1601285890439.png", rgb=True, record_pos=(3.79, 6.045), resolution=(100, 100)), "显示实验室在用人数")
        
    driver.find_element_by_xpath("//a[@href='/creative-lab']").click()
    driver.assert_template(Template(r"tpl1601286061822.png", record_pos=(10.095, 5.01), resolution=(100, 100)), "页面跳转至创意实验室")
    driver.back()
    #python实验室
    driver.assert_template(Template(r"tpl1603354481883.png", record_pos=(-0.031, 0.052), resolution=(1920, 1080)), "显示实验室图片")
    driver.assert_template(Template(r"tpl1601286266354.png", rgb=True, record_pos=(7.005, 6.025), resolution=(100, 100)), "显示实验室在用人数")
    driver.find_element_by_xpath("//a[@href='/python-lab']").click()
    driver.assert_template(Template(r"tpl1601286371990.png", record_pos=(1.42, 0.455), resolution=(100, 100)), "页面跳转至python实验室")
    driver.back()
    #人工智能实验室
    driver.assert_template(Template(r"tpl1601287467885.png", record_pos=(11.62, 5.875), resolution=(100, 100)), "显示实验室图片")
    driver.assert_template(Template(r"tpl1601287482164.png", rgb=True, record_pos=(10.245, 6.025), resolution=(100, 100)), "显示实验室在用人数")
    driver.find_element_by_xpath("//a[@href='/ai-lab']").click()
    driver.assert_template(Template(r"tpl1601287569533.png", record_pos=(1.47, 0.45), resolution=(100, 100)), "页面跳转至人工智能实验室")
    driver.quit()
    return

try:
    main()
except:
    driver.quit()