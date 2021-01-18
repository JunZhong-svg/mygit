# -*- coding: utf-8 -*-
import win32gui
'''根据窗口类型和名称获取窗口句柄'''
hq=win32gui.FindWindow('GlassWndClass-GlassWindowClass-3',u'PerfDog(v4.1.200708)')
print(hq)