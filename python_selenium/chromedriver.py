import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.saucedemo.com/')
driver.maximize_window()

# user_name = driver.find_element(By.ID, 'user-name') #ID
# user_name = driver.find_element(By.NAME, 'user-name') #name
# user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]') #id xpath
# user_name = driver.find_element(By.XPATH, '//input[@data-test="username"]') #data-test xpath
user_name = driver.find_element(By.CSS_SELECTOR, '#user-name') #Selector


user_name.send_keys('standard_user')

password = driver.find_element(By.CSS_SELECTOR, '#password')

password.send_keys('secret_sauce')

login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')
login_button.click()

time.sleep(10)
driver.close()
