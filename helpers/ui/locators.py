from enum import unique
from selenium.webdriver.common.by import By


@unique
class LoginLocators:
    css_email_input = (By.CSS_SELECTOR, 'input[class="email valid"]')
    css_password_input = (By.CSS_SELECTOR, 'input[class="password"]')
    css_checkbox = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    css_login_btn = (By.CSS_SELECTOR, 'button')
    xpath_logout_btn = (By.XPATH, "//a[text()='Logout']")
