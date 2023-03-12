import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")

user_name.send_keys(login_standard_user)
print("Input login")

password = driver.find_element(By.XPATH, "//input[@id='password']")

password.send_keys(password_all)
print("Input password")

login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_button.click()
print("Click login button")

'''info Product #1'''
product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
select_product_1.click()
print("Select product 1")

cart = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
cart.click()
print("Enter cart")

'''info Cart Product #1'''
cart_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)

assert value_cart_product_1 == value_product_1
print("INFO Cart product 1 GOOD")

price_cart_product_1 = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_cart_product_1 = price_cart_product_1.text
print(value_price_cart_product_1)


assert value_price_cart_product_1 == value_price_product_1
print("INFO Cart price product 1 GOOD")

checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()
print("Click checkout")

time.sleep(1)

'''Select user INFO'''
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys("Alex")
print("Input first name")

last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys("Ivanchenko")
print("Input last name")

postal_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
postal_code.send_keys("1234")
print("Input postal code")

continue_button = driver.find_element(By.XPATH, '//input[@id="continue"]')
continue_button.click()
print("Click continue")


'''info Finish Product #1'''
finish_product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)

assert value_finish_product_1 == value_product_1
print("INFO Finish product 1 GOOD")

price_finish_product_1 = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_price_finish_product_1 = price_finish_product_1.text
print(value_price_finish_product_1)

assert value_price_finish_product_1 == value_price_product_1
print("INFO Finish price product 1 GOOD")

summary_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_summary_price = summary_price.text
print(value_summary_price)

item_total = "Item total: " + value_price_finish_product_1
print(item_total)

assert value_summary_price == item_total
print("Total Summary price GOOD")
