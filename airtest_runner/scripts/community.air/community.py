# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
auto_setup(__file__)

import unittest
from selenium import *
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Community(unittest.TestCase):
    @classmethod
    def setUpClass(cls):    ##执行一次
        print("这是所有case的前置条件"+'\n')

    @classmethod
    def tearDownClass(cls):  ##执行一次
        print("这是所有case的后置条件"+'\n')
    '''前提条件'''
    def setUp(self):
        self.driver = WebChrome()
        self.driver.implicitly_wait(20)
        self.driver.get("https://coding.qq.com/")
        #进入首页并登录
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[10]/div[2]").click()
        self.driver.switch_to_previous_tab()
        self.driver.find_element_by_xpath("//a[@href='javascript:void(0);']").click()
        self.driver.find_element_by_id("login_btn_coding").click()
        self.driver.find_element_by_xpath("//input[@placeholder='请输入扣叮帐号（11位数字）']").send_keys("21488075035")
        self.driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("sijk83cr")
        self.driver.find_element_by_id("login_coding_btn").click()#点击登录
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/ul/li[6]/a").click()#进入社区
        return
    '''后置条件'''
    def tearDown(self):     
        self.driver.quit()       
        return
    '''轮播页'''
    #@unittest.skip('跳过')
    def test_01(self):
        #banana页3页轮播图片
        self.driver.assert_template(Template(r"tpl1602207127561.png", record_pos=(7.13, 2.325), resolution=(100, 100)), "第一张图片")
        self.driver.assert_template(Template(r"tpl1602207106319.png", record_pos=(7.795, 2.345), resolution=(100, 100)), "第二张图片")
        self.driver.assert_template(Template(r"tpl1602207146720.png", record_pos=(6.795, 2.32), resolution=(100, 100)), "第三张图片")
        #点击banana页图片
        self.driver.find_element_by_xpath("//img[@src='https://qgcdn0.gtimg.com/common_manage/2782/ImgUrl_fc92ec4fac16a5803e1e8e695f6943be.png']").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1602207414351.png", record_pos=(6.145, 3.36), resolution=(100, 100)), "跳转至对应链接")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        #点击banana页下方白色选择按钮
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/span").click()
        self.driver.assert_template(Template(r"tpl1602207127561.png", record_pos=(7.13, 2.325), resolution=(100, 100)), "第一张图片")
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/span[2]").click()
        self.driver.assert_template(Template(r"tpl1602207106319.png", record_pos=(7.795, 2.345), resolution=(100, 100)), "第二张图片")
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/span[3]").click()
        self.driver.assert_template(Template(r"tpl1602207146720.png", record_pos=(6.795, 2.32), resolution=(100, 100)), "第三张图片")
        
        sleep(30)
        



    '''实验室'''
    #@unittest.skip('跳过')
    def test_02(self):
        #创意实验室
        self.driver.assert_template(Template(r"tpl1601285915155.png", record_pos=(5.335, 5.915), resolution=(100, 100)), "显示实验室图片")

        self.driver.assert_template(Template(r"tpl1601285890439.png", rgb=True, record_pos=(3.79, 6.045), resolution=(100, 100)), "显示实验室在用人数")
        
        self.driver.find_element_by_xpath("//a[@href='/creative-lab']").click()
        self.driver.assert_template(Template(r"tpl1601286061822.png", record_pos=(10.095, 5.01), resolution=(100, 100)), "页面跳转至创意实验室")
        self.driver.back()
        #python实验室
        self.driver.assert_template(Template(r"tpl1601286211912.png", record_pos=(8.505, 5.91), resolution=(100, 100)), "显示实验室图片")
        self.driver.assert_template(Template(r"tpl1601286266354.png", rgb=True, record_pos=(7.005, 6.025), resolution=(100, 100)), "显示实验室在用人数")
        self.driver.find_element_by_xpath("//a[@href='/python-lab']").click()
        self.driver.assert_template(Template(r"tpl1601286371990.png", record_pos=(1.42, 0.455), resolution=(100, 100)), "页面跳转至python实验室")
        self.driver.back()
        #人工智能实验室
        self.driver.assert_template(Template(r"tpl1601287467885.png", record_pos=(11.62, 5.875), resolution=(100, 100)), "显示实验室图片")
        self.driver.assert_template(Template(r"tpl1601287482164.png", rgb=True, record_pos=(10.245, 6.025), resolution=(100, 100)), "显示实验室在用人数")
        self.driver.find_element_by_xpath("//a[@href='/ai-lab']").click()
        self.driver.assert_template(Template(r"tpl1601287569533.png", record_pos=(1.47, 0.45), resolution=(100, 100)), "页面跳转至人工智能实验室")
        self.driver.back()
        return
    
    '''作品-热门作品'''
    #@unittest.skip('跳过')
    def test_03(self):
        pass
    
    '''作品-热门作品-更多'''
    #@unittest.skip('跳过')
    def test_04(self):
        #点击更多
        self.driver.find_element_by_xpath("//a[@href='/community/all?type=0']").click()
        self.driver.assert_template(Template(r"tpl1601288417566.png", record_pos=(3.79, 1.615), resolution=(100, 100)), "页面进入全部作品界面")
        #点击全部实验室
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div").click()
        #点击python实验室
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/ul/li[2]/div").click()
        self.driver.assert_template(Template(r"tpl1601288586694.png", record_pos=(4.435, 2.255), resolution=(100, 100)), "筛选功能正常使用，筛选结果正确")
        #点击专题推荐
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div").click()
        #点击双人大战
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/ul/li/div").click()
        self.driver.assert_template(Template(r"tpl1601288722464.png", record_pos=(5.66, 2.255), resolution=(100, 100)), "筛选功能正常使用，筛选结果正确")
        #点击最热
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/a").click()
        #点击最新
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/a[2]").click()
        #点击最新
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div/div[2]/div/a").click()
        #点击作者名称
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div[2]/div/ul/li/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601289281514.png", record_pos=(3.59, 4.54), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.airtest_touch(Template(r"tpl1601289357814.png", target_pos=7, record_pos=(3.64, 4.785), resolution=(100, 100)))
        self.driver.switch_to_new_tab()

        self.driver.assert_template(Template(r"tpl1601289412092.png", record_pos=(12.33, 2.615), resolution=(100, 100)), "点击作品图片，进入作品页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.back()
        #向下翻页
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        #点击底部303
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div[3]/span[5]").click()
        self.driver.assert_template(Template(r"tpl1601290334816.png", rgb=True, record_pos=(10.47, 7.785), resolution=(100, 100)), "页面跳转至该页")
        #向上翻页
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_UP)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_UP)
        #点击搜索输入框并输入
        self.driver.find_element_by_xpath("//input[@placeholder='请输入搜索关键字']").send_keys("未命名")
        #按回车键
        self.driver.find_element_by_css_selector('body').send_keys(Keys.ENTER)   
        self.driver.assert_template(Template(r"tpl1601290742068.png", record_pos=(0.4, 5.3), resolution=(100, 100)), "作品列表显示包含改字的作品")
        #输入作品列表中名字不包含的字或其他     
        self.driver.find_element_by_xpath("//input[@placeholder='请输入搜索关键字']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='请输入搜索关键字']").send_keys("xxxxxxx")
        #按回车键
        self.driver.find_element_by_css_selector('body').send_keys(Keys.ENTER) 
        self.driver.assert_template(Template(r"tpl1601291282352.png", record_pos=(1.655, 3.85), resolution=(100, 100)), "作品列表空白显示")
        return
    
    '''作品-太空大冒险'''
    #@unittest.skip('跳过')
    def test_05(self):
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.assert_template(Template(r"tpl1601340912746.png", record_pos=(3.66, 5.625), resolution=(100, 100)), "太空大冒险模块")
        #鼠标移动到作品图片上
        a = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[6]/div[2]/div/div/div[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(a).perform()
        #截图
        self.driver.snapshot()
        sleep(3)
        #点击作者名称或头像
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div[6]/div[2]/div/div/div/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601341374112.png", record_pos=(0.67, 4.555), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.assert_template(Template(r"tpl1601341481973.png", record_pos=(9.03, 3.755), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.back()
        
        #点击作品图片，进入作品页面
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_xpath("//img[@src='https://p.qpic.cn/qqgameedu/0/774466d9bd2e960b160e6010a4e8456b/0']").click()
        
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601341761552.png", record_pos=(12.38, 2.615), resolution=(100, 100)), "点击作品图片，进入作品页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        return
    
    
    '''作品-伙伴帮帮忙'''
    #@unittest.skip('跳过')
    def test_06(self):
        #向下翻页3次
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        
        #查看伙伴帮帮忙模块
        self.driver.assert_template(Template(r"tpl1601342191423.png", record_pos=(3.49, 1.21), resolution=(100, 100)), "伙伴帮帮忙模块显示正常")
        #鼠标移动到作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[7]/div[2]/div/div/div[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #截图
        self.driver.snapshot()
        sleep(3)
        #点击作者名称或头像，进入该作者详情页
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div[7]/div[2]/div/div/div/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601342517596.png", record_pos=(3.565, 4.54), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.assert_template(Template(r"tpl1601342545406.png", record_pos=(9.045, 3.77), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        
        #点击作品图片，进入作品页面
        self.driver.find_element_by_xpath("//img[@src='https://p.qpic.cn/qqgameedu/0/1106e5bbcf7bfc4622823fa4770f3407/0']").click()
        self.driver.switch_to_new_tab()

        self.driver.assert_template(Template(r"tpl1601342636489.png", record_pos=(12.365, 2.57), resolution=(100, 100)), "点击作品图片，进入作品页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.back()
        return

    '''作品-反应大挑战2'''
    #@unittest.skip('跳过')
    def test_07(self):
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        #查看反应大挑战2模块
        self.driver.assert_template(Template(r"tpl1601343158429.png", record_pos=(3.53, 5.25), resolution=(100, 100)), "反应大挑战2模块显示正常")
        #鼠标移动到作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[8]/div[2]/div/div/div[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #截图
        self.driver.snapshot()
        sleep(3)
        #点击作者名称或头像，进入该作者详情页
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div[8]/div[2]/div/div/div/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601343379686.png", record_pos=(3.57, 4.55), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.assert_template(Template(r"tpl1601343408897.png", record_pos=(5.27, 3.705), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        #点击作品图片，进入作品页面
        self.driver.find_element_by_xpath("//img[@src='https://p.qpic.cn/qqgameedu/0/0108bd4c8a047e71dcf0befe04d09c7e_0/0']").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601343521209.png", record_pos=(12.345, 2.57), resolution=(100, 100)), "点击作品图片，进入作品页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.back()     
        return
    
    '''作品-反应大挑战'''
    #@unittest.skip('跳过')
    def test_08(self):
        #向下翻页
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        #查看反应大挑战模块
        self.driver.assert_template(Template(r"tpl1601343868514.png", record_pos=(3.515, 0.79), resolution=(100, 100)), "反应大挑战模块显示正常")
        #鼠标移动到作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[9]/div[2]/div/div/div[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #截图
        self.driver.snapshot()
        sleep(3)
        #点击作者名称或头像，进入该作者详情页
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div[9]/div[2]/div/div/div/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601344143386.png", record_pos=(0.68, 4.555), resolution=(100, 100)), "进入该作者详情页")
        self.driver.assert_template(Template(r"tpl1601344173089.png", record_pos=(2.39, 3.705), resolution=(100, 100)), "进入该作者详情页")
        #点击作品图片，进入作品页面
        self.driver.find_element_by_xpath("//img[@src='https://p.qpic.cn/qqgameedu/0/017c29c9d27485f49efbd0973632f2b4/0']").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601344270945.png", record_pos=(12.375, 2.625), resolution=(100, 100)), "进入该作者详情页")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.back()  
        return
    
    '''作品-极速飙车'''
    #@unittest.skip('跳过')
    def test_09(self):
        #向下翻页
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.assert_template(Template(r"tpl1601345011724.png", record_pos=(3.37, 4.815), resolution=(100, 100)), "极速飙车模块显示正常")
        #鼠标移动到作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[10]/div[2]/div/div/div[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #截图
        self.driver.snapshot()
        sleep(3)
        #点击作者名称或头像，进入该作者详情页
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div/div[10]/div[2]/div/div/div/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601345185109.png", record_pos=(3.535, 4.525), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.assert_template(Template(r"tpl1601345212736.png", record_pos=(8.98, 3.565), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        #点击作品图片，进入作品页面
        self.driver.find_element_by_xpath("//img[@src='https://p.qpic.cn/qqgameedu/0/e619d5a1a80e3eb1194af7a176acc60e/0']").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601345307591.png", record_pos=(12.365, 2.6), resolution=(100, 100)), "点击作品图片，进入作品页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.back() 
        return
    
    '''作品-反应大挑战'''
    #@unittest.skip('跳过')
    def test_10(self):
        #向下翻页
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.assert_template(Template(r"tpl1601345819375.png", record_pos=(3.545, 0.41), resolution=(100, 100)), "反应大挑战模块显示正常")
        #鼠标移动到作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[11]/div[2]/div/div/div[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #截图
        self.driver.snapshot()
        sleep(3)
        #点击作者名称或头像，进入该作者详情页
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[11]/div[2]/div/div/div[1]/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601345185109.png", record_pos=(3.535, 4.525), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.assert_template(Template(r"tpl1601346440018.png", record_pos=(9.005, 3.59), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        #点击作品图片，进入作品页面
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/ul/li/div/div[1]/a/img").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601345307591.png", record_pos=(12.365, 2.6), resolution=(100, 100)), "点击作品图片，进入作品页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.back() 
        return
    
    '''作品-我们爱运动'''
    #@unittest.skip('跳过')
    def test_11(self):
        #向下翻页
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.assert_template(Template(r"tpl1601346745045.png", record_pos=(3.51, 4.42), resolution=(100, 100)), "我们爱运动模块显示正常")
        #鼠标移动到作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[12]/div[2]/div/div/div[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #截图
        self.driver.snapshot()
        sleep(3)
        #点击作者名称或头像，进入该作者详情页
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[12]/div[2]/div/div/div[1]/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601345185109.png", record_pos=(3.535, 4.525), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.assert_template(Template(r"tpl1601347029068.png", record_pos=(8.995, 3.545), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        #点击作品图片，进入作品页面
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/ul/li/div/div[1]/a/img").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601345307591.png", record_pos=(12.365, 2.6), resolution=(100, 100)), "点击作品图片，进入作品页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.back() 
        return
    
    '''作品-双人大挑战'''
    #@unittest.skip('跳过')
    def test_12(self):
        #向下翻页
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.assert_template(Template(r"tpl1601347203404.png", record_pos=(3.455, 6.105), resolution=(100, 100)), "双人大挑战模块显示正常")
        #鼠标移动到作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[4]/div[2]/div/div/div[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #截图
        self.driver.snapshot()
        sleep(3)
        #点击作者名称或头像，进入该作者详情页
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[4]/div[2]/div/div/div[1]/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601345185109.png", record_pos=(3.535, 4.525), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.assert_template(Template(r"tpl1601347307069.png", record_pos=(6.2, 3.645), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        #点击作品图片，进入作品页面
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/div/div[1]/a/img").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601345307591.png", record_pos=(12.365, 2.6), resolution=(100, 100)), "点击作品图片，进入作品页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.back()
        return
    
    '''作品-保卫战'''
    #@unittest.skip('跳过')
    def test_13(self):
        #向下翻页
        for i in range(6):
            self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.assert_template(Template(r"tpl1601347588494.png", record_pos=(3.29, 4.02), resolution=(100, 100)), "保卫战模块显示正常")
        #鼠标移动到作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[14]/div[2]/div/div/div[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #截图
        self.driver.snapshot()
        sleep(3)
        #点击作者名称或头像，进入该作者详情页
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[14]/div[2]/div/div/div[1]/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601345185109.png", record_pos=(3.535, 4.525), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.assert_template(Template(r"tpl1601347691451.png", record_pos=(6.16, 3.625), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        #点击作品图片，进入作品页面
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/div/div[1]/a/img").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601345307591.png", record_pos=(12.365, 2.6), resolution=(100, 100)), "点击作品图片，进入作品页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.back()
        return
    
    '''作品-海底大冒险'''
    #@unittest.skip('跳过')
    def test_14(self):
        #向下翻页
        for i in range(7):
            self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.assert_template(Template(r"tpl1601347974708.png", record_pos=(3.475, 2.58), resolution=(100, 100)), "海底大冒险模块显示正常")
        #鼠标移动到作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[15]/div[2]/div/div/div[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #截图
        self.driver.snapshot()
        sleep(3)
        #点击作者名称或头像，进入该作者详情页
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[15]/div[2]/div/div/div[1]/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601345185109.png", record_pos=(3.535, 4.525), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.assert_template(Template(r"tpl1601348060139.png", record_pos=(6.05, 3.625), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        #点击作品图片，进入作品页面
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/div/div[1]/a/img").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601345307591.png", record_pos=(12.365, 2.6), resolution=(100, 100)), "点击作品图片，进入作品页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.back()
        return
    
    '''作品-天天爱消除'''
    #@unittest.skip('跳过')
    def test_15(self):
        #向下翻页
        for i in range(7):
            self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.assert_template(Template(r"tpl1601348317530.png", record_pos=(3.51, 3.625), resolution=(100, 100)), "天天爱消除模块显示正常")
        #鼠标移动到作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[16]/div[2]/div/div/div[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #截图
        self.driver.snapshot()
        sleep(3)
        #点击作者名称或头像，进入该作者详情页
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[16]/div[2]/div/div/div[1]/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601345185109.png", record_pos=(3.535, 4.525), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.assert_template(Template(r"tpl1601348424486.png", record_pos=(6.115, 3.615), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        #点击作品图片，进入作品页面
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/ul/li/div/div[1]/a/img").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601345307591.png", record_pos=(12.365, 2.6), resolution=(100, 100)), "点击作品图片，进入作品页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.back()
        return
    
    '''作品-家园保卫战'''
    #@unittest.skip('跳过')
    def test_16(self):
        #向下翻页
        for i in range(8):
            self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.assert_template(Template(r"tpl1601348906386.png", record_pos=(0.585, 4.545), resolution=(100, 100)), "家园保卫战模块显示正常")
        #鼠标移动到作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[17]/div[2]/div/div/div[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #截图
        self.driver.snapshot()
        sleep(3)
        #点击作者名称或头像，进入该作者详情页
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[1]/div[17]/div[2]/div/div/div[1]/div/div[3]/p/a").click()
        self.driver.assert_template(Template(r"tpl1601345185109.png", record_pos=(3.535, 4.525), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        self.driver.assert_template(Template(r"tpl1601348817506.png", record_pos=(6.11, 3.625), resolution=(100, 100)), "点击作者名称或头像，进入该作者详情页")
        #点击作品图片，进入作品页面
        self.driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div/ul/li/div/div[1]/a/img").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601345307591.png", record_pos=(12.365, 2.6), resolution=(100, 100)), "点击作品图片，进入作品页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.back()
        return
    
    '''个人简介'''
    #@unittest.skip('跳过')
    def test_17(self):
        self.driver.assert_template(Template(r"tpl1601349171160.png", record_pos=(13.92, 3.365), resolution=(100, 100)), "显示获赞数，显示作品数，显示个人头像，名称无误")
        return
    
    '''小小编程家'''
    #@unittest.skip('跳过')
    def test_18(self):
        self.driver.assert_template(Template(r"tpl1601349318096.png", record_pos=(13.94, 5.515), resolution=(100, 100)), "显示作者名称，头像，作品数，获赞数无误")
        self.driver.assert_template(Template(r"tpl1601349343326.png", record_pos=(13.78, 6.455), resolution=(100, 100)), "显示作者名称，头像，作品数，获赞数无误")
        self.driver.assert_template(Template(r"tpl1601349351231.png", record_pos=(14.355, 6.48), resolution=(100, 100)), "显示作者名称，头像，作品数，获赞数无误")
        #点击作者头像或名称
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/ul/li/div/div/p/a").click()
        self.driver.assert_template(Template(r"tpl1601349494849.png", record_pos=(3.51, 4.53), resolution=(100, 100)), "页面进入作者详情页")
        self.driver.assert_template(Template(r"tpl1601349507991.png", record_pos=(9.015, 3.64), resolution=(100, 100)), "页面进入作者详情页")
        return
    
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Community))
runner = unittest.TextTestRunner()
runner.run(suite)




