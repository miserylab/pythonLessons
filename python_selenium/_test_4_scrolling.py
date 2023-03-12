import time
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
# driver.maximize_window()
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

time.sleep(1)

# driver.execute_script("window.scrollTo(0, 500);")
action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
action.move_to_element(red_t_shirt).perform()



time.sleep(1)

now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
name_screenshot = "screenshot_" + now_date + ".png"
driver.save_screenshot('C:\\Users\\miser\\PycharmProjects\\pythonLessons\\python_selenium\\screenshots\\' + name_screenshot)