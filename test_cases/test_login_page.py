from datetime import datetime
import pytest
from selenium.webdriver.firefox.webdriver import WebDriver

from helpers.config_reader import ConfigReader
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage


class TestLoginPage:
    # logger: Logger = CustomLogger.get_logger()

    base_url: str = ConfigReader.get_url()
    email_data: str = ConfigReader.get_email()
    password_data: str = ConfigReader.get_password()

    @pytest.mark.smoke
    @pytest.mark.ui
    def test_homepage_title(self, setup, logger):
        logger.info(f"***** test_homepage_title *****     {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        driver: WebDriver = setup
        logger.info(f'BASE URL: {self.base_url} \n')
        driver.get(self.base_url)
        assert driver.title == 'Your store. Login', 'title does not match "Your store. Login"'
        driver.save_screenshot('screenshots/login_page.png')

    @pytest.mark.smoke
    @pytest.mark.ui
    def test_login(self, setup, logger):
        logger.info(f"***** test_login *****     {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        driver: WebDriver = setup
        logger.info(f'BASE URL: {self.base_url}')
        logger.info(f'EMAIL DATA: {self.email_data}')
        logger.info(f'PASSWORD DATA: {self.password_data} \n')
        driver.get(self.base_url)
        login_page = LoginPage(driver=driver)
        login_page.type_in_email(email=self.email_data)
        login_page.type_in_password(password=self.password_data)
        login_page.click_login_button()
        home_page = HomePage(driver=driver)
        assert driver.title == 'Dashboard / nopCommerce administration',\
            'title does not match "Dashboard / nopCommerce administration"'
        driver.save_screenshot('screenshots/dashboard_page.png')
        home_page.click_logout_button()
