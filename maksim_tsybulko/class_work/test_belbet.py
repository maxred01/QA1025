import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://belbet.by/')

data = [
    'Привет',
    'Как в это играть?',
    'Какая максимальная сумма депозита?',
    'Могут ли граждани РФ играть,',
    'Ау',
    'Какие документы нужны для верификации?',
    'Вы лицензионное казино?',
    'Есть приветсвенный бонус?',
    'Какой вейджер на приветсвтеный бонус?',
    'Ау',
    'Ау'
]

driver.find_element(By.XPATH, "//button[contains(text(), 'Принять')]").click()
time.sleep(3)
driver.find_element(By.ID, "uw-main-button").click()
time.sleep(3)

driver.find_element(By.ID, "uw-button-chat").click()
time.sleep(3)

for i in range(10):
    data_random = random.choice(data)
    driver.find_element(By.NAME, "message").send_keys(data_random)
    time.sleep(random.uniform(4, 10))

    driver.find_element(By.ID, "uw-message-submit-button").click()

    time.sleep(random.uniform(4, 10))

driver.close()
driver.quit()
