from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExCon


class LoginPage:
    css_email_input = 'input[class="email valid"]'
    css_password_input = 'input[class="password"]'
    css_checkbox = 'input[type="checkbox"]'
    css_login_btn = 'button'
    xpath_logout_btn = "//a[text()='Logout']"
    xpath_header = '//h1'

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10, 0.4)

    def type_in_email(self, email: str) -> None:
        header_element: WebElement = self.wait.until(ExCon.presence_of_element_located((By.XPATH, self.xpath_header)), 'header element')
        header_element.click()
        email_box: WebElement = self.wait.until(ExCon.visibility_of_element_located((By.CSS_SELECTOR, self.css_email_input)),
                                                'email box')
        email_box.clear()
        email_box.send_keys(email)

    def type_in_password(self, password: str) -> None:
        password_box: WebElement = self.wait.until(
            ExCon.presence_of_element_located((By.CSS_SELECTOR, self.css_password_input)), 'password box')
        password_box.clear()
        password_box.send_keys(password)

    def click_login_button(self) -> None:
        login_btn: WebElement = self.wait.until(ExCon.presence_of_element_located((By.CSS_SELECTOR, self.css_login_btn)),
                                                'login button')
        login_btn.click()
