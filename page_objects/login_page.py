from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
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
            EC.presence_of_element_located((By.XPATH, LoginPageLocators.xpath_header.value)), 'header element')
        header_element.click()  # to move the mouse cursor out of the input box
        email_box: WebElement = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LoginPageLocators.css_email_input.value)),
            'email box')
        email_box.clear()
        email_box.send_keys(email)

    def type_in_password(self, password: str) -> None:
        """This function will find the password box WebElement and fill in the password info"""
        password_box: WebElement = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LoginPageLocators.css_password_input.value)),
            'password box')
        password_box.clear()
        password_box.send_keys(password)

    def click_login_button(self) -> None:
        """This function will find  """
        login_btn: WebElement = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LoginPageLocators.css_login_btn.value)),
            'login button')
        login_btn.click()
