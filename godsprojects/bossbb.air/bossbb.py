# -*- encoding=utf8 -*-
__author__ = "shijifeng"

from airtest.core.api import *

auto_setup(__file__)
start_app("com.sxc.bossbb")
touch(Template(r"tpl1605692021907.png", record_pos=(-0.047, -0.056), resolution=(720, 1440)))
text("15757185534")
touch(Template(r"tpl1605692046781.png", record_pos=(0.028, 0.14), resolution=(720, 1440)))

text("12345")
touch(Template(r"tpl1606706034159.png", record_pos=(-0.003, 0.312), resolution=(720, 1440)))
touch(Template(r"tpl1606706046685.png", record_pos=(-0.001, 0.058), resolution=(720, 1440)))
