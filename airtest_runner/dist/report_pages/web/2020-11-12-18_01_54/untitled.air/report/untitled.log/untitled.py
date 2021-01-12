# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
import win32gui
import win32api,win32con

using(r"startApp.air")
from startApp import startApp

handle,x,y = startApp.start_application()
def main():
    auto_setup(__file__, devices=['Windows:///{}'.format(handle), ])
    set_current(0)  # 设备切换操作， 0 代表前面连接的第一个
    touch(Template(r"tpl1605163652659.png", record_pos=(-0.477, -0.166), resolution=(x, y)))
    touch(Template(r"tpl1605163664298.png", record_pos=(-0.477, -0.04), resolution=(x, y)))
    touch(Template(r"tpl1605163671585.png", record_pos=(-0.476, 0.022), resolution=(x, y)))
    
    
    
    
    
    os.system("taskkill /F /IM QQGame.exe")
    return
       
try:
    main()
    
except:
    '''关闭QQ游戏'''
    os.system("taskkill /F /IM QQGame.exe")
 