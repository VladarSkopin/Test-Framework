import time
from datetime import datetime
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from helpers.config_reader import ConfigReader
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage


class TestHomepage:

    base_url: str = ConfigReader.get_url()
    email_data: str = ConfigReader.get_email()
    password_data: str = ConfigReader.get_password()

    @pytest.mark.smoke
    @pytest.mark.ui
    def test_homepage_tabs(self, setup, logger):
        logger.info(f"***** test_homepage_tabs *****     {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        driver: WebDriver = setup
        logger.info(f'BASE URL: {self.base_url}')
        logger.info(f'EMAIL DATA: {self.email_data}')
        logger.info(f'PASSWORD DATA: {self.password_data}')
        driver.get(self.base_url)
        driver.maximize_window()
        login_page = LoginPage(driver=driver)
        login_page.type_in_email(email=self.email_data)
        login_page.type_in_password(password=self.password_data)
        login_page.click_login_button()
        home_page = HomePage(driver=driver)
        logger.info(f'clicking on "Dashboard" tab...')
        home_page.click_dashboard_tab()  # to fold back the tab
        logger.info(f'clicking on "Catalog" tab...')
        home_page.click_catalog_tab()
        time.sleep(1)  # time to take screenshot of the unfolded tab
        driver.save_screenshot('screenshots/home_page_catalog_tab.png')
        home_page.click_catalog_tab()  # to fold back the tab
        logger.info(f'clicking on "Sales" tab...')
        home_page.click_sales_tab()
        time.sleep(1)  # time to take screenshot of the unfolded tab
        driver.save_screenshot('screenshots/home_page_sales_tab.png')
        home_page.click_sales_tab()  # to fold back the tab
        logger.info(f'clicking on "Customers" tab...')
        home_page.click_customers_tab()
        time.sleep(1)  # time to take screenshot of the unfolded tab
        driver.save_screenshot('screenshots/home_page_customers_tab.png')
        home_page.click_customers_tab()  # to fold back the tab
        logger.info(f'clicking on "Promotions" tab...')
        home_page.click_promotions_tab()
        time.sleep(1)  # time to take screenshot of the unfolded tab
        driver.save_screenshot('screenshots/home_page_promotions_tab.png')
        home_page.click_promotions_tab()  # to fold back the tab
        logger.info(f'clicking on "Content management" tab...')
        home_page.click_content_management_tab()
        time.sleep(1)  # time to take screenshot of the unfolded tab
        driver.save_screenshot('screenshots/home_page_content_management_tab.png')
        home_page.click_content_management_tab()  # to fold back the tab
        logger.info(f'clicking on "Configuration" tab...')
        home_page.click_configuration_tab()
        time.sleep(1)  # time to take screenshot of the unfolded tab
        driver.save_screenshot('screenshots/home_page_configuration_tab.png')
        home_page.click_configuration_tab()  # to fold back the tab
        logger.info(f'clicking on "System" tab...')
        home_page.click_system_tab()
        time.sleep(1)  # time to take screenshot of the unfolded tab
        driver.save_screenshot('screenshots/home_page_system_tab.png')
        home_page.click_system_tab()  # to fold back the tab
        logger.info(f'clicking on "Reports" tab...')
        home_page.click_reports_tab()
        time.sleep(1)  # time to take screenshot of the unfolded tab
        driver.save_screenshot('screenshots/home_page_reports_tab.png')
        home_page.click_reports_tab()  # to fold back the tab
        logger.info(f'clicking on "Help" tab...')
        home_page.click_help_tab()
        time.sleep(1)  # time to take screenshot of the unfolded tab
        driver.save_screenshot('screenshots/home_page_help_tab.png')
        home_page.click_help_tab()  # to fold back the tab
        home_page.click_logout_button()

    @pytest.mark.regression
    @pytest.mark.ui
    def test_homepage_add_customer(self, setup, logger):
        logger.info(f"***** test_homepage_tabs *****     {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        driver: WebDriver = setup
        logger.info(f'BASE URL: {self.base_url}')
        logger.info(f'EMAIL DATA: {self.email_data}')
        logger.info(f'PASSWORD DATA: {self.password_data}')
        driver.get(self.base_url)
        driver.maximize_window()
        login_page = LoginPage(driver=driver)
        login_page.type_in_email(email=self.email_data)
        login_page.type_in_password(password=self.password_data)
        login_page.click_login_button()
        home_page = HomePage(driver=driver)
        logger.info(f'clicking on "Customers" tab...')
        home_page.click_customers_tab()
        logger.info(f'clicking on "Customers" option...')
        home_page.click_customers_option()
        home_page.click_add_customer_button()


