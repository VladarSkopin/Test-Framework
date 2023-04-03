from enum import Enum, unique


class BaseEnum(Enum):

    @classmethod
    def get_all_values(cls):
        return [x.value for x in cls]


@unique
class LoginPageLocators(BaseEnum):
    """Locators for LoginPage"""
    css_email_input = 'input[class="email valid"]'
    css_password_input = 'input[class="password"]'
    css_checkbox = 'input[type="checkbox"]'
    css_login_btn = 'button'
    css_logout_btn = "a[href$='logout']"
    xpath_logout_btn = "//a[text()='Logout']"
    xpath_header = '//h1'
