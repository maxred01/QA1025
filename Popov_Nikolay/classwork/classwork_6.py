from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://Artmas.by")
driver.maximize_window()
#driver.set_window_position(800, 0)
# driver.set_window_size(550, 886)
time.sleep(3)
driver.find_element(By.XPATH, '//a[@href="/contacts"]').click()
time.sleep(2)
title = driver.find_element(By.XPATH,
                    '//div[@class="js-block-header-title t-section__title t-title t-title_xs t-align_left "]')
time.sleep(2)
title_2 = driver.find_element(By.XPATH,
                    "//div[@field='btitle' and contains(text(),'Арт-пространство')]")
driver.execute_script("arguments[0].scrollIntoView(true);", title_2)

print(title.text)
print(title.get_attribute("field"))
print(title_2.text)
