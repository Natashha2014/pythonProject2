import time
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
options = Options()
options.add_experimental_option("detach", True)
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
sleep(2)
driver.get("http://shopping.beeyor.com/")
print(driver.current_url)
time.sleep(4)
driver.find_element(By.XPATH, "(//a[@href='http://shopping.beeyor.com/shop/'])[1]").click()