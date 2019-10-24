from page.page_login import PageLogin
from page.page_order import PageOrder
from page.page_pay import PagePay


class PageIn():
    def page_get_login(self):
        return PageLogin()

    def page_get_order(self):
        return PageOrder()

    def page_get_pay(self):
        return PagePay()

