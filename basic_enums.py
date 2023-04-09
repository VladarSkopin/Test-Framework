from enum import Enum, unique

from selenium.webdriver.common.by import By


class BaseEnum(Enum):

    @classmethod
    def get_all_values(cls):
        return [x.value for x in cls]


@unique
class LoginPageLocators(BaseEnum):
    """Locators for LoginPage"""
    css_email_input = (By.CSS_SELECTOR, 'input[class="email valid"]')
    css_password_input = (By.CSS_SELECTOR, 'input[class="password"]')
    css_checkbox = (By.CSS_SELECTOR, 'input[type="checkbox"]')
    css_login_btn = (By.CSS_SELECTOR, 'button')
    xpath_header = (By.XPATH, '//h1')


@unique
class HomePageLocators(BaseEnum):
    """Locators for HomePage"""
    css_btn_logout = (By.CSS_SELECTOR, "a[href$='logout']")
    css_btn_add_customer = (By.CSS_SELECTOR, 'a[class="btn btn-primary"]')
    xpath_btn_logout = (By.XPATH, "//a[text()='Logout']")
    xpath_tab_dashboard = (By.XPATH, "//a//p[contains(text(), 'Dashboard')]")
    xpath_tab_catalog = (By.XPATH, "//a//p[contains(text(), 'Catalog')]")
    xpath_tab_sales = (By.XPATH, "//a//p[contains(text(), 'Sales')]")
    xpath_tab_customers = (By.XPATH, "//a//p[contains(text(), 'Customers')]")
    xpath_tab_promotions = (By.XPATH, "//a//p[contains(text(), 'Promotions')]")
    xpath_tab_content_management = (By.XPATH, "//a//p[contains(text(), 'Content')]")
    xpath_tab_configuration = (By.XPATH, "//a//p[contains(text(), 'Config')]")
    xpath_tab_system = (By.XPATH, "//a//p[contains(text(), 'System')]")
    xpath_tab_reports = (By.XPATH, "//a//p[contains(text(), 'Reports')]")
    xpath_tab_help = (By.XPATH, "//a//p[contains(text(), 'Help')]")
    xpath_option_customers = (By.XPATH, "//li[@class='nav-item']//a//p[contains(text(), 'Customers')]")


@unique
class AddCustomerFormLocators(BaseEnum):
    """Locators for Customer info"""
    css_save_btn = (By.CSS_SELECTOR, "button[name='save']")
    css_save_and_continue_btn = (By.CSS_SELECTOR, "button[name='save-continue']")
    xpath_email_input = (By.XPATH, "//input[@type='email']")
    xpath_password_input = (By.XPATH, "//input[@type='password']")
    xpath_first_name_input = (By.XPATH, "//input[@id='FirstName']")
    xpath_last_name_input = (By.XPATH, "//input[@id='LastName']")
    xpath_gender_male_radio_btn = (By.XPATH, "//input[@id='Gender_Male']")
    xpath_gender_female_radio_btn = (By.XPATH, "//input[@id='Gender_Female']")
    xpath_birth_date_input = (By.XPATH, "//input[@name='DateOfBirth']")
    xpath_company_name_input = (By.XPATH, "//input[@name='Company']")
    xpath_is_tax_exempt_checkbox = (By.XPATH, "//input[@name='IsTaxExempt']")
    xpath_newsletter_dropdown = (By.XPATH, "//div[@role='listbox']//input[@class='k-input k-readonly']")
    xpath_customer_roles_dropdown = (By.XPATH, "//div[@role='listbox']//input[@class='k-input']")
    xpath_manager_of_vendor_dropdown = (By.XPATH, "//select[@name='VendorId']")
    xpath_active_checkbox = (By.XPATH, "//input[@name='Active']")
    xpath_admin_comment_input = (By.XPATH, "//textarea")

