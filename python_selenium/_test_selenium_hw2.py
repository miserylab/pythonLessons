import datetime

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

new_date = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
new_date.click()
time.sleep(1)

today_date = datetime.date.today()
future_date = today_date + datetime.timedelta(days=10)
print(future_date)

converted_date = future_date.strftime("%m/%d/%Y")
print(converted_date)

new_date.send_keys(Keys.CONTROL + 'a')
new_date.send_keys(Keys.SPACE)
new_date.send_keys(converted_date)
new_date.send_keys(Keys.RETURN)

time.sleep(1)