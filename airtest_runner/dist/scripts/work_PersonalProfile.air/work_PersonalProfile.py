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
    driver.assert_template(Template(r"tpl1601349171160.png", record_pos=(13.92, 3.365), resolution=(100, 100)), "显示获赞数，显示作品数，显示个人头像，名称无误")
    driver.quit()
    return

try:
    main()
except:
    driver.quit()
    
        
        
        