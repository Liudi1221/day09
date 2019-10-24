import sys
import os
sys.path.append(os.getcwd())

import pytest
from page.page_login import PageLogin

def get_data():
    return [('17744560055','Didi911221'),
            ('17744560053','Didi'),
            ('17744560053','Didi911221')]

class TestLogin():
    # 初始化
    def setup_class(self):
        # 获取 pagelogin对象
        self.login = PageLogin()
        # 关闭弹窗
        self.login.page_close_alert()
        # 点击我
        self.login.page_click_me()
        # 点击 已有帐号，去登录
        self.login.page_click_username_exists()

    # 结束
    def teardown_class(self):
        # 关闭 driver
        self.login.driver.quit()

    # 业务执行
    @pytest.mark.parametrize('username,pwd',get_data())
    def test_login(self,username,pwd):
        self.login.page_login(username,pwd)
