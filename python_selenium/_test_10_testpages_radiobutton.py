import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
driver.get(base_url)
driver.maximize_window()

time.sleep(1)
radio_button_1 = driver.find_element(By.XPATH, '//input[@value="rd1"]')
radio_button_1.click()
print(radio_button_1.get_attribute('CHECKED'))

time.sleep(1)
