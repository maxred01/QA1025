import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://larisadolina.com/')
driver.maximize_window()
time.sleep(3)
driver.set_window_size(550, 866)
time.sleep(3)

driver.find_element(By.XPATH, '(//*[@aria-hidden="true"])[1]').click()
print(driver.find_element(By.XPATH, '(//*[@aria-current="page"])[2]').text) #закомитить текст вверху
# print(driver.find_element(By.XPATH, '(//*[@aria-hidden="true"])[1]').get_attribute('href'))


time.sleep(2)
