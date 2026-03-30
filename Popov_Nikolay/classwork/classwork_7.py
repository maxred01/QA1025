import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
# driver.get('https://demoqa.com/text-box')
# driver.maximize_window()
# time.sleep(2)
# full_name = driver.find_element(By.ID, 'userName')
# full_name.send_keys('Николай Попов')
#
# email = driver.find_element(By.ID, 'userEmail')
# email.send_keys('test_normal@gmail.com')
#
# current_address = driver.find_element(By.ID, 'currentAddress')
# current_address.send_keys('ул. Тестировщиков 35')
#
# permanent_address = driver.find_element(By.ID, 'permanentAddress')
# permanent_address.send_keys('ул. Толстовых 27')
#
# submit = driver.find_element(By.ID, 'submit')
# submit.click()
# time.sleep(1)
#
# name = driver.find_element(By.ID, 'name')
# name = name.text[-len('Николай Попов'):]
# em = driver.find_element(By.ID, 'email')
# em = em.text[-len('test_normal@gmail.com'):]
# cur_address = driver.find_element(By.XPATH, "//p[@id='currentAddress']")
# cur = cur_address.text[-len('ул. Тестировщиков 35'):]
# per_address = driver.find_element(By.XPATH, "//p[@id='permanentAddress']")
# per = per_address.text[-len('ул. Великанов 35'):]
#
#
# assert name == 'Николай Попов'
# assert em == 'test_normal@gmail.com'
# assert cur == 'ул. Тестировщиков 35'
# assert per == 'ул. Толстовых 27'
#
# assert name.find(name) != 1


# driver.get('https://demoqa.com/checkbox')
# time.sleep(1)
# driver.find_element(By.XPATH, '//div[@class="check-box-tree-wrapper"]//span[@class="rc-tree-switcher rc-tree-switcher_close"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//div[@class="check-box-tree-wrapper"]//span[@class="rc-tree-switcher rc-tree-switcher_close"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//div[@class="rc-tree-treenode rc-tree-treenode-switcher-close rc-tree-treenode-leaf-last rc-tree-treenode-leaf"]//span[@class="rc-tree-checkbox"]').click()
# time.sleep(1)
# element = driver.find_element(By.XPATH, '//div[@id="result"]//span[@class="text-success"]').text
#
# assert element == 'commands'


# driver.get('https://demoqa.com/radio-button')
# driver.find_element(By.XPATH, '//input[@id="impressiveRadio"]').click()
# time.sleep(2)
# element = driver.find_element(By.XPATH, '//p[@class="mt-3"]//span[@class="text-success"]').text
# assert element == 'Impressive'

actions = ActionChains(driver)
driver.get('https://demoqa.com/buttons')
actions.double_click(double_click = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')).perform()
actions.context_click(right_click_me = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]'))
actions.click_me(click_me = driver.find_element(By.XPATH, '//button[@id="s2DUf"]'))
