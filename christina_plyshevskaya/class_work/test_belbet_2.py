import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get('https://belbet.by/games')
driver.maximize_window()
time.sleep(25)
action.move_by_offset(450, 370).click().perform() #молния
time.sleep(5)
action.move_by_offset(150, 0).click().perform() #игра
time.sleep(10)
action.move_by_offset(641, 329).click().perform() #штучка для авто
time.sleep(5)
action.move_by_offset(25, 125).click().perform() #20попыток
time.sleep(5)

time.sleep(10)
# driver.find_element(By.XPATH, '//div[contains(text(), "Меню")]').click()
# time.sleep(3)
# driver.find_element(By.XPATH, '//a[@href="/games"]').click()
# time.sleep(30)

driver.close()
driver.quit()