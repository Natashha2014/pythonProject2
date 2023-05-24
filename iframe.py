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

driver.get("http://shopping.beeyor.com/shop/")

print(driver.current_url)
sleep(2)
driver.find_element(By.XPATH, "(//a[text()='Shop'])[1]" ).click()
sleep(5)
select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
sleep(5)
select.select_by_index(0)

list_of_items = driver.find_elements(By.XPATH, "//a[text()='Add to cart']")
for item in list_of_items:
    item.click()
sleep(5)
driver.find_element(By.XPATH, "//a[@title='View cart']").click()
sleep(5)
driver.find_element(By.CSS_SELECTOR, "#coupon_code").send_keys("Tojtech QA1 2023 Automation 10%")
driver.find_element(By.CSS_SELECTOR, "button[name='apply_coupon']").click()
sleep(5)
print(driver.find_element(By.CSS_SELECTOR, ".woocommerce-message").text)

sleep(2)
driver.find_element(By.CLASS_NAME, "checkout-button").click()
sleep(5)

# frame = driver.find_elements(By.TAG_NAME, "iframe")
# driver.switch_to.frame(frame[0])
# sleep(5)
# driver.find_element(By.CSS_SELECTOR, "input[aria-label='Credit or debit card number']").send_keys("4242 4242 4242 4242")
# sleep(5)
# driver.switch_to.default_content()
# sleep(5)
# driver.switch_to.frame(frame[1])
# driver.find_element(By.CSS_SELECTOR, "input[aria-label='Credit or debit card expiration date']").send_keys("01/27")
# sleep(5)
# driver.switch_to.default_content()
# sleep(5)
# driver.switch_to.frame(frame[2])
# sleep(5)
# driver.find_element(By.CSS_SELECTOR, "input[aria-label='Credit or debit card CVC/CVV']").send_keys("813")
driver.quit()