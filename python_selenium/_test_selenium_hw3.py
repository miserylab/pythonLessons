from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



'''Выбор товара'''
products = ['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
# products.append['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']
print("Приветствую тебя в нашем интеренет магазине!")
# print("Выбери один из следующих товаров и укажи его номер: \n1 - Sauce Labs Backpack, \n2 - Sauce Labs Bike Light, "
#       "\n3 - Sauce Labs Bolt T-Shirt, \n4 - Sauce Labs Fleece Jacket, \n5 - Sauce Labs Onesie, "
#       "\n6 - Test.allTheThings() T-Shirt (Red)")
print("Выбери один из следующих товаров и укажи его номер: ")

for i in range(len(products)):
    print(i + 1, products[i])

try:
    сhosen_product_number = int(input("\nВведите номер товара: "))
    if сhosen_product_number <= len(products):
        product_name = products[сhosen_product_number - 1]
        print(сhosen_product_number, product_name)
    else:
        print("Номер товара введен неверно")
        exit()
except ValueError as exception:
    print("Номер товара введен неверно")
    exit()


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1000, 1000)

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


class Product_locators:
    '''Создаём класс для локаторов товаров'''

    def __init__(self, name_locator, price_locator, button_locator_text):
        self.name_locator = name_locator
        self.price_locator = price_locator
        self.button_locator_text = button_locator_text


products = []
products.append(
    Product_locators(driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]'),
                     driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div'),
                     '//button[@id="add-to-cart-sauce-labs-backpack"]'))
products.append(
    Product_locators(driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]'),
                     driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div'),
                     '//button[@id="add-to-cart-sauce-labs-bike-light"]'))
products.append(
    Product_locators(driver.find_element(By.XPATH, '//a[@id="item_1_title_link"]'),
                     driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div'),
                     '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
products.append(
    Product_locators(driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]'),
                     driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div'),
                     '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]'))
products.append(
    Product_locators(driver.find_element(By.XPATH, '//a[@id="item_2_title_link"]'),
                     driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[5]/div[2]/div[2]/div'),
                     '//button[@id="add-to-cart-sauce-labs-onesie"]'))
products.append(
    Product_locators(driver.find_element(By.XPATH, '//a[@id="item_3_title_link"]'),
                     driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[6]/div[2]/div[2]/div'),
                     '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]'))

# '''Выбор товара'''
#
# print("Приветствую тебя в нашем интеренет магазине!")
# print("Выбери один из следующих товаров и укажи его номер:")
#
# for i in range(len(products)):
#     print(i + 1, products[i].name_locator.text)
#
# сhosen_product_number = int(input("\nВведите номер товара: "))
# if сhosen_product_number <= len(products):
#     print(сhosen_product_number)
# else:
#     print("Номер товара введен неверно")
#     exit()



'''info Product'''



value_product = products[сhosen_product_number - 1].name_locator.text
print(value_product)

value_price_product = products[сhosen_product_number - 1].price_locator.text
print(value_price_product)

select_product = driver.find_element(By.XPATH, products[сhosen_product_number - 1].button_locator_text)
select_product.click()

print(f"Product {products[сhosen_product_number - 1].name_locator.text} added to cart!")

'''Enter cart'''

cart = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
cart.click()
print("Enter cart")

'''info Cart Product'''
cart_product = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
value_cart_product = cart_product.text
print(value_cart_product)

assert value_cart_product == value_product
print("INFO Cart product GOOD")

price_cart_product = driver.find_element(By.XPATH, '//div[@class="inventory_item_price"]')
value_price_cart_product = price_cart_product.text
print(value_price_cart_product)

assert value_price_cart_product == value_price_product
print("INFO Cart price product GOOD")

checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
checkout.click()
print("Click checkout")

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

'''info Finish Product'''
finish_product = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
value_finish_product = finish_product.text
print(value_finish_product)

assert value_finish_product == value_product
print("INFO Finish product GOOD")

price_finish_product = driver.find_element(By.XPATH, '//div[@class="inventory_item_price"]')
value_price_finish_product = price_finish_product.text
print(value_price_finish_product)

assert value_price_finish_product == value_price_product
print("INFO Finish price product GOOD")

'''Summary price'''

summary_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
value_summary_price = summary_price.text
print(value_summary_price)

item_total = "Item total: " + value_price_product
print(item_total)

assert value_summary_price == item_total
print("Total Summary price GOOD")