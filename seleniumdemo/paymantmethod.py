import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
service_obj = Service("/opt/homebrew/bin/chromedriver")
# driver = webdriver.Chrome(service=service_obj, options=options)
# driver.maximize_window()
# sleep(2)
# driver.get("http://shopping.beeyor.com/")
# print(driver.current_url)
# time.sleep(4)
# driver.find_element(By.XPATH, "(//a[@href='http://shopping.beeyor.com/shop/'])[1]").click()
# sleep(3)
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# select.select_by_value("menu_order")
# list_of_items = driver.find_elements(By.XPATH, "//a[text()='Add to cart']")
# for item in list_of_items:
#     item.click()
# sleep(5)
# driver.find_element(By.XPATH, "(//a[@title='View cart'])[1]").click()
# sleep(3)
# driver.find_element(By.ID, "coupon_code").send_keys("Tojtech QA1 2023 Automation 10%")
# sleep(3)
# driver.find_element(By.CSS_SELECTOR, "button[name='apply_coupon']").click()


#driver.find_element(By.CLASS_NAME, "checkout-button").click()

