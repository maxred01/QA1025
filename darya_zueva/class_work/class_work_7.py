import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.nadejdakadisheva.ru/')
driver.maximize_window()
#driver.find_element(By.XPATH, '//*[@target="_blank"])[1]"]').click()
print(driver.find_element(By.XPATH, value='(//main//*[@target="_blank"])[8]').text)
print(driver.find_element(By.XPATH, value='(//main//*[@target="_blank"])[3]').get_attribute('href'))

time.sleep(2)
