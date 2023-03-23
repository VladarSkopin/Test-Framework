from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon

from basic_enums import BasicLocators


class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10, 0.4)

    def type_in_email(self, email: str) -> None:
        email_box: WebElement = self.wait.until(ExCon.presence_of_element_located(BasicLocators.css_email_input), 'email box')
        email_box.send_keys(email)

    def type_in_password(self, password: str) -> None:
        password_box: WebElement = self.wait.until(ExCon.presence_of_element_located(BasicLocators.css_password_input), 'password box')
        password_box.send_keys(password)

    def click_login_button(self) -> None:
        login_btn: WebElement = self.wait.until(ExCon.presence_of_element_located(BasicLocators.css_login_btn), 'login button')
        login_btn.click()
