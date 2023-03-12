import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()


yes_radio_button = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
yes_radio_button.click()
try:
    message = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_message = message.text
    print(value_message)
    assert value_message == 'No'
except AssertionError as exception:
    print('AssertionError exception')
    driver.refresh()
    yes_radio_button = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
    yes_radio_button.click()
    message = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_message = message.text
    print(value_message)
    assert value_message == 'Yes'
    print("Click on yes radio button")
print("test over")

