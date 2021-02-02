# -*- encoding=utf8 -*-
__author__ = "shijifeng"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
start_app("com.sxc.bossbb")
poco(text="手机号登录").click()

poco(text="请输入手机号").click()

text("15757185534")
poco(text="请输入密码").click()

poco(text="请输入密码").set_text("123")


poco(text="登录").click()
poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").offspring("android.widget.ScrollView").child("android.view.ViewGroup").click()


touch(Template(r"tpl1612147817463.png", record_pos=(0.003, 0.022), resolution=(1080, 2244)))

poco(text="生产管理").click()


poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").offspring("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].click()

poco(text="请选择切底地点").click()
poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").offspring("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.view.ViewGroup").child("android.widget.TextView").click()
poco("android.widget.LinearLayout").offspring("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").click()
poco(text="添加切底原料").click()


touch(Template(r"tpl1612148342768.png", record_pos=(-0.41, -0.608), resolution=(1080, 2244)))


poco(text="确定").click()

poco(text="提交").click()

poco(text="切底中").click()






