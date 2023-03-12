import datetime
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
driver.maximize_window()

actions = ActionChains(driver)

square = driver.find_element(By.XPATH, '//input[@class="slider-square"]')
# actions.context_click(square).move_by_offset(20,0).release().perform()

# actions.drag_and_drop_by_offset(square, 20, 0)

actions.click_and_hold(square).move_by_offset(-300, 0).release().perform()

time.sleep(1)
