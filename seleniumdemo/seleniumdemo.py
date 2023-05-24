# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# options = Options()
# options.add_experimental_option("detach", True)
# service_obj = Service("/opt/homebrew/bin/chromedriver")
# driver = webdriver.Chrome(service=service_obj, options=options)
# driver.get("http://shopping.beeyor.com/")
# driver.find_element(By.CSS_SELECTOR, "#woocommerce-product-search-field-0").send_keys("eShapalaq loop wakey machine")
# sleep(5)
# print(driver.current_url)
# print(driver.title)
# driver.close()

from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("http://shopping.beeyor.com/")
driver.maximize_window()
# sleep(2)
# #driver.minimize_window()
# print(driver.current_url)
# print(driver.title)
# driver.find_element(By.CSS_SELECTOR, "#woocommerce-product-search-field-0").send_keys("eShapalaq loop wakey machine")
# driver.find_element(By.CSS_SELECTOR, "#woocommerce-product-search-field-0").send_keys(Keys.ENTER)
# sleep(6)
# #driver.refresh()
# driver.back()
# sleep(4)
# #driver.find_element(By.CSS_SELECTOR, "#woocommerce-product-search-field-0").send_keys(Keys.COMMAND + "A")
# sleep(3)
# driver.find_element(By.CSS_SELECTOR, "#woocommerce-product-search-field-0").clear()
# sleep(3)
# driver.forward()
driver.close()
