from time import sleep

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    # 初始化driver
    def __init__(self):
        desired_caps = {}  # 定义空字典
        desired_caps['platformName'] = 'Android'  # 指定平台名称
        desired_caps['platformVersion'] = '5.1'  # 版本号
        desired_caps['deviceName'] = 'emulator-5554'  # 设备名称，不能为空，可以随便写
        desired_caps['appPackage'] = 'com.yunmall.lc'  # 包名
        desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'  # 启动名
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 声明⼿机驱动对象
        self.driver.implicitly_wait(10)  # 隐式等待

    # 定位元素
    def base_find(self, location, timeout=30, poll=0.5):
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*location))

    # 点击
    def base_click(self,location):
        # 调用 定位元素
        self.base_find(location).click()

    # 输入
    def base_input(self,location,value):
        # 调用 定位元素
        element = self.base_find(location)
        # 清空
        element.clear()
        sleep(3)
        # 输入
        element.send_keys(value)