# -*- encoding=utf8 -*-
#内容：个人中心——我的作品（已登录）
#编写人：钟俊
#修改时间：2020-10-12
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
'''个人中心-我的作品'''  
def main(): 
    driver.find_element_by_xpath("//a[@href='/personal/work']").click()#点击我的作品
    driver.assert_template(Template(r"tpl1601259230667.png", record_pos=(3.785, 1.385), resolution=(100, 100)), "进入个人中心，默认展示我的作品全部作品")
    
    a = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div/div[2]/div/div[1]/div[3]/div/div/div/a')#寻找’选择实验室‘元素
    ActionChains(driver).move_to_element(a).perform()#鼠标移动到’选择实验室‘
    #点击创意实验室
    #driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div[1]/div[3]/div/div/div/a").click()
    driver.airtest_touch(Template(r"tpl1604283067449.png", record_pos=(-0.126, -0.127), resolution=(1920, 1080)))

    driver.assert_template(Template(r"tpl1602466742739.png", record_pos=(3.955, 2.01), resolution=(100, 100)), "显示创意实验室作品")
    #点击全部
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/a").click()

    '''个人中心-我的作品-全部作品-批量删除显示'''
    #点击批量删除
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div/div[3]/a").click()
    driver.assert_template(Template(r"tpl1601259840260.png", record_pos=(12.025, 2.02), resolution=(100, 100)), "批量删除文字变为取消删除")
    
    #勾选作品
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/ul/li/div/span").click()
    driver.assert_template(Template(r"tpl1602467342380.png", record_pos=(11.715, 2.01), resolution=(100, 100)), "批量删除文字变为确认删除")
    
    #取消勾选
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/ul/li/div/div/div/img").click()
    driver.assert_template(Template(r"tpl1601259840260.png", record_pos=(12.025, 2.02), resolution=(100, 100)), "确认删除文字变为取消删除")
  
    #点击取消删除
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div/div[3]/a").click()
    driver.assert_template(Template(r"tpl1602467016736.png", record_pos=(11.71, 2.01), resolution=(100, 100)), "取消删除文字变为批量删除")
    
    #作品名称查看
    driver.assert_template(Template(r"tpl1602467753009.png", record_pos=(3.38, 4.995), resolution=(100, 100)), "作品图片下方显示作品名称")
    #查看作品列表作品实验室图标
    driver.assert_template(Template(r"tpl1602564218897.png", record_pos=(6.635, 5.005), resolution=(100, 100)), "作品后方显示实验室图标")
    #作品点击跳转
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/ul/li/div/div[2]/div[2]/a").click()
    driver.switch_to_new_tab()
    driver.assert_template(Template(r"tpl1604283773422.png", record_pos=(-0.404, -0.216), resolution=(1920, 1080)), "跳转到实验室")

    driver.close()#关闭标签
    driver.switch_to_previous_tab()
    #点击发布
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/ul/li/div/div[2]/div[2]/a[2]").click()
    #driver.assert_template(Template(r"tpl1602468483917.png", record_pos=(9.075, 0.755), resolution=(100, 100)), "不可发布作品提示不可发布")
    '''搜索框不输入'''
    driver.find_element_by_xpath("//input[@placeholder='请输入']").send_keys("")
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a/i").click()
        
    '''正常输入搜索'''
    find_element_by_xpath("//input[@placeholder='请输入']").send_keys("作品")
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/a/i").click()
        
    '''点击去创作'''
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/a").click()
    switch_to_new_tab()
    driver.assert_template(Template(r"tpl1601260517654.png", record_pos=(1.33, 0.445), resolution=(100, 100)), "界面跳转到创意实验室界面")
    driver.close()
    driver.switch_to_previous_tab()
        
    '''点击已发布作品'''
    driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div[2]/div/div/div[2]/div/div/div/div/div[2]/a/span").click()  
    
    driver.quit()
    
    return

try:
    main()
except:
    driver.quit()
    
    
    
    