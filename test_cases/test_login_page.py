from selenium.webdriver.firefox.webdriver import WebDriver

from page_objects.login_page import LoginPage
from test_data.login_data import base_url, email_data, password_data


class TestLoginPage:

    def test_homepage_title(self, setup):
        self.driver: WebDriver = setup
        self.driver.get(base_url)
        assert self.driver.title == 'Your store. Login', 'title does not match "Your store. Login"'
        self.driver.save_screenshot('screenshots/login_page.png')
        self.driver.close()

    def test_login(self, setup):
        self.driver: WebDriver = setup
        self.driver.get(base_url)
        self.login_page = LoginPage(driver=self.driver)
        self.login_page.type_in_email(email=email_data)
        self.login_page.type_in_password(password=password_data)
        self.login_page.click_login_button()
        assert self.driver.title == 'Dashboard / nopCommerce administration', 'title does not match "Dashboard / nopCommerce administration"'
        self.driver.save_screenshot('screenshots/dashboard_page.png')
        self.driver.close()
