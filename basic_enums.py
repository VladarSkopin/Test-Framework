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
    xpath_header = '//h1'


@unique
class HomePageLocators(BaseEnum):
    """Locators for HomePage"""
    css_logout_btn = "a[href$='logout']"
    xpath_logout_btn = "//a[text()='Logout']"
    xpath_tab_dashboard = "//a//p[contains(text(), 'Dashboard')]"
    xpath_tab_catalog = "//a//p[contains(text(), 'Catalog')]"
    xpath_tab_sales = "//a//p[contains(text(), 'Sales')]"
    xpath_tab_customers = "//a//p[contains(text(), 'Customers')]"
    xpath_tab_promotions = "//a//p[contains(text(), 'Promotions')]"
    xpath_tab_content_management = "//a//p[contains(text(), 'Content')]"
    xpath_tab_configuration = "//a//p[contains(text(), 'Config')]"
    xpath_tab_system = "//a//p[contains(text(), 'System')]"
    xpath_tab_reports = "//a//p[contains(text(), 'Reports')]"
    xpath_tab_help = "//a//p[contains(text(), 'Help')]"
    xpath_option_customers = "//li[@class='nav-item']//a//p[contains(text(), 'Customers')]"

