import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://demoqa.com/text-box')  # переходим на сайт
driver.maximize_window()  # разрешение на весь экран


user_name = "Кунделев Андрей"
user_email = "test@test.com"
current_address = 'г. Тест, ул. Тестовая, д.1, кв.1'
permanent_address = 'г. Тест, ул. Тестовая, д.1, кв.1'
time.sleep(1)
driver.find_element(By.ID, 'userName').send_keys(user_name)
driver.find_element(By.ID, 'userEmail').send_keys(user_email)
driver.find_element(By.ID, 'currentAddress').send_keys(current_address)
driver.find_element(By.ID, 'permanentAddress').send_keys(permanent_address)
driver.find_element(By.ID, 'submit').click()

time.sleep(1)

name = driver.find_element(By.XPATH, '//p[@id="name"]').text
email = driver.find_element(By.XPATH, '//p[@id="email"]').text
currentAddress = driver.find_element(By.XPATH, '//p[@id="currentAddress"]').text
permanentAddress = driver.find_element(By.XPATH, '//p[@id="currentAddress"]').text
time.sleep(1)

assert permanentAddress.find(permanent_address) != -1
assert currentAddress.find(current_address) != -1
# assert permanentAddress.find(permanent_address) != -1
# assert permanentAddress.find(permanent_address) != -1

# driver.get('https://demoqa.com/checkbox')
# driver.find_element(By.XPATH, '//div[@class='rc-tree-switcher rc-tree-switcher_open'')
# driver.find_element(By.XPATH, '//div[@class='rc-tree-switcher rc-tree-switcher_open')
# driver.find_element(By.XPATH, //span[@aria-label = "Select Commands"]').click()
# time.sleep(1)
# assert driver.find_element(By.XPATH, )
# time.sleep(1)

driver.get('https://demoqa.com/radio-button')  # переходим на сайт
driver.find_element(By.XPATH, '//*[@for="impressiveRadio"]').click()
assert driver.find_element(By.ID, 'impressiveRadio' ).is_selected()
time.sleep(1)

driver.get('https://demoqa.com/buttons')  # переходим на сайт
driver.find_element(By.ID, 'doubleClickBtn').click()
driver.find_element(By.ID, 'rightClickBtn').click()
driver.find_element(By.XPATH, '4UHpG').click()

ActionChains.double_click(doubleClickBtn)