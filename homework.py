from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option("detach", True)
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("http://shopping.beeyor.com/shop/")
sleep(3)
driver.find_element(By.XPATH, "(//a[text()='Shop'])[1]").click()
# sleep(3)
# select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
# sleep(3)
# select.select_by_index(0)

items = driver.find_elements(By.LINK_TEXT, "Add to cart")
for item in items:
    item.click()
    if item == driver.find_element(By.XPATH, "//a[@aria-label='Add “Beanie” to your cart']"):
        break
sleep(3)
driver.find_element(By.XPATH, "//a[@title='View cart']").click()
sleep(3)
driver.find_element(By.CSS_SELECTOR, "#coupon_code").send_keys("Tojtech QA1 2023 Automation 10%")
sleep(3)
driver.find_element(By.NAME, "apply_coupon").click()
sleep(3)
driver.find_element(By.CLASS_NAME, "checkout-button").click()
sleep(3)
driver.find_element(By.CSS_SELECTOR, "#billing_first_name").send_keys("Angelina")
sleep(3)
driver.find_element(By.CSS_SELECTOR, "#billing_last_name").send_keys("Jolly")
sleep(3)
driver.find_element(By.CSS_SELECTOR, "#billing_company").send_keys("Apple")
sleep(3)
driver.find_element(By.CSS_SELECTOR, "#select2-billing_country-container").click()
sleep(3)
driver.find_element(By.CLASS_NAME, "select2-search__field").send_keys("Uni")
sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR, ".select2-results__option")
for country in countries:
    if country.text == "United Kingdom (UK)":
        country.click()
        sleep(2)
        break
countries = (driver.find_elements(By.CSS_SELECTOR, ".select2-results__option"))
sleep(4)


driver.find_element(By.CSS_SELECTOR, "#billing_address_1").send_keys("Green Street")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#billing_address_2").send_keys("50")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#billing_city").send_keys("London")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#billing_postcode").send_keys("03456")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#billing_phone").send_keys("603 717 8888")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#billing_email").send_keys("Jolly@gmail.com")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#ship-to-different-address-checkbox").click()
sleep(2)
driver.quit()

