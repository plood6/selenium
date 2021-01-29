from time import sleep

import pytest
from selenium_po.page.main_page import MainPage


class TestLogin:

    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name,id,mail", [("zhao", "qian", "sunli@qq.com")])
    def test_login(self, name, id, mail):
        # name = "jason"
        # id = "ukk"
        # mail = "ukk@qq.com"
        namelist = self.main.goto_contact_page().click_add_member(). \
            add_member(name, id, mail).get_member()
        print(namelist)
        assert name in namelist

    @pytest.mark.parametrize("name,id,mail", [("zhou", "wu", "zheng@qq.com")])
    def test_mainadd(self, name, id, mail):
        sleep(5)
        namelist = self.main.goto_add_member_page(). \
            add_member(name, id, mail).get_member()
        print(namelist)
        assert name in namelist
