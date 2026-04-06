import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://store.steampowered.com/?l=russian')
driver.maximize_window()
print(driver.find_element(By.XPATH, value='//*[@id="language_pulldown"]').text)
print(driver.find_element(By.XPATH, value='//*[@aria-label="Меню аккаунта"]/*[2]').get_attribute('href'))
driver.find_element(By.XPATH, value='//*[@aria-label="Меню аккаунта"]/*[2]').click()
time.sleep(5)

