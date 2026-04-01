from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get(("https://demoqa.com/webtables"))
time.sleep(1)

def counter_employees(num):
    table = driver.find_element(
        By.XPATH, '//table[@class="-striped -highlight table table-striped table-bordered table-hover"]')
    row_count = len(table.find_elements(By.TAG_NAME, 'tr')) - 1
    assert row_count == num, 'Not in 4 row'

def delete_employee():
    driver.find_element(By.XPATH, '//span[@id="delete-record-4"]').click()
    time.sleep(1)


def add_new_employee(first_name, last_name, email, age, salary, department):
    add_button = driver.find_element(By.XPATH, '//button[@id="addNewRecordButton"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@id="firstName"]').send_keys(first_name)
    driver.find_element(By.XPATH, '//input[@id="lastName"]').send_keys(last_name)
    driver.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys(email)
    driver.find_element(By.XPATH, '//input[@id="age"]').send_keys(age)
    driver.find_element(By.XPATH, '//input[@id="salary"]').send_keys(salary)
    driver.find_element(By.XPATH, '//input[@id="department"]').send_keys(department)
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()
    time.sleep(1)
    counter_employees(4)
    delete_employee()
    time.sleep(1)


add_new_employee(
    'Nikolay',
    'Popov',
    'test_name@gmail.com',
    39,
    6000,
    'AQA Engineer'
)
counter_employees(3)