# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
import win32gui
import win32api,win32con

auto_setup(__file__)

class startApp():
    def start_application(self):
        '''启动QQ游戏'''
        win32api.ShellExecute(0, 'open', r"D:\Program Files (x86)\Tencent\QQGameTempest\QQGame.exe", '','',1)
        sleep(3)
        '''获得屏幕分辨率X轴'''
        x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)   
        '''获得屏幕分辨率Y轴'''
        y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)   
        print(x,y)
        '''获取窗口句柄'''
        handle = win32gui.FindWindow(None,'QQ游戏')
        print(handle)
        if handle == 0:
            print('没获取到应用句柄')
            '''关闭QQ游戏'''
            os.system("taskkill /F /IM QQGame.exe")

        '''窗口最大化'''
        win32gui.ShowWindow(handle, win32con.SW_MAXIMIZE) 

        return handle,x,y
    
startApp = startApp()




























