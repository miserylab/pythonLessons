import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
# driver.maximize_window()
driver.set_window_size(1000, 1000)

driver.implicitly_wait(10) # явное ожидание на странице

print("Start test")
visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
visible_button.click()
print("Finish test")


