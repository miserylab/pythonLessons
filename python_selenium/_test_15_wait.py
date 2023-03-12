import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
# driver.maximize_window()
driver.set_window_size(1000, 1000)

print("Start test")
visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="visibleAfter"]')))
visible_button.click()
print("Finish test")


