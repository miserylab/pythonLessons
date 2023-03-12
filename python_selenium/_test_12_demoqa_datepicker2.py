import datetime
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
now_date = datetime.datetime.now().strftime("%d")
print(now_date)

date_1 = int(now_date) + 1
locator = ("//div[@aria-label='Choose Monday, March " + str(date_1) + "th, 2023']")
print(locator)


date_13 = driver.find_element(By.XPATH, locator)
date_13.click()



