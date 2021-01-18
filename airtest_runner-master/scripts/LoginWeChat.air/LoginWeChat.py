# -*- encoding=utf8 -*-
__author__ = "AUSU"

from airtest.core.api import *

auto_setup(__file__)

start_app("com.tencent.mm")#输入微信包名，启动微信
touch(Template(r"tpl1598005515151.png", record_pos=(0.199, 0.832), resolution=(720, 1280)))
touch(Template(r"tpl1598005585671.png", record_pos=(0.007, 0.372), resolution=(720, 1280)))
assert_exists(Template(r"tpl1598005623085.png", record_pos=(-0.278, -0.578), resolution=(720, 1280)), "页面跳转成功")
touch(Template(r"tpl1598005669183.png", record_pos=(-0.203, -0.096), resolution=(720, 1280)))
assert_exists(Template(r"tpl1598005714701.png", record_pos=(-0.14, -0.585), resolution=(720, 1280)), "判断页面是否成功跳转")
touch(Template(r"tpl1598006459665.png", record_pos=(0.049, -0.389), resolution=(720, 1280)))
text("wx_75040",enter=False)
touch(Template(r"tpl1598005881998.png", record_pos=(-0.089, -0.243), resolution=(720, 1280)))
text("CRTest123",enter=False)
touch(assert_exists(Template(r"tpl1598006000999.png", record_pos=(-0.004, 0.093), resolution=(720, 1280)), "判断账号密码是否成功输入"))
wait(Template(r"tpl1598006123390.png", record_pos=(-0.126, 0.812), resolution=(720, 1280)))#等待图片出现，当前处于登录加载界面
assert_exists(Template(r"tpl1598006263792.png", record_pos=(-0.429, -0.771), resolution=(720, 1280)), "判断是否成功登录")
print('登录成功')
















