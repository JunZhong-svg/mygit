# -*- encoding=utf8 -*-
#内容：头像下拉窗（已登录）
#编写人：钟俊
#修改时间：2020-10-14
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

using(r"common.air")
from common import common
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
from selenium.webdriver import ActionChains

driver = common.login()#登录

def main():
    HeadPortrait = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[1]/div/div[2]/div[2]/div/div/img")
    ActionChains(driver).move_to_element(HeadPortrait).perform()#鼠标到头像处
    #进入人中心
    driver.find_element_by_link_text("个人中心").click()
    driver.switch_to_new_tab()
    driver.assert_template(Template(r"tpl1602644590492.png", record_pos=(3.695, 4.26), resolution=(100, 100)), "进入个人中心")
    driver.close()#关闭标签
    driver.switch_to_previous_tab()

        
        
    #消息中心
    ActionChains(driver).move_to_element(HeadPortrait).perform()#鼠标到头像处
    driver.find_element_by_link_text("消息中心").click()
    driver.switch_to_new_tab()
    driver.assert_template(Template(r"tpl1601274159905.png", record_pos=(3.81, 1.37), resolution=(100, 100)), "默认显示全部消息")
    driver.close()#关闭标签
    driver.switch_to_previous_tab()
        
    #用户反馈
    ActionChains(driver).move_to_element(HeadPortrait).perform()#鼠标到头像处
    driver.find_element_by_link_text("用户反馈").click()
    driver.switch_to_new_tab()
    driver.assert_template(Template(r"tpl1601274311699.png", record_pos=(8.945, 1.89), resolution=(100, 100)), "跳转“腾讯扣叮”用户反馈界面")
    driver.close()#关闭标签
    driver.switch_to_previous_tab()
        
        
    #退出登录
    ActionChains(driver).move_to_element(HeadPortrait).perform()#鼠标到头像处
    driver.find_element_by_link_text("退出登录").click()
    driver.switch_to_new_tab()
    #driver.assert_template(Template(r"tpl1601274520320.png", record_pos=(18.17, 0.49), resolution=(100, 100)), "退出登录")
    driver.quit()
    return
    
try:
    main()
except:
    driver.quit()