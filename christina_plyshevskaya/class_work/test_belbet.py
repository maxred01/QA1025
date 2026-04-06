import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from christina_plyshevskaya.helpers.main.helpers_main import data, click_cookie
from christina_plyshevskaya.locator.main.locator_main import website, main, chat, message, submit

driver = webdriver.Chrome()

driver.get(website)
driver.maximize_window()

click_cookie(driver)

driver.find_element(By.ID, main).click()
time.sleep(3)
driver.find_element(By.ID, chat).click()
time.sleep(3)

for i in range(7):
    data_random = random.choice(data)
    driver.find_element(By.NAME, message).send_keys(data_random)
    time.sleep(random.uniform(3, 10))

    driver.find_element(By.ID, submit).click()
    time.sleep(random.uniform(3, 10))

driver.close()
driver.quit()

