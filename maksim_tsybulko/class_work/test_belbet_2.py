import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.maximize_window()
driver.get('https://belbet.by/games')
time.sleep(25)
action.move_by_offset(450, 370).click().perform()
time.sleep(6)
action.move_by_offset(150, 0).click().perform()
time.sleep(6)
action.move_by_offset(1400, 700).click().perform()
time.sleep(6)


driver.close()
driver.quit()
