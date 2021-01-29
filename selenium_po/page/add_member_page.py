from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_po.page.basepage import BasePage
from selenium_po.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    ele_name = (By.ID, "username")
    ele_id = (By.ID, "memberAdd_acctid")
    ele_mail = (By.ID, "memberAdd_mail")

    def add_member(self, name, id, mail):
        self.find(*self.ele_name).send_keys(name)
        self.find(*self.ele_id).send_keys(id)
        self.find(*self.ele_mail).send_keys(mail)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

        return ContactPage(self.driver)
