import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://demoqa.com/radio-button')
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@for="yesRadio"]').click()
assert driver.find_element(By.ID, 'yesRadio').is_selected()
selected_yes = driver.find_element(By.CLASS_NAME, 'text-success').text
assert selected_yes == 'Yes'
time.sleep(1)

driver.find_element(By.XPATH, '//*[@for="impressiveRadio"]').click()
assert driver.find_element(By.ID, 'impressiveRadio').is_selected()
selected_impressive = driver.find_element(By.CLASS_NAME, 'text-success').text
assert selected_impressive == 'Impressive'
time.sleep(1)

disabled_radio = driver.find_element(By.ID, 'noRadio')
# Проверяем, что кнопка действительно отключена
assert not disabled_radio.is_enabled()
print("Кнопка 'No' заблокирована")

time.sleep(2)


driver.get('https://demoqa.com/webtables')
driver.maximize_window()
time.sleep(3)


driver.find_element(By.ID, 'addNewRecordButton').click()
time.sleep(1)
driver.find_element(By.ID, 'firstName').send_keys("Зуева")
driver.find_element(By.ID, 'lastName').send_keys("Дарья")
driver.find_element(By.ID, 'userEmail').send_keys("test@test.com")
driver.find_element(By.ID, 'age').send_keys("123")
driver.find_element(By.ID, 'salary').send_keys("100500")
driver.find_element(By.ID, 'department').send_keys("QA")
driver.find_element(By.ID, 'submit').click()
time.sleep(3)
