import unittest # 单元测试框架
from appium import webdriver # appium库


class AppTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = '/Users/shijifeng/Downloads/depot-android-release-1599122464503.apk'
        desired_caps['noReset'] = False
        # desired_caps["unicodeKeyboard"] = "True"
        # desired_caps["resetKeyboard"] = "True"

        self.wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.wd.implicitly_wait(60)

    def test_login(self):
        pass

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()