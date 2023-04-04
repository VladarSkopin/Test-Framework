from datetime import datetime

import pytest
from selenium.webdriver.firefox.webdriver import WebDriver
from logging import Logger

from helpers import excel_utils
from helpers.config_reader import ConfigReader
from helpers.custom_logger import CustomLogger
from page_objects.login_page import LoginPage


class TestLoginPage:
    # logger: Logger = CustomLogger.get_logger()
    excel_file_path: str = './/test_data/logins.xlsx'
    base_url: str = ConfigReader.get_url()

    @pytest.mark.regression
    @pytest.mark.ddt
    def test_login(self, setup, logger):
        logger.info("***** Test Login from Excel file*****")
        logger.info(f"***** test_login *****     {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        self.driver: WebDriver = setup
        logger.info(f'BASE URL: {self.base_url}')
        self.driver.get(self.base_url)
        self.login_page = LoginPage(driver=self.driver)
        rows: int = excel_utils.get_max_row(self.excel_file_path, 'Sheet1')
        status_list: list[str] = []

        for row in range(2, rows + 1):
            email_data: str = excel_utils.get_cell_data(self.excel_file_path, 'Sheet1', row_number=row, column_number=1)
            password_data: str = excel_utils.get_cell_data(self.excel_file_path, 'Sheet1', row_number=row, column_number=2)
            expected_result: str = excel_utils.get_cell_data(self.excel_file_path, 'Sheet1', row_number=row, column_number=3)

            self.login_page.type_in_email(email=email_data)
            self.login_page.type_in_password(password=password_data)
            self.login_page.click_login_button()

            expected_title: str = "Dashboard / nopCommerce administration"
            actual_title: str = self.driver.title

            if actual_title == expected_title:
                if expected_result == 'Pass':
                    logger.info(f"passed: {email_data}")
                    self.login_page.click_logout_button()
                    status_list.append("Pass")
                elif expected_result == 'Fail':
                    logger.info(f"failed: {email_data}")
                    self.login_page.click_logout_button()
                    status_list.append("Fail")

            elif actual_title != expected_title:
                if expected_result == 'Pass':
                    logger.info(f"failed: {email_data}")
                    status_list.append("Fail")
                elif expected_result == 'Fail':
                    logger.info(f"passed: {email_data}")
                    status_list.append("Pass")

        assert "Fail" not in status_list
