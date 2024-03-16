import requests
from bs4 import BeautifulSoup
import json
import errors

main_url = 'https://edu2.aues.kz'

custom_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept-Language': 'en-GB,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,en-US;q=0.6'
}


def get_session():
    session = requests.Session()
    return session
git

def login_user(login: str, password: str):
    session = get_session()
    session.headers.update(custom_headers)

    payload = {'login': login,
               'password': password
               }

    payload = json.dumps(payload)

    base_url = '/rest/api/login'

    response = session.post(url=main_url + base_url, headers=custom_headers, data=payload)
    return response


if __name__ == '__main__':
    values = login_user('d.nurdaulet@aues.kz', 'R3Bx@U3R')

    print(values.text)
