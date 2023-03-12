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

checkbox_1 = driver.find_element(By.XPATH, '//input[@value="cb1"]')
checkbox_1.click()

result = checkbox_1.get_attribute('checked')
print(result)

time.sleep(1)

checkbox_3 = driver.find_element(By.XPATH, '//input[@value="cb3"]')
checkbox_3.click()
print(checkbox_3.get_attribute('checked'))
time.sleep(1)

# toggle = driver.find_element(By.XPATH, '//button[@aria-label="Toggle"]')
# toggle.click()
#
# time.sleep(1)
