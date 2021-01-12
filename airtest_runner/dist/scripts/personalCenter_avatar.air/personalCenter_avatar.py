# -*- encoding=utf8 -*-
#内容：个人中心——头像（已登录）
#编写人：钟俊
#修改时间：2020-10-12
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

using(r"common.air")
from common import common
from selenium.webdriver.common.keys import Keys
from airtest_selenium.proxy import WebChrome
from selenium.webdriver import ActionChains

driver = common.enter_personalCenter()#进入个人中心
def main():
    headPortraid = driver.find_element_by_xpath("//img[@alt='您的头像']")
    ActionChains(driver).move_to_element(headPortraid).perform()#鼠标移动到头像
    driver.assert_template(Template(r"tpl1601257341568.png", record_pos=(18.11, 0.57), resolution=(100, 100)), "出现更改按钮")
    
    driver.quit()  
    return

try:
    main()
except:
    driver.quit()