import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://demoqa.com/webtables')
driver.maximize_window()
first_name = "Kost"
last_name = "Shab"
email = "kot@mail.rut"
age ="99"
salary = "5000"
department = "Cat"



driver.find_element(By.ID, value='addNewRecordButton').click()
driver.find_element(By.ID, value='firstName').send_keys(first_name)
driver.find_element(By.ID, value='lastName').send_keys(last_name)
driver.find_element(By.ID, value='userEmail').send_keys(email)
driver.find_element(By.ID, value='age').send_keys(age)
driver.find_element(By.ID, value='salary').send_keys(salary)
driver.find_element(By.ID, value='department').send_keys(department)
driver.find_element(By.ID, value='submit').click()

time.sleep(3)

driver.find_element(By.ID, value='edit-record-1').click()
driver.find_element(By.ID, value='firstName').clear()
driver.find_element(By.ID, value='firstName').send_keys(first_name)
driver.find_element(By.ID, value='lastName').clear()
driver.find_element(By.ID, value='lastName').send_keys(last_name)
driver.find_element(By.ID, value='userEmail').clear()
driver.find_element(By.ID, value='userEmail').send_keys(email)
driver.find_element(By.ID, value='age').clear()
driver.find_element(By.ID, value='age').send_keys(age)
driver.find_element(By.ID, value='salary').clear()
driver.find_element(By.ID, value='salary').send_keys(salary)
driver.find_element(By.ID, value='department').clear()
driver.find_element(By.ID, value='department').send_keys(department)
driver.find_element(By.ID, value='submit').click()

time.sleep(3)

driver.find_element(By.ID, value='delete-record-3').click()

time.sleep(3)