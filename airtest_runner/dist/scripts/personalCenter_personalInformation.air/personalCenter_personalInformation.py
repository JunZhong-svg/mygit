# -*- encoding=utf8 -*-
#内容：个人中心——个人资料（已登录）
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
'''个人中心-个人资料'''  
def main():
    driver.find_element_by_xpath("//a[@href='/personal/edit']").click()
    driver.assert_template(Template(r"tpl1601264296698.png", record_pos=(6.225, 1.7), resolution=(100, 100)), "个人资料展示昵称")
    driver.assert_template(Template(r"tpl1601264304345.png", record_pos=(6.27, 2.37), resolution=(100, 100)), "个人资料展示真实姓名")
    driver.assert_template(Template(r"tpl1601264311601.png", record_pos=(6.25, 3.025), resolution=(100, 100)), "个人资料展示性别")
    driver.assert_template(Template(r"tpl1601264320003.png", record_pos=(6.275, 3.585), resolution=(100, 100)), "个人资料展示出生年月")
    driver.assert_template(Template(r"tpl1601264330396.png", record_pos=(6.285, 4.24), resolution=(100, 100)), "个人资料展示我的位置")
    driver.assert_template(Template(r"tpl1601264374454.png", record_pos=(7.59, 5.305), resolution=(100, 100)), "个人资料展示允许使用扣钉账号登录")
    driver.assert_template(Template(r"tpl1601264349802.png", record_pos=(7.56, 6.285), resolution=(100, 100)), "个人资料展示保存资料")
        
    '''昵称修改'''
    driver.find_element_by_name("nick").send_keys("哈哈")
    driver.find_element_by_name("name").click()
    driver.assert_template(Template(r"tpl1601265035606.png", record_pos=(7.0, 1.675), resolution=(100, 100)), "昵称不修改，为原昵称")
        
    '''昵称修改不输入限制'''
    driver.find_element_by_name("nick").send_keys(" ")
    #点击保存资料
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/a").click()
        
        
    '''真实姓名显示'''
    driver.find_element_by_name("name").send_keys("哈哈")
    driver.find_element_by_name("nick").click()
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/a").click()
        
    '''真实姓名不输入限制'''
    driver.find_element_by_name("name").send_keys(" ")
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/a").click()
        
    '''性别显示'''
    driver.find_element_by_xpath("//label[@title='男']").click()
    driver.assert_template(Template(r"tpl1601276357525.png", record_pos=(6.95, 3.015), resolution=(100, 100)), "选中的性别选择点蓝色标志")
        
    '''出生年月显示'''
    #年
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/ul/li[4]/div/div/div").click()
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/ul/li[4]/div/div[2]/div/ul/li[43]/div").click()
    #月
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/ul/li[4]/div[2]/div/div").click()
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/ul/li[4]/div[2]/div[2]/div/ul/li[3]/div").click()
    #日
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/ul/li[4]/div[3]/div/div").click()
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/ul/li[4]/div[3]/div[2]/div/ul/li[3]/div").click()
    driver.assert_template(Template(r"tpl1601276673300.png", record_pos=(9.055, 3.56), resolution=(100, 100)), "选定后，出生年月显示为所选的年月")
        
    '''我的位置显示'''     
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/ul/li[5]/div/div/div").click()
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/ul/li[5]/div/div[2]/div/ul/li/div").click()
    driver.assert_template(Template(r"tpl1601276907054.png", record_pos=(7.055, 4.26), resolution=(100, 100)), "选择栏显示为所选的地区")
        
        
    '''扣叮账号密码显示'''
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/ul/li[6]/div[2]/a").click()
    assert_template(Template(r"tpl1601279047692.png", record_pos=(11.105, 4.91), resolution=(100, 100)), "密码显示，显示字样变成隐藏")
    #点击保存资料
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/a").click() 
    driver.quit()
    return


try:
    main()
except:
    driver.quit()

