import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    return driver
