from enum import unique, Enum
from selenium.webdriver.common.by import By


class BaseEnum(Enum):

    @classmethod
    def get_all_values(cls):
        """Get the list of all BaseEnum values"""
        return [x.value for x in cls]


@unique
class BasicLocators(BaseEnum):
    css_email_input = (By.CSS_SELECTOR, 'input[class="email valid"]')
    css_password_input = (By.CSS_SELECTOR, 'input[class="password"]')
    css_checkbox = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    css_login_btn = (By.CSS_SELECTOR, 'button')
    xpath_logout_btn = (By.XPATH, "//a[text()='Logout']")
