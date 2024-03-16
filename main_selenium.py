import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from os import getenv
from dotenv import load_dotenv


def clicker_cather(driver: webdriver.Chrome, value):
    try:
        value.click()
    except selenium.common.exceptions.StaleElementReferenceException:
        pass
    finally:
        new_url = driver.current_url
        return new_url


def get_source(driver: webdriver.Chrome, url: str):
    driver.get(url)
    source = driver.page_source
    return source


def get_map_site(driver: webdriver.Chrome, url: str):
    driver.get(url)
    map_site = driver.find_element(By.LINK_TEXT, 'Карта сайта')
    new_url = clicker_cather(driver, value=map_site)
    return new_url


def map_menu_choice(user_choice, driver: webdriver.Chrome, url: str):
    driver.get(url)
    value_url = ''

    if user_choice == 'Расписание':
        value = driver.find_element(By.LINK_TEXT, f'{user_choice}')
        value_url = clicker_cather(driver, value)
    return value_url


def login(url: str, login: str, password: str):
    driver = webdriver.Chrome()
    driver.get(url)
    assert 'Platonus' in driver.title
    log = driver.find_element(By.NAME, 'login')
    pword = driver.find_element(By.ID, 'pass_input')
    submit = driver.find_element(By.ID, 'Submit1')
    log.clear()
    pword.clear()

    try:
        log.send_keys(login + Keys.RETURN)
        pword.send_keys(password + Keys.RETURN)
        submit.click()
    except selenium.common.exceptions.StaleElementReferenceException:
        pass
    finally:
        new_url = driver.current_url

    map_url = get_map_site(driver, new_url)

    menu_item = map_menu_choice('Расписание', driver=driver, url=map_url)

    chosen_item_source = get_source(driver, menu_item)

    driver.close()

    return chosen_item_source


if __name__ == '__main__':
    load_dotenv()
    url = 'https://edu2.aues.kz'
    username = getenv('LOGIN')
    password = getenv('password')

    html_code = login(url, username, password)

    soup = BeautifulSoup(html_code, 'html.parser')

    weekdays = soup.find_all(name='h5', class_='card-title')

    print(html_code)
