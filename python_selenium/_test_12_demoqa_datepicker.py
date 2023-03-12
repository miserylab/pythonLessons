import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
new_date.send_keys(Keys.CONTROL + 'a')
new_date.send_keys(Keys.SPACE)
time.sleep(1)
new_date.send_keys('04/13/2022')
time.sleep(1)
new_date.send_keys(Keys.RETURN)

time.sleep(1)


