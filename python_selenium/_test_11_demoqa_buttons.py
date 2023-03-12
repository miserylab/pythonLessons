from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()

actions = ActionChains(driver)
double_click_button = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
actions.double_click(double_click_button).perform()

double_click_button_text = driver.find_element(By.XPATH, '//p[@id="doubleClickMessage"]')
assert double_click_button_text.text == 'You have done a double click'


right_click_button = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
actions.context_click(right_click_button).perform()

right_click_button_text = driver.find_element(By.XPATH, '//p[@id="rightClickMessage"]')
assert right_click_button_text.text == 'You have done a right click'