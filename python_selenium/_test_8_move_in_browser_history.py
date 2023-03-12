import time
import datetime

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



menu =  driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
menu.click()
print("Click menu button")
time.sleep(1)

link_about = driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')
link_about.click()
print("Click about link")


driver.back()
print("Go back")
time.sleep(1)
driver.forward()
print("Go forward")

#
# url = "https://saucelabs.com/"
# get_url = driver.current_url
# print(get_url)
# assert get_url == url
# print("GOOD URL")
#
# time.sleep(1)
# now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
# name_screenshot = "screenshot_" + now_date + ".png"
# driver.save_screenshot('C:\\Users\\miser\\PycharmProjects\\pythonLessons\\python_selenium\\screenshots\\' + name_screenshot)


