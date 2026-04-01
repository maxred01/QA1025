import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://belbet.by/')
driver.maximize_window()

data = [
    'Ку',
    'Как тут играть?',
    'Какая максимальная сумма депозита?',
    'Ау',
    'Как дела?',
    'Какой максимальный выигрыш?',
    'Добрый вечер',
    'У вас лицензионное казино?',
    'Как играть в игру?',
    'Какие игры тут есть?',
    'Сколько я могу выграть?'
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
    driver.find_element(By.NAME, 'message').send_keys(data_random)
    time.sleep(random.uniform(4, 10))

    driver.find_element(By.ID, "uw-message-submit-button").click()

    time.sleep(random.uniform(4, 10))

driver.close()
driver.quit()


driver = webdriver.Chrome()
action = ActionChains(driver)

driver.maximize_window()
driver.get('https://belbet.by/games')
time.sleep(25)
action.move_by_offset(403, 369).click().perform()
time.sleep(6)
action.move_by_offset(175, 0).click().perform()
time.sleep(9)
action.move_by_offset(492, 193).click().perform()
time.sleep(9)
action.move_by_offset(132, 142).click().perform()
time.sleep(9)
action.move_by_offset(45, 124).click().perform()
time.sleep(9)
action.move_by_offset(196, 117).click().perform()
time.sleep(9)

driver.close()
driver.quit()