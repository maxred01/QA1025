import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://demoqa.com/radio-button')
driver.maximize_window()



driver.find_element(By.XPATH, value='(//*[@name="like"])[1]').click()
assert driver.find_element(By.ID, 'yesRadio').is_selected()
button_yes = driver.find_element(By.CLASS_NAME, 'text-success').text
assert button_yes == 'Yes'

driver.find_element(By.XPATH, value='(//*[@name="like"])[2]').click()
assert driver.find_element(By.ID, 'impressiveRadio').is_selected()
button_impressive = driver.find_element(By.CLASS_NAME, 'text-success').text
assert button_impressive == 'Impressive'

button_no = driver.find_element(By.XPATH, value='(//*[@name="like"])[3]')
assert not button_no.is_enabled()

time.sleep(2)
