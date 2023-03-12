import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/checkbox/'
driver.get(base_url)
driver.maximize_window()

checkbox = driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]')
checkbox.click()

time.sleep(1)

toggle = driver.find_element(By.XPATH, '//button[@aria-label="Toggle"]')
toggle.click()

time.sleep(1)