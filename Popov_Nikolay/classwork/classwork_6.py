from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from Popov_Nikolay.classwork.helpers.main.telegram_link import LINK_telegram
from Popov_Nikolay.classwork.helpers.operations import data
from Popov_Nikolay.classwork.selectors.blog import LINK_BLOG
from Popov_Nikolay.classwork.selectors.catalog_page import LINK_CATALOG
from Popov_Nikolay.classwork.selectors.contacts import LINK_CONTACTS
from Popov_Nikolay.classwork.selectors.designers import LINK_DESIGNERS
from Popov_Nikolay.classwork.selectors.main_page import MAIN_PAGE
from Popov_Nikolay.classwork.selectors.projects_page import LINK_PROJECTS

driver = webdriver.Chrome()
driver.get("https://Artmas.by")
driver.maximize_window()
#driver.set_window_position(800, 0)
# driver.set_window_size(550, 886)
time.sleep(3)
catalog = driver.find_element(By.XPATH, LINK_CATALOG)
catalog.click()
time.sleep(2)
projects = driver.find_element(By.XPATH, LINK_PROJECTS)
projects.click()
time.sleep(2)
designers = driver.find_element(By.XPATH, LINK_DESIGNERS)
designers.click()
time.sleep(2)
blog = driver.find_element(By.XPATH, LINK_BLOG)
blog.click()
time.sleep(2)
contacts = driver.find_element(By.XPATH, LINK_CONTACTS)
contacts.click()
time.sleep(2)
telegram = driver.find_element(By.XPATH, LINK_telegram)
telegram.click()
time.sleep(2)
page_tel = driver.switch_to.window(driver.window_handles[1])
main_page = driver.find_element(By.XPATH, MAIN_PAGE)
main_page.click()
title_2 = driver.find_element(By.XPATH, '//div[@class="b24-widget-button-icon-container"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//a[@class="b24-widget-button-social-item b24-widget-button-openline_livechat"]').click()
time.sleep(1)

for i in data:
    driver.find_element(By.XPATH, '//textarea[@class="bx-im-textarea-input"]').send_keys(i)
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[@class="bx-im-textarea-send-button bx-im-textarea-send-button-bright-arrow"]').click()
    time.sleep(6)



