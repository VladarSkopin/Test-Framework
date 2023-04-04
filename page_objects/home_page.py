from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from basic_enums import HomePageLocators


class HomePage:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10, 0.4)

    def click_logout_button(self) -> None:
        """This function will find logout button and click on it"""
        # HomePageLocators.xpath_logout_btn leads to "TypeError: ... is not JSON serializable"
        logout_btn: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Logout']")),
            'logout button')
        logout_btn.click()

    def alert_accept(self) -> None:
        """This function switches the driver to alert window and accepts it"""
        alert_window = self.driver.switch_to.alert
        alert_window.accept()

    def alert_dismiss(self) -> None:
        """This function switches the driver to alert window and dismisses it"""
        alert_window = self.driver.switch_to.alert
        alert_window.dismiss()
