import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from os import getenv
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

main_url = 'https://edu2.aues.kz/index?sid=043175e87722aaff702e22fdeeb6eb61&returnUrl=%2Fv7%2F%23%2Fschedule%2FstudentView'


def login_user(login: str, password: str):
    driver = webdriver.Chrome(keep_alive=False)

    driver.get(main_url)

    try:
        login_field = driver.find_element(By.NAME, 'login')
        login_field.send_keys(login + Keys.RETURN)

        password_field = driver.find_element(By.ID, 'pass_input')
        password_field.send_keys(password + Keys.RETURN)

        login_button = driver.find_element(By.ID, 'Submit1')
        login_button.click()

    except selenium.common.exceptions.StaleElementReferenceException:
        pass

    wait = WebDriverWait(driver, 10)  # Ожидание до 10 секунд
    schedule_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'card-body')))

    page_content = driver.page_source

    driver.quit()

    return page_content


if __name__ == '__main__':
    load_dotenv()

    log = getenv('LOGIN')

    password = getenv('PASSWORD')

    values = login_user(log, password)
    # print(values)

    soup = BeautifulSoup(values, 'html.parser')

    weekdays = soup.find_all(name='h5', class_='card-title')


    print(weekdays)
