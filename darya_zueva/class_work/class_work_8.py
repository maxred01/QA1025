import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://demoqa.com/text-box')
driver.maximize_window()

user_name = 'Зуева Дарья'
user_email = 'test@test.com'
current_address = 'г. Тест, ул. Тест, д. 40, кв.66'
permanent_address = 'г. Тест, ул. Тест, д. 40, кв.666'

driver.find_element(By.ID, value='userName').send_keys(user_name)
driver.find_element(By.ID, value='userEmail').send_keys(user_email)
driver.find_element(By.ID, value='currentAddress').send_keys(current_address)
driver.find_element(By.ID, value='permanentAddress').send_keys(permanent_address)
driver.find_element(By.ID, value='submit').click()

name = driver.find_element(By.XPATH, value='//p[@id="name"]').text
email = driver.find_element(By.XPATH, value='//p[@id="email"]').text
currentAddress = driver.find_element(By.XPATH, value='//p[@id="currentAddress"]').text
permanentAddress = driver.find_element(By.XPATH, value='//p[@id="permanentAddress"]').text

assert permanentAddress.find(permanent_address) != -1
assert name.find(user_name) != -1
assert email.find(user_email) != -1
assert currentAddress.find(current_address) != -1


driver.get('https://demoqa.com/checkbox')
driver.maximize_window()

selected_checkbox = 'home'

driver.find_element(By.XPATH, value='//*[@aria-expanded="false"]/*[2]').click()
driver.find_element(By.XPATH, value='(//*[@aria-expanded="false"])[1]/*[2]').click()
driver.find_element(By.XPATH, value='(//*[@aria-expanded="false"])[2]/*[2]').click()
driver.find_element(By.XPATH, value='//*[@aria-checked="false"]').click()

selected = driver.find_element(By.XPATH, value='//*[@id="result"]/*[2]').text

assert selected.find(selected_checkbox) != -1

driver.get('https://demoqa.com/radio-button')
driver.find_element(By.XPATH, '//*[@for="impressiveRadio"]').click()
assert driver.find_element(By.ID, 'impressiveRadio').is_selected()
time.sleep(1)

driver.get('https://demoqa.com/buttons')
doubleClickBtn = driver.find_element(By.ID, 'doubleClickBtn')
rightClickBtn = driver.find_element(By.ID, 'rightClickBtn')
tvpiU = driver.find_element(By.ID, 'tvpiU')

ActionChains.double_click(doubleClickBtn).perform()
ActionChains.double_click(doubleClickBtn).perform()