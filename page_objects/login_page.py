from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from basic_enums import LoginPageLocators


class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10, 0.4)

    def type_in_email(self, email: str) -> None:
        """This function will find the email box WebElement and fill in the email info"""
        header_element: WebElement = self.wait.until(
            EC.presence_of_element_located(LoginPageLocators.xpath_header.value), 'header element')
        header_element.click()  # to move the mouse cursor out of the input box
        email_box: WebElement = self.wait.until(
            EC.presence_of_element_located(LoginPageLocators.css_email_input.value),
            'email box')
        email_box.clear()
        email_box.send_keys(email)

    def type_in_password(self, password: str) -> None:
        """This function will find the password box WebElement and fill in the password info"""
        password_box: WebElement = self.wait.until(
            EC.presence_of_element_located(LoginPageLocators.css_password_input.value),
            'password box')
        password_box.clear()
        password_box.send_keys(password)

    def click_login_button(self) -> None:
        """This function will find login button and click on it"""
        login_btn: WebElement = self.wait.until(
            EC.presence_of_element_located(LoginPageLocators.css_login_btn.value),
            'login button')
        login_btn.click()

    def alert_accept(self) -> None:
        """This function switches the driver to alert window and accepts it"""
        alert_window = self.driver.switch_to.alert
        alert_window.accept()

    def alert_dismiss(self) -> None:
        """This function switches the driver to alert window and dismisses it"""
        alert_window = self.driver.switch_to.alert
        alert_window.dismiss()
