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
driver.get("http://shopping.beeyor.com/")
print(driver.current_url)
time.sleep(2)
driver.find_element(By.XPATH, "(//a[@href='http://shopping.beeyor.com/shop/'])[1]").click()
sleep(2)
select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
select.select_by_value("menu_order")
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# select.select_by_value("popularity")
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# select.select_by_value("date")
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# select.select_by_value("rating")
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# select.select_by_value("price")
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# select.select_by_value("price-desc")
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# select.select_by_index(1)
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# select.select_by_index(2)
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# select.select_by_index(3)
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# select.select_by_index(4)
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# select.select_by_index(5)
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# select.select_by_index(0)
list_of_items = driver.find_elements(By.XPATH, "//a[text()='Add to cart']")
for item in list_of_items:
    item.click()
sleep(2)
driver.find_element(By.XPATH, "(//a[@title='View cart'])[1]").click()
sleep(2)
driver.find_element(By.ID, "coupon_code").send_keys("Tojtech QA1 2023 Automation 10%")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[name='apply_coupon']").click()
sleep(2)
driver.find_element(By.CLASS_NAME, "checkout-button").click()
sleep(6)
driver.find_element(By.CSS_SELECTOR, "#select2-billing_country-container").click()
sleep(4)

# driver.execute_script("window.scrollBy(0, 200)", "")
driver.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Ind")
sleep(4)

countries = driver.find_elements(By.CSS_SELECTOR, ".select2-results__option")
sleep(3)

for country in countries:
    if country.text == "Indonesia":
        country.click()
driver.find_element(By.ID, "ship-to-different-address-checkbox").click()
sleep(5)





