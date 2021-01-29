import time
from selenium.webdriver.common.by import By
from selenium_po.page.basepage import BasePage


class ContactPage(BasePage):

    def click_add_member(self):
        from selenium_po.page.add_member_page import AddMemberPage
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        self.wait_for_click(ele, 5)
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))
        while True:
            self.find(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            element = self.finds(By.ID, "username")
            if len(element) > 0:
                break
        return AddMemberPage(self.driver)

    def get_member(self):
        time.sleep(2)
        eles = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for value in eles:
            print(value.get_attribute("title"))
            name_list.append(value.get_attribute("title"))
        return name_list
