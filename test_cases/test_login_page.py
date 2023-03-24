from selenium.webdriver.firefox.webdriver import WebDriver

from helpers.config_reader import ConfigReader
from helpers.custom_logger import CustomLogger
from page_objects.login_page import LoginPage


class TestLoginPage:
    logger = CustomLogger.get_logger()

    base_url = ConfigReader.get_url()
    email_data = ConfigReader.get_email()
    password_data = ConfigReader.get_password()

    def test_homepage_title(self, setup):
        self.logger.info("***** TestLoginPage *****")
        self.logger.info("***** test_homepage_title *****")
        self.driver: WebDriver = setup
        self.logger.info(f'BASE URL: {self.base_url}')
        self.driver.get(self.base_url)
        assert self.driver.title == 'Your store. Login', 'title does not match "Your store. Login"'
        self.driver.save_screenshot('screenshots/login_page.png')
        self.driver.close()

    def test_login(self, setup):
        self.logger.info("***** TestLoginPage *****")
        self.logger.info("***** test_login *****")
        self.driver: WebDriver = setup
        self.logger.info(f'BASE URL: {self.base_url}')
        self.logger.info(f'EMAIL DATA: {self.email_data}')
        self.logger.info(f'PASSWORD DATA: {self.password_data}')
        self.driver.get(self.base_url)
        self.login_page = LoginPage(driver=self.driver)
        self.login_page.type_in_email(email=self.email_data)
        self.login_page.type_in_password(password=self.password_data)
        self.login_page.click_login_button()
        assert self.driver.title == 'Dashboard / nopCommerce administration',\
            'title does not match "Dashboard / nopCommerce administration"'
        self.driver.save_screenshot('screenshots/dashboard_page.png')
        self.driver.close()
