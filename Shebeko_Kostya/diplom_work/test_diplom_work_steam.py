import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Shebeko_Kostya.diplom_work.locator_steam.games.games_locator import game_steam, add_game_basket, open_basket, \
    basket
from Shebeko_Kostya.diplom_work.locator_steam.main.locator_main import steam_search_game


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_steam_search(driver):
    # 1. Открываем главную страницу
    driver.get("https://steampowered.com")
    search_input = driver.find_element(By.XPATH, value=steam_search_game)
    search_game = "Portal 2"
    search_input.send_keys(search_game)
    search_input.send_keys(Keys.RETURN)
    first_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".search_result_row .title"))
    )

    assert search_game in first_result.text
    print(f"Тест пройден: Игра '{first_result.text}' найдена!")


def test_steam_basket(driver):
    driver.get("https://steampowered.com")
    search_game_steam = driver.find_element(By.XPATH, value=steam_search_game)
    search_game_basket = "Windrose"
    search_game_steam.send_keys(search_game_basket)
    search_game_steam.send_keys(Keys.RETURN)
    driver.find_element(By.XPATH, value=game_steam).click()
    driver.find_element(By.XPATH, value=add_game_basket).click()
    driver.find_element(By.XPATH, value=open_basket).click()
    actual_game_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, basket))
    )
    game_in_basket = actual_game_element.text

    assert search_game_basket.lower() in game_in_basket.lower()
    print(f"Ожидали {search_game_basket}, но в корзине {game_in_basket}")


