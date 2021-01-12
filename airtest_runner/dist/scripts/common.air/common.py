# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
from airtest_selenium.proxy import WebChrome
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


'''通用函数'''
class common():
    '''进入网页不登录'''
    def enter():
        driver = WebChrome()
        driver.implicitly_wait(20)
        driver.get("https://coding.qq.com/")
        #进入首页
        driver.maximize_window()
        #driver.find_element_by_xpath("//*[@id=/app/]/div/div[2]/div[11]/div[2]/div/div[6]").click()
        driver.airtest_touch(Template(r"tpl1604280812644.png", record_pos=(-0.026, 0.176), resolution=(1920, 1080)))
        driver.switch_to_previous_tab()
        return driver
    
    '''进入网页并登录'''
    def login():
        driver = WebChrome()
        driver.implicitly_wait(20)
        driver.get("https://coding.qq.com/")
        #进入首页并登录
        driver.maximize_window()
        #driver.find_element_by_xpath("//*[@id=/app/]/div/div[2]/div[11]/div[2]/div/div[6]").click()
        driver.airtest_touch(Template(r"tpl1604280812644.png", record_pos=(-0.026, 0.176), resolution=(1920, 1080)))

        
        driver.switch_to_previous_tab()
        driver.find_element_by_xpath("//a[@href='javascript:void(0);']").click()
        driver.find_element_by_id("login_btn_coding").click()
        driver.find_element_by_xpath("//input[@placeholder='请输入扣叮帐号（11位数字）']").send_keys("21488075035")
        driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("sijk83cr")
        driver.find_element_by_id("login_coding_btn").click()       
        return driver
    
    '''进入网页登录后进入个人中心'''
    def enter_personalCenter():
        driver = common.login()#进入网页并登录
        button = driver.find_element_by_xpath("//*[@id='app']/div/div[1]/div/div[2]/div[2]/div/div/img")
        ActionChains(driver).move_to_element(button).perform()#移动鼠标到指定位置

        #进入个人中心
        driver.find_element_by_link_text("个人中心").click()
        driver.switch_to_new_tab()
        driver.assert_template(Template(r"tpl1601191280964.png", record_pos=(3.695, 4.235), resolution=(100, 100)), "页面跳转至个人中心界面")
        return driver


    '''该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false'''
    def isElementExist(element):
        flag=True
        try:
            driver.find_element_by_css_selector(element)
            return flag
        
        except:
            flag=False
            return flag
        
    def verification_code():
        common.login()#进入网页并登录
        return



    
    
        


        
    
    
    
    
