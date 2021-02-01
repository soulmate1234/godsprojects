# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco =AndroidUiautomationPoco(use_airtest_input=False, screenshot_each_action=False)


touch(Template(r"tpl1606792128602.png", record_pos=(-0.12, 0.412), resolution=(1080, 1920)))


sleep(1.0)
sleep(1.0)
touch(Template(r"tpl1605840310115.png", record_pos=(0.219, -0.736), resolution=(720, 1440)))
sleep(1.0)
sleep(1.0)
sleep(1.0)

touch(Template(r"tpl1605840322629.png", record_pos=(-0.003, -0.525), resolution=(720, 1440)))
sleep(1.0)
sleep(1.0)
sleep(1.0)
#swipe(Template(r"tpl1605841211820.png", record_pos=(0.003, 0.083), resolution=(720, 1440)), vector=[-0.3417, -0.05])

poco.swipe([930,490],[268,490],duration=2)




sleep(1.0)
sleep(1.0)


touch(Template(r"tpl1605841423666.png", record_pos=(0.386, 0.072), resolution=(720, 1440)))



sleep(1.0)
sleep(1.0)
sleep(1.0)
poco(text="提交").click()


touch(Template(r"tpl1605840787009.png", record_pos=(0.008, 0.1), resolution=(720, 1440)))
sleep(1.0)
sleep(1.0)
touch(Template(r"tpl1605840825009.png", record_pos=(0.0, -0.514), resolution=(720, 1440)))
sleep(1.0)
sleep(1.0)

touch(Template(r"tpl1605840854390.png", record_pos=(0.35, -0.503), resolution=(720, 1440)))

sleep(1.0)
sleep(1.0)
touch(Template(r"tpl1605841629606.png", record_pos=(-0.35, -0.511), resolution=(720, 1440)))


sleep(1.0)
sleep(1.0)
touch(Template(r"tpl1605840884538.png", record_pos=(-0.417, -0.864), resolution=(720, 1440)))
sleep(1.0)
sleep(1.0)












