# -*- encoding=utf8 -*-
#内容：社区——热门作品-伙伴帮帮忙（已登录）
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
    #向下翻页3次
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
    driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        
    #查看伙伴帮帮忙模块
    driver.assert_template(Template(r"tpl1601342191423.png", record_pos=(3.49, 1.21), resolution=(100, 100)), "伙伴帮帮忙模块显示正常")
    #鼠标移动到作品图片上
    pic = driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[7]/div[2]/div/div/div[1]/div/div[1]/a/img")
    ActionChains(driver).move_to_element(pic).perform()
        #截图
    driver.snapshot()
    sleep(3)
    #点击作者名称或头像，进入该作者详情页
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div[7]/div[2]/div/div/div/div/div[3]/p/a").click()
    driver.assert_template(Template(r"tpl1601342517596.png", record_pos=(3.565, 4.54), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
    driver.assert_template(Template(r"tpl1601342545406.png", record_pos=(9.045, 3.77), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        
    #点击作品图片，进入作品页面
    driver.find_element_by_xpath("//img[@src='https://p.qpic.cn/qqgameedu/0/1106e5bbcf7bfc4622823fa4770f3407/0']").click()
    driver.switch_to_new_tab()

    driver.assert_template(Template(r"tpl1601342636489.png", record_pos=(12.365, 2.57), resolution=(100, 100)), "点击作品图片，进入作品页面")
    driver.close()#关闭标签
    driver.switch_to_previous_tab()
    driver.back()
    driver.quit()
    return

try:
    main()
except:
    driver.quit()
    
        
        
        