# -*- encoding=utf8 -*-
#内容：个人中心——我的项目和我的群组（已登录）
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

driver = common.enter_personalCenter()#进入个人中心
'''个人中心-我的项目和我的群组'''  
def main():
    #点击我的项目
    driver.find_element_by_xpath("//a[@href='/personal/project']").click()
    driver.assert_template(Template(r"tpl1602637316833.png", record_pos=(6.29, 1.48), resolution=(100, 100)), "打开我的项目")
    #点击我的群组
    driver.find_element_by_xpath("//a[@href='/personal/group']").click()
    driver.assert_template(Template(r"tpl1601279412736.png", rgb=True, record_pos=(6.05, 1.99), resolution=(100, 100)), "默认显示全部群组")
        
    #点击我创建的
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/a[2]").click()
    driver.assert_template(Template(r"tpl1602637589842.png", rgb=True, record_pos=(6.805, 2.0), resolution=(100, 100)), "打开我的创建")

        
    #点击我加入的
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/a[3]").click()
        
    driver.assert_template(Template(r"tpl1601279662622.png", record_pos=(7.78, 2.0), resolution=(100, 100)), "显示所有我加入的群组")
        
    #点击去创建或创建群组按钮
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/a").click()
    driver.assert_template(Template(r"tpl1601279758492.png", record_pos=(9.09, 4.975), resolution=(100, 100)), "弹出创建群组弹窗")
    #创建群组名不输入字符创建
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div[3]/div/a").click()
    driver.assert_template(Template(r"tpl1601280301336.png", record_pos=(9.085, 2.93), resolution=(100, 100)), "界面上方弹窗提示名字不能为空")
    #创建群组名空格字符创建
    driver.find_element_by_xpath("//input[@placeholder='请输入群名']").send_keys("   ")
    #driver.assert_template(Template(r"tpl1601280301336.png", record_pos=(9.085, 2.93), resolution=(100, 100)), "界面上方弹窗提示名字不能为空")
    #关闭创建群组弹窗
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/a/i").click()
        
    '''加入群组弹窗显示'''
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/a[2]").click()
    driver.assert_template(Template(r"tpl1601280787948.png", record_pos=(9.06, 5.045), resolution=(100, 100)), "弹出加入群组弹窗")
        
    '''邀请码为空时确认提示'''
    driver.find_element_by_xpath("//input[@placeholder='请输入6位群组邀请码']").send_keys("")
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div[3]/div/a").click()
    #driver.assert_template(Template(r"tpl1601280957275.png", record_pos=(9.105, 2.22), resolution=(100, 100)), "提示邀请码不能为空")
    driver.snapshot()
        
    driver.find_element_by_xpath("//input[@placeholder='请输入6位群组邀请码']").send_keys("123456")
    driver.snapshot()
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div[3]/div[2]/div/div/div[3]/div/a").click()
    #driver.assert_template(Template(r"tpl1601281150193.png", record_pos=(4.34, 4.395), resolution=(100, 100)), "上方弹出加入群组失败，请确认邀请码是否正确")  
    driver.quit()
    return
try:
    main()
except:
    driver.quit()


