import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://belbet.by/')
driver.maximize_window()

data = [
    'Привет',
    'Как в это играть?',
    'Какая минимальная и максимальная сумма депозита?',
    'Могут ли граждане РФ играть?',
    'Ау',
    'Вы здесь?',
    'Меня слышно?'
]

driver.find_element(By.XPATH, '//button[contains(text(), "Принять")]').click()
time.sleep(3)
driver.find_element(By.ID, 'uw-main-button').click()
time.sleep(3)
driver.find_element(By.ID, 'uw-button-chat').click()
time.sleep(3)
for i in range(7):
    data_random = random.choice(data)
    driver.find_element(By.NAME, 'message').send_keys(data_random)
    time.sleep(random.uniform(3, 10))

    driver.find_element(By.ID, 'uw-message-submit-button').click()
    time.sleep(random.uniform(3, 10))

driver.close()
driver.quit()

