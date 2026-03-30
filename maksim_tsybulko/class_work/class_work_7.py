import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
#
# driver.get('https://demoqa.com/text-box')
# driver.maximize_window()
#
# user_name = 'Цыбулько Максим'
# user_email = 'test@test.com'
# current_address = 'г. Тест, ул.Тест, д.40, кв.666'
# permanent_address = 'г. Тест, ул.Тест, д.40, кв.666'
#
# driver.find_element(By.ID, 'userName').send_keys(user_name)
# driver.find_element(By.ID, 'userEmail').send_keys(user_email)
# driver.find_element(By.ID, 'currentAddress').send_keys(current_address)
# driver.find_element(By.ID, 'permanentAddress').send_keys(permanent_address)
# driver.find_element(By.ID, 'submit').click()
#
# name = driver.find_element(By.XPATH, '//p[@id="name"]').text
# email = driver.find_element(By.XPATH, '//p[@id="email"]').text
# currentAddress = driver.find_element(By.XPATH, '//p[@id="currentAddress"]').text
# permanentAddress = driver.find_element(By.XPATH, '//p[@id="permanentAddress"]').text
#
# assert permanentAddress.find(permanent_address) != -1
# assert currentAddress.find(current_address) != -1
# assert email.find(user_email) != -1
# assert name.find(user_name) != 1
#
#
# driver.get('https://demoqa.com/checkbox')
# driver.find_element(By.XPATH, '//div[@class="rc-tree-treenode rc-tree-treenode-switcher-close rc-tree-treenode-leaf-last"]//span[@class="rc-tree-switcher rc-tree-switcher_close"]').click()
# driver.find_element(By.XPATH, '(//div[@class="rc-tree-treenode rc-tree-treenode-switcher-close"]//span[@class="rc-tree-switcher rc-tree-switcher_close"])[1]').click()
# driver.find_element(By.XPATH, '//span[@aria-label="Select Notes"]').click()
# time.sleep(1)
#
# driver.get('https://demoqa.com/radio-button')
# driver.find_element(By.XPATH, '//*[@for="yesRadio"]').click()
# assert driver.find_element(By.ID, 'yesRadio').is_selected()
# time.sleep(1)
#

driver.get('https://demoqa.com/buttons')
actions = ActionChains(driver)
actions.double_click(driver.find_element(By.ID, 'doubleClickBtn')).perform()
time.sleep(2)
actions.context_click(driver.find_element(By.ID, 'rightClickBtn')).perform()
time.sleep(2)
actions.click(driver.find_element(By.ID, 'doubleClickBtn')).perform()
time.sleep(2)

