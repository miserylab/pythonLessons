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
new_date.click()
time.sleep(1)

date_13 = driver.find_element(By.XPATH, '//div[@aria-label="Choose Monday, March 13th, 2023"]')
date_13.click()

time.sleep(1)

new_date.click()
date_today = driver.find_element(By.XPATH, '//div[contains(@class,"react-datepicker__day--today")]')
date_today.click()
time.sleep(1)