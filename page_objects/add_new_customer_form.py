from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from basic_enums import AddCustomerFormLocators


class AddNewCustomerForm:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10, 0.4)

    def type_in_email(self, email: str) -> None:
        email_box: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_email_input),
            'password box')
        email_box.send_keys(email)

    def type_in_password(self, password: str) -> None:
        password_box: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_password_input),
            'password box')
        password_box.send_keys(password)

    def type_in_first_name(self, first_name: str) -> None:
        first_name_text_box: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_first_name_input),
            'first name textbox')
        first_name_text_box.send_keys(first_name)

    def type_in_last_name(self, last_name: str) -> None:
        last_name_text_box: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_last_name_input),
            'last name textbox')
        last_name_text_box.send_keys(last_name)

    def click_gender_male_radio_btn(self) -> None:
        radio_btn: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_gender_male_radio_btn),
            'gender male radio button')
        radio_btn.click()

    def click_gender_female_radio_btn(self) -> None:
        radio_btn: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_gender_female_radio_btn),
            'gender female radio button')
        radio_btn.click()

    def type_in_date_of_birth(self, date_of_birth: str) -> None:
        date_box: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_birth_date_input),
            'date of birth input box')
        date_box.send_keys(date_of_birth)

    def type_in_company_name(self, company_name: str) -> None:
        company_name_text_box: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_company_name_input),
            'company name textbox')
        company_name_text_box.send_keys(company_name)

    def click_is_tax_exempt_checkbox(self) -> None:
        checkbox: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_is_tax_exempt_checkbox),
            'is tax exempt checkbox')
        checkbox.click()

    def select_newsletter_dropdown(self, select_option: str) -> None:
        dropdown: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_newsletter_dropdown),
            'newsletter dropdown')
        # password_box.send_keys(password)

    def select_customer_roles_dropdown(self, select_option: str) -> None:
        dropdown: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_customer_roles_dropdown),
            'customer roles dropdown')
        # password_box.send_keys(password)

    def select_manager_of_vendor_dropdown(self, select_option: str) -> None:
        dropdown: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_manager_of_vendor_dropdown),
            'manage of vendor dropdown')
        # password_box.send_keys(password)

    def click_active_checkbox(self) -> None:
        checkbox: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_active_checkbox),
            'is active checkbox')
        checkbox.click()

    def type_in_admin_comment(self, admin_comment: str) -> None:
        admin_comment_text_box: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.xpath_admin_comment_input),
            'admin comment textbox')
        admin_comment_text_box.send_keys(admin_comment)

    def click_save_btn(self) -> None:
        save_btn: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.css_save_btn),
            'save button')
        save_btn.click()

    def click_save_and_continue_btn(self) -> None:
        save_and_continue_btn: WebElement = self.wait.until(
            EC.presence_of_element_located(AddCustomerFormLocators.css_save_and_continue_btn),
            'save and continue button')
        save_and_continue_btn.click()
