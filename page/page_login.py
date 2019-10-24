from base.base import Base
import page


class PageLogin(Base):
    # 关闭弹窗
    def page_close_alert(self):
        self.base_click(page.login_close_alert)

    # 点击 我
    def page_click_me(self):
        self.base_click(page.login_me)

    # 点击 已有账号，去登录
    def page_click_username_exists(self):
        self.base_click(page.login_username_exists)

    # 输入 用户名
    def page_input_username(self,username):
        self.base_input(page.login_username,username)

    # 输入 密码
    def page_input_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd)

    # 点击 登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 登录组合业务
    def page_login(self,username,pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()