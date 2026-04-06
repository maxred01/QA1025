import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from Shebeko_Kostya.class_work.helpers_steam.login.helpers_login import data_login_steam
from Shebeko_Kostya.class_work.locator_steam.login.locator_login import btn_login_steam
from Shebeko_Kostya.class_work.locator_steam.main.locator_main import btn_enter, btn_change_language

driver = webdriver.Chrome()

driver.get('https://store.steampowered.com/')
driver.maximize_window()
print(driver.find_element(By.XPATH, value=btn_change_language).text)
print(driver.find_element(By.XPATH, value=btn_enter).get_attribute('href'))

driver.find_element(By.XPATH, value=btn_enter).click()
driver.find_element(By.XPATH, value=btn_login_steam).send_keys(data_login_steam)
time.sleep(5)




