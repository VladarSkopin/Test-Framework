import logging
import pytest
from logging import Logger, StreamHandler
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
    yield driver
    driver.close()


def pytest_addoption(parser) -> None:  # This will get the value from CLI / hooks
    parser.addoption('--browser')
    parser.addoption('--loglevel')


@pytest.fixture()
def browser(request: FixtureRequest) -> str:  # This will return the Browser value to the "setup" method
    return request.config.getoption('--browser')


@pytest.fixture(scope="session")
def logger(request: FixtureRequest) -> Logger:
    logger: Logger = logging.getLogger('alex_logger')
    formatter = logging.Formatter("{asctime} {levelname} {name} {message}", style='{')
    if logger.hasHandlers():
        logger.handlers.clear()
    handler: StreamHandler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    levels: dict[str, int] = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "critical": logging.CRITICAL
    }
    level_option: str = request.config.getoption("--loglevel")
    level: int = levels.get("debug") if level_option is None else levels.get(request.config.getoption("--loglevel").lower())
    logger.setLevel(level)
    return logger
