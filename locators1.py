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
print(driver.current_url)
sleep(2)
driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[9]").click()
sleep(6)
actions =ActionChains(driver)
actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[title='View your shopping cart']")).perform()
time.sleep(6)
driver.find_element(By.CSS_SELECTOR, "a[class='button wc-forward wp-element-button']").click()
# info for XPATH below:
#RELATIVE XPATH syntax starts with double slashies // and fallow the tag name and the @singe than atribute and the value (//a[@href='http://shopping.beeyor.com/shop/'])[1]
driver.close()

# actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "div[class='wc-block-grid wp-block-product-new wc-block-product-new has-4-columns has-multiple-rows'] a[aria-label='Add “Cool” to your cart']")).click()
 #CSS info bellow:
 #CSS locator need tag name scuare brackets and brchyalebi syntax is symilat to XPATH but without slashes and @ sing
#a[class='button wc-forward wp-element-button']