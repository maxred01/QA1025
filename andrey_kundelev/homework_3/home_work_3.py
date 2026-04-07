import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By # Класс для поиска элементов по различным локаторам
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://demoqa.com/text-box')  # переходим на сайт
driver.maximize_window()  # разрешение на весь экран

user_name = "Кунделев Андрей" # Задаем тестовые данные
user_email = "test@test.com"
current_address = 'г. Тест, ул. Тестовая, д.1, кв.1'
permanent_address = 'г. Тест, ул. Тестовая, д.1, кв.1'


driver.find_element(By.ID, 'userName').send_keys(user_name)# Вводим тестовые данные в поля
driver.find_element(By.ID, 'userEmail').send_keys(user_email)
driver.find_element(By.ID, 'currentAddress').send_keys(current_address)
driver.find_element(By.ID, 'permanentAddress').send_keys(permanent_address)
driver.find_element(By.ID, 'submit').click()


name = driver.find_element(By.XPATH, '//p[@id="name"]').text # Берем текст из полей
email = driver.find_element(By.XPATH, '//p[@id="email"]').text
currentAddress = driver.find_element(By.XPATH, '//p[@id="currentAddress"]').text
permanentAddress = driver.find_element(By.XPATH, '//p[@id="permanentAddress"]').text
time.sleep(1)

assert permanentAddress.find(permanent_address) != -1  # Проверяем текст содержится в результате
assert name.find(user_name) != -1
assert email.find(user_email) != -1
assert currentAddress.find(current_address) != -1
time.sleep(1)


driver.get('https://demoqa.com/checkbox') # Переход на страницу с чекбоксами
driver.maximize_window()

selected_checkbox = 'home'
driver.find_element(By.XPATH, '//*[@aria-expanded="false"]/*[2]').click() # Кликаем первый плюс
time.sleep(1)
driver.find_element(By.XPATH, '(//*[@aria-expanded="false"])[1]/*[2]').click() # Кликаем второй плюс
time.sleep(1)
driver.find_element(By.XPATH, '(//*[@aria-expanded="false"])[2]/*[2]').click() # Кликаем третий плюс
time.sleep(1)
driver.find_element(By.XPATH, '//*[@aria-checked="false"]').click()

selected = driver.find_element(By.XPATH, '//*[@id="result"]/*[2]').text # Берем результат из консоли


assert selected.find(selected_checkbox) != -1 # Проверяем что "home" есть в результате
time.sleep(1)

driver.get('https://demoqa.com/radio-button')
driver.maximize_window()


driver.find_element(By.XPATH, '//*[@for="yesRadio"]').click()
time.sleep(1)
assert driver.find_element(By.ID, 'yesRadio').is_selected()
message_yes = driver.find_element(By.CLASS_NAME, 'text-success').text # находим локатор text-success
assert message_yes.find('Yes') != -1
time.sleep(1)


driver.find_element(By.XPATH, '//*[@for="impressiveRadio"]').click()
time.sleep(1)
assert driver.find_element(By.ID, 'impressiveRadio').is_selected()
message_impressive = driver.find_element(By.CLASS_NAME, 'text-success').text
assert message_impressive.find('Impressive') != -1
time.sleep(1)


button = driver.find_element(By.ID, "noRadio")
assert not button.is_enabled()  # Проверка, что кнопка не активна
time.sleep(1)


driver.get('https://demoqa.com/webtables')
driver.maximize_window()
time.sleep(3)


driver.find_element(By.ID, 'addNewRecordButton').click()         # Нажимаем кнопку ADD
time.sleep(1)
driver.find_element(By.ID, 'firstName').send_keys("Андрей")      # Вводим данные
driver.find_element(By.ID, 'lastName').send_keys("Кунделев")
driver.find_element(By.ID, 'userEmail').send_keys("test@test.com")
driver.find_element(By.ID, 'age').send_keys("41")
driver.find_element(By.ID, 'salary').send_keys("100500")
driver.find_element(By.ID, 'department').send_keys("QA")
driver.find_element(By.ID, 'submit').click()
time.sleep(1)
time.sleep(3)

