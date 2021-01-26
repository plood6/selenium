import time
import yaml
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    cookies = driver.get_cookies()
    with open("data.yaml", "w", encoding="utf-8") as f:
        yaml.dump(cookies, f)
    driver.quit()


def test_addmem():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    with open("data.yaml", encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)
    for cookie in yaml_data:
        driver.add_cookie(cookie)
    driver.implicitly_wait(10)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id("menu_contacts").click()
    ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(ele))
    while True:
        driver.find_element(*ele).click()
        element = driver.find_elements_by_id("username")
        if len(element) > 0:
            break
    driver.find_element(By.ID, "username").send_keys("济公")
    driver.find_element(By.ID, "memberAdd_acctid").send_keys("666")
    driver.find_element(By.ID, "memberAdd_phone").send_keys("13000000086")
    driver.find_element_by_css_selector(".js_btn_save").click()
    time.sleep(3)
    eles = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2")
    name_list = []
    for value in eles:
        print(value.get_attribute("title"))
        name_list.append(value.get_attribute("title"))
    assert "济公" in name_list
    driver.quit()
