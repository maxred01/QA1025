import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.netflix.com/')
driver.maximize_window()
# driver.find_element(By.XPATH, '//a[@class=" ea2wixt2 default-ltr-iqcdef-cache-1de5mro"]').click()
print(driver.find_element(By.CSS_SELECTOR, ' [data-uia="loc"] header [aria-hidden="true"]').text)
print(driver.find_element(By.XPATH, '//*[@data-uia="header-login-link"]').get_attribute('href'))

time.sleep(2)