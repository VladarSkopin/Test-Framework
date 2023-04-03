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
    #return driver
    yield driver
    driver.close()


def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):  # This will return the Browser value to the "setup" method
    return request.config.getoption('--browser')


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