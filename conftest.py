import logging
import pytest
from logging import Logger
from _pytest.fixtures import FixtureRequest
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
    #return driver
    yield driver
    driver.close()


def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):  # This will return the Browser value to the "setup" method
    return request.config.getoption('--browser')


@pytest.fixture(scope="session")
def logger(request: FixtureRequest) -> Logger:
    logger: Logger = logging.getLogger('alex_logger')
    formatter = logging.Formatter("{asctime} {levelname} {name} {message}", style='{')
    if logger.hasHandlers():
        logger.handlers.clear()
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    levels = {"debug": logging.DEBUG, "info": logging.INFO, "warning": logging.WARNING, "critical": logging.CRITICAL}
    # level = levels.get(request.config.getoption("--loglevel").lower())
    level = levels.get("info")
    logger.setLevel(level)
    return logger

'''
def pytest_configure(config):
    """The hook for adding environment info to HTML report"""
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Alex'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    """The hook for deleting / modifying environment info for HTML report"""
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
'''