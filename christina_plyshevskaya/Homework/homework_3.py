import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

#первое задание
driver = webdriver.Chrome()

driver.get('https://demoqa.com/radio-button')
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@for="yesRadio"]').click()
assert driver.find_element(By.ID, 'yesRadio').is_selected()
text_message = driver.find_element(By.XPATH, '//p[@class="mt-3"]')
yes_span = text_message.find_element(By.CSS_SELECTOR, 'span.text-success')
full_message = f'You have selected {yes_span.text}'
print(full_message)
time.sleep(2)

driver.find_element(By.XPATH, '//*[@for="impressiveRadio"]').click()
assert driver.find_element(By.ID, 'impressiveRadio').is_selected()
text_message = driver.find_element(By.XPATH, '//p[@class="mt-3"]')
impressive_span = text_message.find_element(By.CSS_SELECTOR, 'span.text-success')
full_message = f'You have selected {impressive_span.text}'
print(full_message)
time.sleep(2)

driver.find_element(By.XPATH, '//*[@for="noRadio"]')
assert driver.find_element(By.ID, 'noRadio').is_enabled() == False
if not driver.find_element(By.ID, 'noRadio').is_enabled():
    print('No radio button is disabled')
time.sleep(2)

driver.get('https://demoqa.com/webtables')
driver.maximize_window()

#второе задание
def row_count():
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, 'span[title="Delete"]')
    return len(delete_buttons)

initial_count = row_count()
print(f'Начальное количество: {initial_count}')

#создание
count = 1
while count <= 5:
    driver.find_element(By.ID, 'addNewRecordButton').click()

    driver.find_element(By.ID, 'firstName')
    name_value = f"Милаша{count}"
    driver.find_element(By.ID, 'firstName').send_keys(name_value)

    driver.find_element(By.ID, 'lastName')
    lastname_value = "Чпокер"
    driver.find_element(By.ID, 'lastName').send_keys(lastname_value)

    driver.find_element(By.ID, 'userEmail')
    email_value = f"fdfdfdfd{count}@dsds.com"
    driver.find_element(By.ID, 'userEmail').send_keys(email_value)

    driver.find_element(By.ID, 'age')
    age_value = "18"
    driver.find_element(By.ID, 'age').send_keys(age_value)

    driver.find_element(By.ID, 'salary')
    salary_value = "10000000"
    driver.find_element(By.ID, 'salary').send_keys(salary_value)

    driver.find_element(By.ID, 'department')
    department_value = "dfgdfdf"
    driver.find_element(By.ID, 'department').send_keys(department_value)
    time.sleep(2)

    driver.find_element(By.ID, 'submit').click()
    count += 1
    time.sleep(2)

#изменение
count = 1
while count <= 3:
    driver.find_element(By.ID, f'edit-record-{count}').click()

    driver.find_element(By.ID, 'firstName').clear()
    name_value = f"Ульяша{10-(10-count)}"
    driver.find_element(By.ID, 'firstName').send_keys(name_value)

    driver.find_element(By.ID, 'lastName').clear()
    lastname_value = "Брейнротик"
    driver.find_element(By.ID, 'lastName').send_keys(lastname_value)

    driver.find_element(By.ID, 'userEmail').clear()
    email_value= f"fdfdfdfd{10-(10-count)}@dsds.com"
    driver.find_element(By.ID, 'userEmail').send_keys(email_value)

    driver.find_element(By.ID, 'age').clear()
    age_value = "20"
    driver.find_element(By.ID, 'age').send_keys(age_value)

    driver.find_element(By.ID, 'salary').clear()
    salary_value = "6767676767"
    driver.find_element(By.ID, 'salary').send_keys(salary_value)

    driver.find_element(By.ID, 'department').clear()
    department_value = "аывьалыватывоар"
    driver.find_element(By.ID, 'department').send_keys(department_value)
    time.sleep(2)

    driver.find_element(By.ID, 'submit').click()
    count += 1
    time.sleep(2)

final_count = row_count()
print(f'Итого в таблице: {final_count}')
print(f'Добавлено: {final_count - initial_count}')
time.sleep(2)

#удаление
driver.find_element(By.ID, 'delete-record-1').click()
time.sleep(2)

deleted_count = row_count()
print(f'Удалено: {final_count - deleted_count}')
time.sleep(2)

time.sleep(2)
driver.quit()
