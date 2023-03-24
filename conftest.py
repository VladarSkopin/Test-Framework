import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome()  # Chrome is the default browser
    return driver


def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):  # This will return the Browser value to the "setup" method
    return request.config.getoption('--browser')
