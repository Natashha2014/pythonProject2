import time
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
#options.add_argument("--start-minimized") #panjarad daapataravebs da driver minimize kide vapshe chakecavs.
#options.add_argument("headless")
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_experimental_option("detach", True)
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)

driver.get("http://shopping.beeyor.com/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
sleep(2)
driver.execute_script("window.scrollTo(document.body.scrollHeight, 0)")
sleep(3)
