from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_po.page.add_member_page import AddMemberPage
from selenium_po.page.basepage import BasePage
from selenium_po.page.contact_page import ContactPage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_contact_page(self):
        self.find(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)

    def goto_add_member_page(self):
        self.find(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div').click()
        return AddMemberPage(self.driver)
