import random
import time

from selenium import webdriver

from selenium.webdriver.common.by import By # Класс для поиска элементов по различным локаторам
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://belbet.by/')  # переходим на сайт
driver.maximize_window()  # разрешение на весь экран
data = [
    'Привет',
    'Где почитать правила',
    'Какая минимальная ставка',
    'С какого возраста можно игать?',
    'Где вы?',
    '...',
    'как зарегиться?',
    'паспорт нужен?'


]
data_random = random.choice(data)


driver.find_element(By.XPATH, "//button[contains(text(), 'Принять')]").click()
time.sleep(3)

driver.find_element(By.ID, 'uw-main-button').click()
time.sleep(3)

driver.find_element(By.ID, 'uw-button-chat').click()
time.sleep(3)

for i in range(10):
    data_random = random.choice(data)
    driver.find_element(By.NAME, "message").send_keys(data_random)
    time.sleep(random.uniform(4,10))
    driver.find_element(By.ID, "uw-message-submit-button").click()
    time.sleep(random.uniform(4, 10))


driver.close()
driver.quit()