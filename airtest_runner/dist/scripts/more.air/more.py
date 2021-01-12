# -*- encoding=utf8 -*-
#内容：社区——热门作品-更多（已登录）
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
    #点击更多
    driver.find_element_by_xpath("//a[@href='/community/all?type=0']").click()
    driver.assert_template(Template(r"tpl1601288417566.png", record_pos=(3.79, 1.615), resolution=(100, 100)), "页面进入全部作品界面")
    #点击全部实验室
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div").click()
    #点击python实验室
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/ul/li[2]/div").click()
    driver.assert_template(Template(r"tpl1601288586694.png", record_pos=(4.435, 2.255), resolution=(100, 100)), "筛选功能正常使用，筛选结果正确")
    #点击专题推荐
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div").click()
    #点击双人大战
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/ul/li/div").click()
    driver.assert_template(Template(r"tpl1601288722464.png", record_pos=(5.66, 2.255), resolution=(100, 100)), "筛选功能正常使用，筛选结果正确")
    #点击最热
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/a").click()
    #点击最新
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/a[2]").click()
    #点击最新
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div/a").click()
    #点击作者名称
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div[2]/div/ul/li/div/div[3]/p/a").click()
    driver.assert_template(Template(r"tpl1601289281514.png", record_pos=(3.59, 4.54), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
    driver.airtest_touch(Template(r"tpl1601289357814.png", target_pos=7, record_pos=(3.64, 4.785), resolution=(100, 100)))
    driver.switch_to_new_tab()

    driver.assert_template(Template(r"tpl1601289412092.png", record_pos=(12.33, 2.615), resolution=(100, 100)), "点击作品图片，进入作品页面")
    driver.close()#关闭标签
    driver.switch_to_previous_tab()
    driver.back()
    #向下翻页
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
    #点击底部303
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div[3]/span[5]").click()
    driver.assert_template(Template(r"tpl1601290334816.png", rgb=True, record_pos=(10.47, 7.785), resolution=(100, 100)), "页面跳转至该页")
    #向上翻页
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_UP)
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_UP)
    #点击搜索输入框并输入
    driver.find_element_by_xpath("//input[@placeholder='请输入搜索关键字']").send_keys("未命名")
    #按回车键
    driver.find_element_by_css_selector('body').send_keys(Keys.ENTER)   
    driver.assert_template(Template(r"tpl1601290742068.png", record_pos=(0.4, 5.3), resolution=(100, 100)), "作品列表显示包含改字的作品")
    #输入作品列表中名字不包含的字或其他     
    driver.find_element_by_xpath("//input[@placeholder='请输入搜索关键字']").clear()
    driver.find_element_by_xpath("//input[@placeholder='请输入搜索关键字']").send_keys("xxxxxxx")
    #按回车键
    #driver.find_element_by_css_selector('body').send_keys(Keys.ENTER)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/a/i").clear()
    #driver.assert_template(Template(r"tpl1601291282352.png", record_pos=(1.655, 3.85), resolution=(100, 100)), "作品列表空白显示")
    driver.quit()
    return

try:
    main()
except:
    driver.quit()