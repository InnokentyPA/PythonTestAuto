import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import yaml
import requests

with open("testdata.yaml") as f:
    test_data = yaml.safe_load(f)


@pytest.fixture(scope="session")
def browser():
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def login():
    response = requests.post(test_data['url'], data={'username': test_data['username'],
                                                     'password': test_data['password']})
    response.encoding = 'utf-8'
    return response.json()['token']


@pytest.fixture()
def get_title_font_size():
    return "32px"