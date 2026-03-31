import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://demoqa.com/radio-button')
driver.maximize_window()

button_yes = 'You have selected'
button_impressive = 'You have selected Impressive'


driver.find_element(By.XPATH, value='(//*[@name="like"])[1]').click()
selected = driver.find_element(By.XPATH, value='//p').text
assert selected.find(button_yes) != -1

driver.find_element(By.XPATH, value='(//*[@name="like"])[2]').click()
selected = driver.find_element(By.XPATH, value='//p').text
assert selected.find(button_impressive) != -1

button_no = driver.find_element(By.XPATH, value='(//*[@name="like"])[3]')
assert not button_no.is_enabled()

time.sleep(2)
