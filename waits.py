from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_experimental_option("detach", True)
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(30)
driver.get("http://shopping.beeyor.com/")
print(driver.current_url)
driver.find_element(By.XPATH, "(//a[@href='http://shopping.beeyor.com/shop/'])[1]").click()
select = Select(driver.find_element(By.XPATH, "(//select[@name='orderby'])[1]"))
select.select_by_index(0)
list_of_items = driver.find_elements(By.XPATH, "//a[text()='Add to cart']")
for item in list_of_items:
    sleep(5)
    item.click()
driver.find_element(By.XPATH, "//a[@title='View cart']").click()
driver.find_element(By.CSS_SELECTOR, "#coupon_code").send_keys("Tojtech QA1 2023 Automation 10%")
driver.find_element(By.CSS_SELECTOR, "button[value='Apply coupon']").click()
text = "Coupon code applied successfully."
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-message"), text))
print(driver.find_element(By.CSS_SELECTOR, ".woocommerce-message").text)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "checkout-button")))
driver.refresh()
driver.find_element(By.CLASS_NAME, "checkout-button").click()
sleep(10)
payment_method = driver.find_elements(By.CSS_SELECTOR, "Input[name='payment_method']")
driver.find_element(By.CSS_SELECTOR, "label[for='payment_method_cod']").click()
sleep(5)
driver.get_screenshot_as_file("screenshot.png")
driver.quit()











