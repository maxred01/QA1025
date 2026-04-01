import random
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By # Класс для поиска элементов по различным локаторам
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.maximize_window()
driver.get


driver.get('https://belbet.by/games')  # переходим на сайт
time.sleep(25)
action.move_by_offset(450, 370).click().perform()
time.sleep(6)
action.move_by_offset(150, 0).click().perform()
time.sleep(9)
action.move_by_offset(620, 318).click().perform()
time.sleep(12)
action.move_by_offset(36, 127).click().perform()
time.sleep(10)

driver.close()
driver.quit()
