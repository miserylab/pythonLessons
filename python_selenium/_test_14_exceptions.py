import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()

try:
    visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
    visible_button.click()
except NoSuchElementException as exception:
    print('NoSuchElementException exception')
    time.sleep(6)
    visible_button = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
    visible_button.click()
    print("Click on visible button")


