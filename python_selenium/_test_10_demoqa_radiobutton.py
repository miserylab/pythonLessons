import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

time.sleep(1)
# radio_button = driver.find_element(By.XPATH, '//input[@id="yesRadio"]') # не работает
radio_button = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
radio_button.click()

time.sleep(1)

