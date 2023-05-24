import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
options = Options()
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)



