# -*- encoding=utf8 -*-
#内容：名师团——头部工作室显示（已登录）
#编写人：钟俊
#修改时间：2020-10-23
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
    driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/ul/li[4]/a").click()#进入名师团
    driver.assert_template(Template(r"tpl1601360475160.png", record_pos=(0.615, 5.87), resolution=(100, 100)), "显示工作室图片，名称无误")
    driver.assert_template(Template(r"tpl1601360494325.png", record_pos=(2.07, 5.935), resolution=(100, 100)), "显示工作室图片，名称无误")
    driver.assert_template(Template(r"tpl1601360506762.png", record_pos=(3.72, 5.83), resolution=(100, 100)), "显示工作室图片，名称无误")
    driver.assert_template(Template(r"tpl1601360519255.png", record_pos=(5.26, 5.895), resolution=(100, 100)), "显示工作室图片，名称无误")
    driver.assert_template(Template(r"tpl1601360530920.png", record_pos=(6.83, 5.795), resolution=(100, 100)), "显示工作室图片，名称无误")
    driver.assert_template(Template(r"tpl1601360544278.png", record_pos=(8.385, 5.835), resolution=(100, 100)), "显示工作室图片，名称无误")
    driver.assert_template(Template(r"tpl1601360559477.png", record_pos=(9.96, 5.83), resolution=(100, 100)), "显示工作室图片，名称无误")
    driver.assert_template(Template(r"tpl1601360574563.png", record_pos=(11.555, 5.73), resolution=(100, 100)), "盛思工作室图片，名称显示无误")
    driver.quit()
    return
try:
    main()
except:
    driver.quit()
    
    