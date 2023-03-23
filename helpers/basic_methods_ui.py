from __future__ import annotations

from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon
from typing import Optional, Any


class BasicMethods:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_inner_text(element: WebElement) -> str:
        """Function returns 'innerText' attribute of an element"""
        return element.get_attribute('innerText')

    def get_element_text(self, locator: tuple[str, str], driver: Optional[WebDriver | WebElement] = None,
                         message: Optional[str | Any] = None, waiting_time: int = 10) -> str:
        """Function searches for the element and returns the element's 'innerText' attribute"""
        return self.get_inner_text(
            self.get_element_present(locator=locator, driver=driver, message=message, waiting_time=waiting_time))

    @staticmethod
    def get_value(element: WebElement) -> str:
        """Function returns the element's 'value' attribute"""
        return element.get_attribute('value')

    def get_element_value(self, locator: tuple[str, str], driver: Optional[WebDriver | WebElement] = None,
                          message: Optional[str | Any] = None, waiting_time: int = 10) -> str:
        """Function searches for the element and returns its 'value' attribute"""
        return self.get_value(
            self.get_element_present(locator=locator, driver=driver, message=message, waiting_time=waiting_time))

    def get_element_present(self, locator: tuple[str, str], driver: Optional[WebDriver | WebElement] = None,
                            message: Optional[str | Any] = None, waiting_time: int = 10) -> WebElement:
        """Function searches for the element present on the webpage and returns it"""
        driver = self.driver if not driver else driver
        message = f'Element not found by locator "{locator}"' if not message else message
        return WebDriverWait(driver, waiting_time).until(ExCon.presence_of_element_located(locator), message=message)

    def get_list_of_elements_present(self, locator: tuple[str, str], driver: Optional[WebDriver | WebElement] = None,
                                     message: Optional[str | Any] = None, waiting_time: int = 10) -> list[WebElement]:
        """Function searches for elements present on the webpage and returns them"""
        driver = self.driver if not driver else driver
        message = f'Elements not found by locator "{locator}"' if not message else message
        return WebDriverWait(driver, waiting_time).until(ExCon.presence_of_all_elements_located(locator),
                                                         message=message)

    def check_all_elements_missing(self, locator: tuple[str, str], driver: Optional[WebDriver | WebElement] = None,
                                   message: Optional[str | Any] = None, waiting_time: int = 10) -> list[bool]:
        """Function checks for elements not present on the webpage"""
        driver = self.driver if not driver else driver
        message = f'At least one element was found by locator "{locator}"' if not message else message
        return WebDriverWait(driver, waiting_time).until_not(ExCon.presence_of_all_elements_located(locator),
                                                             message=message)

    def check_element_stale(self, element: WebElement, driver: Optional[WebDriver | WebElement] = None,
                            message: Optional[str | Any] = None, waiting_time: int = 10) -> bool:
        """Function checks for stale element on the webpage"""
        driver = self.driver if not driver else driver
        message = f'Element is not stale' if not message else message
        return WebDriverWait(driver, waiting_time).until_not(ExCon.staleness_of(element),
                                                             message=message)

    def get_element_clickable(self, locator: tuple[str, str], driver: Optional[WebDriver | WebElement] = None,
                              message: Optional[str | Any] = None, waiting_time: int = 10) -> WebElement:
        """Function searches for clickable element on the webpage and returns it"""
        driver = self.driver if not driver else driver
        message = f'Element is found by locator "{locator}" is not clickable' if not message else message
        return WebDriverWait(driver, waiting_time).until_not(ExCon.element_to_be_clickable(locator),
                                                             message=message)

    def get_element_visible(self, locator: tuple[str, str], driver: Optional[WebDriver | WebElement] = None,
                            message: Optional[str | Any] = None, waiting_time: int = 10) -> WebElement:
        """Function searches for the element visible on the webpage and returns it"""
        driver = self.driver if not driver else driver
        message = f'Element found by locator "{locator}" is not visible' if not message else message
        return WebDriverWait(driver, waiting_time).until(ExCon.visibility_of_element_located(locator), message=message)

    def get_element_not_visible(self, locator: tuple[str, str], driver: Optional[WebDriver | WebElement] = None,
                                message: Optional[str | Any] = None, waiting_time: int = 10) -> WebElement:
        """Function searches for the element not visible on the webpage and returns it"""
        driver = self.driver if not driver else driver
        message = f'Element found by locator "{locator}" is visible' if not message else message
        return WebDriverWait(driver, waiting_time).until_not(ExCon.visibility_of_element_located(locator),
                                                             message=message)

    def get_list_of_visible_elements(self, locator: tuple[str, str], driver: Optional[WebDriver | WebElement] = None,
                                     message: Optional[str | Any] = None, waiting_time: int = 10) -> list[WebElement]:
        """Function searches for visible elements on the webpage and returns them"""
        driver = self.driver if not driver else driver
        message = f'Elements found by locator "{locator}" are not visible' if not message else message
        return WebDriverWait(driver, waiting_time).until(ExCon.visibility_of_all_elements_located(locator),
                                                         message=message)

    def url_contains(self, url: str, driver: Optional[WebDriver | WebElement] = None,
                     message: Optional[str | Any] = None, waiting_time: int = 10) -> bool:
        """Function checks out URL of the page"""
        driver = self.driver if not driver else driver
        message = f'Current URL does not contain expected "{url}"' if not message else message
        return WebDriverWait(driver, waiting_time).until(ExCon.url_contains(url),
                                                         message=message)

    def get_url(self, url: str) -> BasicMethods:
        """Function lets to go to a specified URL"""
        self.driver.get(url)
        self.url_contains(url)
        return self

    def drag_and_drop_to_elem(self, source: WebElement, target: WebElement) -> None:
        """Function drags an element to another element and drops it"""
        ActionChains(self.driver).drag_and_drop(source=source, target=target).perform()

    def refresh_page(self) -> BasicMethods:
        """Function refreshes the webpage"""
        self.driver.refresh()
        return self

    def back_page(self, url: str) -> BasicMethods:
        """Function goes back one step in the browser history"""
        self.driver.back()
        self.url_contains(url)
        return self

    def accept_alert(self, driver: Optional[WebDriver | WebElement] = None, message: Optional[str | Any] = None, waiting_time: int = 10) -> None:
        """Function accepts the alert window"""
        driver = self.driver if not driver else driver
        message = 'No alert window was found' if not message else message
        WebDriverWait(driver, waiting_time).until(ExCon.alert_is_present(), message=message)
        driver.switch_to.alert.accept()

    def open_last_tab(self) -> None:
        """Function switches to the last tab in the browser window"""
        self.driver.switch_to.window(self.driver.window_handles[-1])
