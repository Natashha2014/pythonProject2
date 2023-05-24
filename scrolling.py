import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
time.sleep(6)


# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.CSS_SELECTOR, "#checkBoxOption3").click()
# time.sleep(4)
# driver.get("http://shopping.beeyor.com/checkout/")
# driver.find_element(By.CSS_SELECTOR, "#ship-to-different-address-checkbox").click()
# time.sleep()



driver.get("http://shopping.beeyor.com/checkout/")
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "ship-to-different-address-checkbox").click()
time.sleep(5)
# driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
# time.sleep(1)
# driver.maximize_window()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,  "#login-input").send_keys("Ana")
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,  "#login-input").clear()
# time.sleep(5)
# print(driver.title)
# print(driver.current_url)
# awindow = driver.current_window_handle
# login = driver.find_element(By.XPATH, "//a[@class='trk-login-net btn btn-primary login-link-attr']")
# login.click()
# handles = []
# handles = driver.window_handles
# for handle in handles:
#     print(handle)
# newHandle = handles[1]
# driver.switch_to.window(newHandle)
# time.sleep(4)
# driver.get_screenshot_as_file("iphone.png")

