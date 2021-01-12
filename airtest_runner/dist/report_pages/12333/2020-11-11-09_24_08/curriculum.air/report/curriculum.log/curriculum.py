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


'''课程'''
class course(unittest.TestCase):
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
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div/div/ul/li[3]/a").click()#点击课程

    '''后置条件'''
    def tearDown(self):     
        self.driver.quit()       
        return
    
    
    '''轮播页'''
    #@unittest.skip('跳过')
    def test_01(self):
        #查看轮播页
        self.driver.assert_template(Template(r"tpl1601432407434.png", record_pos=(9.17, 3.58), resolution=(100, 100)), "banana页轮播图图片")
        self.driver.assert_template(Template(r"tpl1601432430820.png", record_pos=(9.14, 3.115), resolution=(100, 100)), "banana页轮播图图片")
        #点击下方‘专注6-18岁青少年计算思维培养’
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div[2]/ul/li[2]/a").click()
        self.driver.assert_template(Template(r"tpl1601432430820.png", record_pos=(9.14, 3.115), resolution=(100, 100)), "banana播放‘专注6-18岁青少年计算思维培养’对应图片")
        #点击下方‘Fun Coding编程课’
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div[2]/ul/li/a").click()
        self.driver.assert_template(Template(r"tpl1601432407434.png", record_pos=(9.17, 3.58), resolution=(100, 100)), "banana播放‘Fun Coding编程课’对应图片")
        #点击轮播页‘Fun Coding编程课’
        self.driver.find_element_by_xpath("//img[@src='https://wuji-30130.sz.gfp.tencent-cloud.com/pics/20200728_dyu9l1b62u0.png']").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601432830428.png", record_pos=(9.11, 1.85), resolution=(100, 100)), "跳转至对应链接")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        return
    
    '''热门推荐'''
    #@unittest.skip('跳过')
    def test_02(self):
        # 向下滚动600个像素
        self.driver.execute_script('window.scrollBy(0,600)')
        '''检查作品显示数量'''
        # 定位到ul，并获得ul中所有得li元素
        menu_ul = self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div[2]/div/ul")
        rows = menu_ul.find_elements_by_tag_name('li')
        # python的len()函数返回对象（字符、列表、元组）的长度或者元素的个数
        before_add_numbers = len(rows)
        if before_add_numbers == 8:
            print('显示8个作品图片')
        #点击‘1-3年级’
        self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div/div/div/div[2]/a/span").click()
        self.driver.assert_template(Template(r"tpl1601436265472.png", record_pos=(3.53, 4.625), resolution=(100, 100)), "下方作品展示1-3年级对应的作品")
        self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div/div/div/div[3]/a/span").click()
        self.driver.assert_template(Template(r"tpl1601436318081.png", record_pos=(6.565, 4.63), resolution=(100, 100)), "下方作品展示4-6年级对应的作品")
        #点击作品图片
        self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div[2]/div/ul/li/div/div/a/img").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601436410181.png", record_pos=(4.585, 3.415), resolution=(100, 100)), "直接跳转到作品，显示课程内容，相关系列课")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        #点击热门推荐下的作品名称
        self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div[2]/div/ul/li/div/div[2]/p/a").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601436569738.png", record_pos=(8.26, 2.05), resolution=(100, 100)), "跳转到作品详情界面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        #点击作品图片的工作室
        self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div[2]/div/ul/li/div/div[2]/div[2]/p/a").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601436702630.png", record_pos=(9.005, 3.43), resolution=(100, 100)), "跳转到名师团该工作室")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        #鼠标移动到学过作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div[2]/div/ul/li[1]/div")
        ActionChains(self.driver).move_to_element(pic).perform()
        #收藏
        self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div[2]/div/ul/li/div/div[2]/div[3]/a[2]").click()
        sleep(3)
        #取消收藏
        self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div[2]/div/ul/li[1]/div/div[2]/div[3]/a[2]").click()
        self.driver.assert_template(Template(r"tpl1601437540321.png", record_pos=(0.705, 5.97), resolution=(100, 100)), "学习过的作品显示继续学习按钮")
        self.driver.assert_template(Template(r"tpl1601437751929.png", record_pos=(0.635, 3.01), resolution=(100, 100)), "已经学习过的作品图片上方显示正在学习")

        #鼠标移动到未学过作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div[2]/div/ul/li[2]/div")
        ActionChains(self.driver).move_to_element(pic).perform()
        self.driver.assert_template(Template(r"tpl1601437708850.png", record_pos=(3.845, 5.31), resolution=(100, 100)), "未学习过的作品显示立即学习")
        #点击不限年龄
        self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div/div/div/div/a/span").click()
        # 向下滚动300个像素
        self.driver.execute_script('window.scrollBy(0,300)')
        #点击展开全部
        self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[3]/a").click()
        # 定位到ul，并获得ul中所有得li元素
        menu_ul = self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div[2]/div/ul")
        rows = menu_ul.find_elements_by_tag_name('li')
        # python的len()函数返回对象（字符、列表、元组）的长度或者元素的个数
        before_add_numbers = len(rows)
        if before_add_numbers != 8:
            print('展示所有作品')
            self.driver.assert_template(Template(r"tpl1601438539382.png", record_pos=(6.18, 7.505), resolution=(100, 100)), "展示所有作品")

        #点击收起
        self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[3]/a").click()
        # 定位到ul，并获得ul中所有得li元素
        menu_ul = self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div[2]/div/ul")
        rows = menu_ul.find_elements_by_tag_name('li')
        # python的len()函数返回对象（字符、列表、元组）的长度或者元素的个数
        before_add_numbers = len(rows)
        if before_add_numbers == 8:
            print('收起成功')
            self.driver.assert_template(Template(r"tpl1601438514554.png", record_pos=(6.16, 7.525), resolution=(100, 100)), "收起成功")
        return
    
    
    '''入门体验'''
    #@unittest.skip('跳过')
    def test_03(self):
        # 滚动至‘入门体验’元素可见位置
        ele = self.driver.find_element_by_xpath("//*[@id=\"introduction\"]/div/div/div/h2")
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        sleep(3)
        # 定位到ul，并获得ul中所有得li元素
        menu_ul = self.driver.find_element_by_xpath("//*[@id=\"introduction\"]/div/div/div[2]/div/div/ul")
        rows = menu_ul.find_elements_by_tag_name('li')
        before_add_numbers = len(rows)
        if before_add_numbers == 8:
            print('显示8个作品图片')
        #点击作品图片
        self.driver.find_element_by_xpath("//img[@src='https://p.qpic.cn/qqgameedu/0/06faf49904214626482171f856ba01f4/0']").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601446652499.png", record_pos=(0.85, 3.435), resolution=(100, 100)), "直接跳转到作品")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        #点击热门推荐下的作品名称
        self.driver.find_element_by_xpath("//a[@href='/lesson/course-single/1363']").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601446802967.png", record_pos=(3.88, 5.555), resolution=(100, 100)), "跳转到作品详情界面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        #防止鼠标影响元素的显示，把鼠标移开
        pic = self.driver.find_element_by_xpath("//*[@id=\"introduction\"]/div/div/div[2]/div/div/ul/li[2]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #点击作品图片的工作室
        self.driver.find_element_by_xpath("//*[@id=\"introduction\"]/div/div/div[2]/div/div/ul/li/div/div[2]/div[2]/p/a").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601446884324.png", record_pos=(6.665, 1.82), resolution=(100, 100)), "跳转到名师团该工作详情界面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        #鼠标移动到作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id=\"introduction\"]/div/div/div[2]/div/div/ul/li[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        #点击收藏
        self.driver.find_element_by_xpath("//*[@id=\"introduction\"]/div/div/div[2]/div/div/ul/li[1]/div/div[2]/div[3]/a[2]").click()    
        sleep(3)
        #取消收藏
        ActionChains(self.driver).move_to_element(pic).perform()
        self.driver.find_element_by_xpath("//*[@id=\"introduction\"]/div/div/div[2]/div/div/ul/li[1]/div/div[2]/div[3]/a[2]").click()
        self.driver.assert_template(Template(r"tpl1601437540321.png", record_pos=(0.705, 5.97), resolution=(100, 100)), "学习过的作品显示继续学习按钮")
        self.driver.assert_template(Template(r"tpl1601437751929.png", record_pos=(0.635, 3.01), resolution=(100, 100)), "已经学习过的作品图片上方显示正在学习")

        #鼠标移动到未学过作品图片上
        pic = self.driver.find_element_by_xpath("//*[@id=\"introduction\"]/div/div/div[2]/div/div/ul/li[8]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform()
        self.driver.assert_template(Template(r"tpl1601437708850.png", record_pos=(3.845, 5.31), resolution=(100, 100)), "未学习过的作品显示立即学习")
        
        return
    
    '''系列编程课'''
    #@unittest.skip('跳过')
    def test_04(self):
        # 滚动至‘更多主题编程课’元素可见位置
        ele = self.driver.find_element_by_xpath("//*[@id=\"series\"]/div/div/div[1]/h2")
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        sleep(3)
        # 定位到ul，并获得ul中所有得li元素
        menu_ul = self.driver.find_element_by_xpath("//*[@id=\"series\"]/div/div/div[2]/div/div/ul")
        rows = menu_ul.find_elements_by_tag_name('li')
        before_add_numbers = len(rows)
        if before_add_numbers == 6:
            print('显示6个作品图片')
        #鼠标移动到系列课图片上
        pic = self.driver.find_element_by_xpath("//*[@id=\"series\"]/div/div/div[2]/div/div/ul/li[1]/div")
        ActionChains(self.driver).move_to_element(pic).perform() 
        self.driver.assert_template(Template(r"tpl1601452449355.png", record_pos=(2.92, 2.51), resolution=(100, 100)), "出现该课程简介")
        #点击系列课名称或图片
        self.driver.find_element_by_xpath("//img[@src='https://p.qpic.cn/qqgameedu/0/c051068d1f5343d8f93430a8a2ab189e/0']").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601452577413.png", record_pos=(4.205, 2.675), resolution=(100, 100)), "界面跳转至该课程详情页")
        self.driver.assert_template(Template(r"tpl1601452610718.png", record_pos=(3.865, 7.96), resolution=(100, 100)), "展示课程目录")
        # 向下滚动300个像素
        self.driver.execute_script('window.scrollBy(0,300)')
        #点击课程目录展示的课程
        self.driver.find_element_by_xpath("//img[@src='https://p.qpic.cn/qqgameedu/0/9c408b3162555c3a7adb98c11d9724db/0']").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601452829679.png", record_pos=(0.835, 1.51), resolution=(100, 100)), "跳转到该课程")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        #鼠标移动到系列课图片上
        ActionChains(self.driver).move_to_element(pic).perform() 
        #点击收藏
        self.driver.find_element_by_xpath("//*[@id=\"series\"]/div/div/div[2]/div/div/ul/li[1]/div/div[2]/div[3]/a").click()
        #取消收藏
        ActionChains(self.driver).move_to_element(pic).perform()
        self.driver.find_element_by_xpath("//*[@id=\"series\"]/div/div/div[2]/div/div/ul/li[1]/div/div[2]/div[3]/a").click()
        #向下滚动300个像素
        self.driver.execute_script('window.scrollBy(0,300)')
        #点击展开全部
        self.driver.find_element_by_xpath("//*[@id=\"series\"]/div/div/div[3]/a").click()
        # 定位到ul，并获得ul中所有得li元素
        menu_ul = self.driver.find_element_by_xpath("//*[@id=\"series\"]/div/div/div[2]/div/div/ul")
        rows = menu_ul.find_elements_by_tag_name('li')
        before_add_numbers = len(rows)
        if before_add_numbers == 11:
            print('展开全部')
        self.driver.assert_template(Template(r"tpl1601453475306.png", record_pos=(5.825, 7.135), resolution=(100, 100)), "展开全部")
        #点击收起
        self.driver.find_element_by_xpath("//*[@id=\"series\"]/div/div/div[3]/a").click()
        # 定位到ul，并获得ul中所有得li元素
        menu_ul = self.driver.find_element_by_xpath("//*[@id=\"series\"]/div/div/div[2]/div/div/ul")
        rows = menu_ul.find_elements_by_tag_name('li')
        before_add_numbers = len(rows)
        if before_add_numbers == 6:
            print('已收起')
        self.driver.assert_template(Template(r"tpl1601453597065.png", record_pos=(5.755, 7.15), resolution=(100, 100)), "已收起") 
        return
    
    '''知识小课堂'''
    #@unittest.skip('跳过')
    def test_05(self):
        # 滚动至‘知识小课堂’元素可见位置
        ele = self.driver.find_element_by_xpath("//*[@id=\"basic\"]/div/div/div[1]/h2")
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        sleep(3)
        # 定位到ul，并获得ul中所有得li元素
        menu_ul = self.driver.find_element_by_xpath("//*[@id=\"basic\"]/div/div/div[2]/div/div/ul")
        rows = menu_ul.find_elements_by_tag_name('li')
        before_add_numbers = len(rows)
        if before_add_numbers == 6:
            print('显示6个作品图片')
        #鼠标移动到系列课图片上
        pic = self.driver.find_element_by_xpath("//*[@id=\"basic\"]/div/div/div[2]/div/div/ul/li[1]/div/div[1]/a/img")
        ActionChains(self.driver).move_to_element(pic).perform() 
        self.driver.assert_template(Template(r"tpl1601455103464.png", record_pos=(0.775, 2.91), resolution=(100, 100)), "出现该课程简介")
        #点击系列课名称或图片
        self.driver.find_element_by_xpath("//*[@id=\"basic\"]/div/div/div[2]/div/div/ul/li/div/div[2]/p/a").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601454241524.png", record_pos=(8.325, 2.22), resolution=(100, 100)), "界面跳转至该课程详情页")
        self.driver.assert_template(Template(r"tpl1601454280260.png", record_pos=(3.94, 5.495), resolution=(100, 100)), "展示课程内容")
        #点击课程目录展示的课程
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[2]/div/div/div[2]/div/ul/li/a").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601454402235.png", record_pos=(0.53, 1.025), resolution=(100, 100)), "跳转到该课程")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()
        #鼠标移动到系列课图片上
        ActionChains(self.driver).move_to_element(pic).perform() 
        #点击收藏
        self.driver.find_element_by_xpath("//*[@id=\"basic\"]/div/div/div[2]/div/div/ul/li[1]/div/div[2]/div[3]/a[2]").click()
        #取消收藏
        ActionChains(self.driver).move_to_element(pic).perform()
        self.driver.find_element_by_xpath("//*[@id=\"basic\"]/div/div/div[2]/div/div/ul/li[1]/div/div[2]/div[3]/a[2]").click()
        #向下滚动300个像素
        self.driver.execute_script('window.scrollBy(0,300)')
        #点击展开全部
        self.driver.find_element_by_xpath("//*[@id=\"basic\"]/div/div/div[3]/a").click()
        # 定位到ul，并获得ul中所有得li元素
        menu_ul = self.driver.find_element_by_xpath("//*[@id=\"basic\"]/div/div/div[2]/div/div/ul")
        rows = menu_ul.find_elements_by_tag_name('li')
        before_add_numbers = len(rows)
        if before_add_numbers == 12:
            print('已展开全部')
        self.driver.assert_template(Template(r"tpl1601453475306.png", record_pos=(5.825, 7.135), resolution=(100, 100)), "已展开全部")
        #点击收起
        self.driver.find_element_by_xpath("//*[@id=\"basic\"]/div/div/div[3]/a").click()
        # 定位到ul，并获得ul中所有得li元素
        menu_ul = self.driver.find_element_by_xpath("//*[@id=\"basic\"]/div/div/div[2]/div/div/ul")
        rows = menu_ul.find_elements_by_tag_name('li')
        before_add_numbers = len(rows)
        if before_add_numbers == 6:
            print('已收起')
        self.driver.assert_template(Template(r"tpl1601453597065.png", record_pos=(5.755, 7.15), resolution=(100, 100)), "已收起") 
        return
    
    '''CodingDay主题课程'''
    #@unittest.skip('跳过')
    def test_06(self):
        # 滚动至‘CodingDay主题课程’元素可见位置
        ele = self.driver.find_element_by_xpath("//*[@id=\"theme\"]/div/div/div[1]/h2")
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        sleep(3)
        self.driver.assert_template(Template(r"tpl1601455688715.png", record_pos=(2.73, 2.03), resolution=(100, 100)), "名称，简介，地点显示正常")
        #鼠标移动到图片上
        pic = self.driver.find_element_by_xpath("//*[@id=\"theme\"]/div/div/div[2]/div/ul/li[1]/div/a")
        ActionChains(self.driver).move_to_element(pic).perform() 
        self.driver.assert_template(Template(r"tpl1601455823132.png", record_pos=(0.395, 3.04), resolution=(100, 100)), "显示地点位置出现‘查看详情’")
        #点击图片
        self.driver.find_element_by_xpath("//a[@href='https://coding.qq.com/coding-day/detail?id=9']").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601455993273.png", record_pos=(7.875, 1.97), resolution=(100, 100)), "跳转至该课程详情页")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()  
        return  
    
    
    '''我要开课-信息填写正确'''
    #@unittest.skip('跳过')
    def test_07(self):
        # 滚动至‘我要开课’元素可见位置
        ele = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[12]/div/div")
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        sleep(3)
        self.driver.assert_template(Template(r"tpl1601456409488.png", record_pos=(1.21, 5.475), resolution=(100, 100)), "显示名称")
        self.driver.assert_template(Template(r"tpl1601456418869.png", record_pos=(2.635, 5.91), resolution=(100, 100)), "显示简介")
        self.driver.assert_template(Template(r"tpl1601456426728.png", record_pos=(1.325, 6.495), resolution=(100, 100)), "显示申请入住按钮")
        #点击申请入住
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[12]/div/div/div/div/a").click()
        self.driver.assert_template(Template(r"tpl1601456532959.png", record_pos=(5.815, 3.265), resolution=(100, 100)), "弹出弹窗")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写姓名']").send_keys("哼哼")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写所属机构或学校名称']").send_keys("哈哈")
        self.driver.find_element_by_xpath("//input[@placeholder='请输入团队的人数']").send_keys("12")
        self.driver.find_element_by_xpath("//textarea[@placeholder='请填写个人的介绍']").send_keys("你好！")
        #点击下一步
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/a").click()
        self.driver.assert_template(Template(r"tpl1601456726201.png", rgb=True, record_pos=(5.775, 3.275), resolution=(100, 100)), "擅长教学方向")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写擅长的编程语言']").send_keys("python")
        self.driver.find_element_by_xpath("//textarea[@placeholder='请填写擅长的课程主题或方向']").send_keys("自动化测试")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写擅长的课程所覆盖的学生年龄范围']").send_keys("大于18")
        #点击下一步
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/a[2]").click()
        self.driver.assert_template(Template(r"tpl1601456897449.png", record_pos=(7.35, 3.29), resolution=(100, 100)), "联系方式")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写正确的电子邮箱']").send_keys("123456@qq.com")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写正确的手机号']").send_keys("123456")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写正确的微信号']").send_keys("654321")
        #点击同意注册协议
        self.driver.find_element_by_xpath("//label[@title='同意']").click()
        #点击提交申请
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/a[2]").click()
        self.driver.assert_template(Template(r"tpl1601457088187.png", record_pos=(5.76, 4.055), resolution=(100, 100)), "提交成功")
        #点击’我知道了‘
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[3]/div/a").click()
        
        return
    
    '''我要开课-基本信息不全'''
    #@unittest.skip('跳过')
    def test_08(self):
        # 滚动至‘我要开课’元素可见位置
        ele = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[12]/div/div")
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        sleep(3)
        self.driver.assert_template(Template(r"tpl1601456409488.png", record_pos=(1.21, 5.475), resolution=(100, 100)), "显示名称")
        self.driver.assert_template(Template(r"tpl1601456418869.png", record_pos=(2.635, 5.91), resolution=(100, 100)), "显示简介")
        self.driver.assert_template(Template(r"tpl1601456426728.png", record_pos=(1.325, 6.495), resolution=(100, 100)), "显示申请入住按钮")
        #点击申请入住
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[12]/div/div/div/div/a").click()
        self.driver.assert_template(Template(r"tpl1601456532959.png", record_pos=(5.815, 3.265), resolution=(100, 100)), "弹出弹窗")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写姓名']").send_keys("")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写所属机构或学校名称']").send_keys("哈哈")
        self.driver.find_element_by_xpath("//input[@placeholder='请输入团队的人数']").send_keys("12")
        self.driver.find_element_by_xpath("//textarea[@placeholder='请填写个人的介绍']").send_keys("你好！")
        #点击下一步
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/a").click()
        self.driver.assert_template(Template(r"tpl1601456726201.png", rgb=True, record_pos=(5.775, 3.275), resolution=(100, 100)), "擅长教学方向")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写擅长的编程语言']").send_keys("python")
        self.driver.find_element_by_xpath("//textarea[@placeholder='请填写擅长的课程主题或方向']").send_keys("自动化测试")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写擅长的课程所覆盖的学生年龄范围']").send_keys("大于18")
        #点击下一步
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/a[2]").click()
        self.driver.assert_template(Template(r"tpl1601456897449.png", record_pos=(7.35, 3.29), resolution=(100, 100)), "联系方式")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写正确的电子邮箱']").send_keys("123456@qq.com")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写正确的手机号']").send_keys("123456")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写正确的微信号']").send_keys("654321")
        #点击同意注册协议
        self.driver.find_element_by_xpath("//label[@title='同意']").click()
        #点击提交申请
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/a[2]").click()
        self.driver.assert_template(Template(r"tpl1601457678122.png", record_pos=(7.65, 7.165), resolution=(100, 100)), "不可提交")

        
        return  
    '''我要开课-擅长教学方向不全'''
    #@unittest.skip('跳过')
    def test_09(self):
        # 滚动至‘我要开课’元素可见位置
        ele = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[12]/div/div")
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        sleep(3)
        self.driver.assert_template(Template(r"tpl1601456409488.png", record_pos=(1.21, 5.475), resolution=(100, 100)), "显示名称")
        self.driver.assert_template(Template(r"tpl1601456418869.png", record_pos=(2.635, 5.91), resolution=(100, 100)), "显示简介")
        self.driver.assert_template(Template(r"tpl1601456426728.png", record_pos=(1.325, 6.495), resolution=(100, 100)), "显示申请入住按钮")
        #点击申请入住
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[12]/div/div/div/div/a").click()
        self.driver.assert_template(Template(r"tpl1601456532959.png", record_pos=(5.815, 3.265), resolution=(100, 100)), "弹出弹窗")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写姓名']").send_keys("哼哼")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写所属机构或学校名称']").send_keys("哈哈")
        self.driver.find_element_by_xpath("//input[@placeholder='请输入团队的人数']").send_keys("12")
        self.driver.find_element_by_xpath("//textarea[@placeholder='请填写个人的介绍']").send_keys("你好！")
        #点击下一步
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/a").click()
        self.driver.assert_template(Template(r"tpl1601456726201.png", rgb=True, record_pos=(5.775, 3.275), resolution=(100, 100)), "擅长教学方向")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写擅长的编程语言']").send_keys("")
        self.driver.find_element_by_xpath("//textarea[@placeholder='请填写擅长的课程主题或方向']").send_keys("自动化测试")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写擅长的课程所覆盖的学生年龄范围']").send_keys("大于18")
        #点击下一步
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/a[2]").click()
        self.driver.assert_template(Template(r"tpl1601456897449.png", record_pos=(7.35, 3.29), resolution=(100, 100)), "联系方式")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写正确的电子邮箱']").send_keys("123456@qq.com")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写正确的手机号']").send_keys("123456")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写正确的微信号']").send_keys("123456")
        #点击同意注册协议
        self.driver.find_element_by_xpath("//label[@title='同意']").click()
        #点击提交申请
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/a[2]").click()
        self.driver.assert_template(Template(r"tpl1601457678122.png", record_pos=(7.65, 7.165), resolution=(100, 100)), "不可提交")

        
        return
    '''我要开课-填写联系方式错误'''
    #@unittest.skip('跳过')
    def test_10(self):
        # 滚动至‘我要开课’元素可见位置
        ele = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[12]/div/div")
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        sleep(3)
        self.driver.assert_template(Template(r"tpl1601456409488.png", record_pos=(1.21, 5.475), resolution=(100, 100)), "显示名称")
        self.driver.assert_template(Template(r"tpl1601456418869.png", record_pos=(2.635, 5.91), resolution=(100, 100)), "显示简介")
        self.driver.assert_template(Template(r"tpl1601456426728.png", record_pos=(1.325, 6.495), resolution=(100, 100)), "显示申请入住按钮")
        #点击申请入住
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[12]/div/div/div/div/a").click()
        self.driver.assert_template(Template(r"tpl1601456532959.png", record_pos=(5.815, 3.265), resolution=(100, 100)), "弹出弹窗")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写姓名']").send_keys("哼哼")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写所属机构或学校名称']").send_keys("哈哈")
        self.driver.find_element_by_xpath("//input[@placeholder='请输入团队的人数']").send_keys("12")
        self.driver.find_element_by_xpath("//textarea[@placeholder='请填写个人的介绍']").send_keys("你好！")
        #点击下一步
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/a").click()
        self.driver.assert_template(Template(r"tpl1601456726201.png", rgb=True, record_pos=(5.775, 3.275), resolution=(100, 100)), "擅长教学方向")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写擅长的编程语言']").send_keys("python")
        self.driver.find_element_by_xpath("//textarea[@placeholder='请填写擅长的课程主题或方向']").send_keys("自动化测试")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写擅长的课程所覆盖的学生年龄范围']").send_keys("大于18")
        #点击下一步
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/a[2]").click()
        self.driver.assert_template(Template(r"tpl1601456897449.png", record_pos=(7.35, 3.29), resolution=(100, 100)), "联系方式")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写正确的电子邮箱']").send_keys("123456@qq.com")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写正确的手机号']").send_keys("")
        self.driver.find_element_by_xpath("//input[@placeholder='请填写正确的微信号']").send_keys("123456")
        #点击同意注册协议
        self.driver.find_element_by_xpath("//label[@title='同意']").click()
        #点击提交申请
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[3]/a[2]").click()
        self.driver.assert_template(Template(r"tpl1601457678122.png", record_pos=(7.65, 7.165), resolution=(100, 100)), "不可提交")
        
        
        return
    
    '''右侧导航栏'''
    #@unittest.skip('跳过')
    def test_11(self):
        if self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[13]/div[1]"):
            self.driver.assert_template(Template(r"tpl1601459098647.png", record_pos=(17.085, 9.25), resolution=(100, 100)), "显示最近学习模块，展示作品名称")
            #点击继续学习
            self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[13]/div/div[3]/a").click()
            self.driver.switch_to_new_tab()
            print('有学习记录')
            self.driver.close()#关闭标签
            self.driver.switch_to_previous_tab()      
        else:
            print('无学习记录,不显示最近学习模块')
        #向下翻页
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        #点击推荐课
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[13]/div[2]/ul/li/a/span").click()
        self.driver.assert_template(Template(r"tpl1601459669107.png", record_pos=(3.89, 1.24), resolution=(100, 100)), "页面上/下滑动至热门推荐模块")
        #点击右侧导航栏的入门课
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[13]/div[2]/ul/li[3]/a/span").click()
        self.driver.assert_template(Template(r"tpl1601459733087.png", record_pos=(3.905, 1.205), resolution=(100, 100)), "页面上/下滑动至入门体验模块")
        #点击右侧导航栏的系列课
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[13]/div[2]/ul/li[9]/a/span").click()
        self.driver.assert_template(Template(r"tpl1601459804501.png", record_pos=(4.535, 1.225), resolution=(100, 100)), "页面上/下滑动至系列课模块")
        #点击右侧导航栏的知识点
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[13]/div[2]/ul/li/a/span").click()
        self.driver.assert_template(Template(r"tpl1601459954517.png", record_pos=(3.93, 1.23), resolution=(100, 100)), "页面上/下滑动至热门推荐模块")
        #点击右侧导航栏的主题课
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[13]/div[2]/ul/li[10]/a/span").click()
        self.driver.assert_template(Template(r"tpl1601460009104.png", record_pos=(4.965, 1.19), resolution=(100, 100)), "页面上/下滑动至知识点小课堂模块")
        #点击右侧导航栏的回顶部
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[13]/div[2]/ul/li[11]/a/span").click()
        self.driver.assert_template(Template(r"tpl1601460054293.png", record_pos=(1.56, 0.53), resolution=(100, 100)), "页面上滑动至顶部")
        #向下翻页
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        #鼠标移动到右侧导航栏的公众号
        pic = self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[13]/div[3]/a")
        ActionChains(self.driver).move_to_element(pic).perform()
        self.driver.assert_template(Template(r"tpl1601460197967.png", record_pos=(17.455, 8.54), resolution=(100, 100)), "左侧显示二维码，微信扫描可关注公众号")
        #点击右侧导航栏的问卷
        self.driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div[13]/div[4]/a").click()
        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1601460375188.png", record_pos=(8.94, 1.59), resolution=(100, 100)), "请填写测试点")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()     
        return
    
    '''课程详情页'''
    #@unittest.skip('跳过')
    def test_12(self):
        self.driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        self.driver.assert_template(Template(r"tpl1602208585823.png", record_pos=(4.52, 5.135), resolution=(100, 100)), "请填写测试点")
        self.driver.find_element_by_xpath("//*[@id=\"recommend\"]/div/div/div[2]/div[2]/div/ul/li[5]/div/div[2]/div[2]/p/a").click()

        self.driver.switch_to_new_tab()
        self.driver.assert_template(Template(r"tpl1602208644800.png", record_pos=(1.67, 0.475), resolution=(100, 100)), "跳转至该工作室详情页面")
        self.driver.close()#关闭标签
        self.driver.switch_to_previous_tab()        
        return
    
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(course))
runner = unittest.TextTestRunner()
runner.run(suite)    
    
    
    
    