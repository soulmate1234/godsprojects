import unittest

from airtest.core.api import init_device, touch, auto_setup
from airtest.core.cv import Template
import os


class MyTestCase(unittest.TestCase):
    __file__ = os.getcwd()
    print(__file__)
    auto_setup(__file__)
    def setUp(self) -> None:
        init_device("Android", "CLBGL18A23000056")
    def test_1(self):
        touch(Template(r"tpl1606792128602.png", record_pos=(-0.12, 0.412), resolution=(1080, 1920)))


if __name__ == '__main__':
    unittest.main()
