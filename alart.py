import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
options = Options()
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
sleep(2)
driver.get("http://the-internet.herokuapp.com/")
time.sleep(2)
driver.find_element(By.LINK_TEXT, "JavaScript Alerts").click()
sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']").click()
sleep(4)
alert = driver.switch_to.alert
alert.accept()
text_for_first_alert = driver.find_element(By.CSS_SELECTOR, "#result")
print(text_for_first_alert.text)
sleep(4)
driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
sleep(4)
alert.dismiss()
text_for_second_alert = driver.find_element(By.ID, "result")
print(text_for_second_alert.text)
sleep(5)
driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
sleep(3)
alert.send_keys("I am Ana and I am the best Automation engineer in the World")
sleep(4)
alert.accept()
text_for_third_alert = driver.find_element(By.ID, "result")
#assert "I  am " not in text_for_third_alert
print(text_for_third_alert.text)
sleep(5)

