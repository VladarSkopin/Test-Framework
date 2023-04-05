from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from basic_enums import HomePageLocators


class HomePage:

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10, 0.4)

    def click_logout_button(self) -> None:
        """This function will find logout button and click on it"""
        # HomePageLocators.xpath_logout_btn leads to "TypeError: ... is not JSON serializable"
        logout_btn: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Logout']")),
            'logout button')
        logout_btn.click()

    def click_dashboard_tab(self) -> None:
        """This function will find the Dashboard tab and click on it"""
        dashboard_tab: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.xpath_tab_dashboard)),
            'dashboard tab')
        dashboard_tab.click()

    def click_catalog_tab(self) -> None:
        """This function will find the Catalog tab and click on it"""
        catalog_tab: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.xpath_tab_catalog)),
            'catalog tab')
        catalog_tab.click()

    def click_sales_tab(self) -> None:
        """This function will find the Sales tab and click on it"""
        sales_tab: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.xpath_tab_sales)),
            'sales tab')
        sales_tab.click()

    def click_customers_tab(self) -> None:
        """This function will find the Customers tab and click on it"""
        customers_tab: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.xpath_tab_customers)),
            'customers tab')
        customers_tab.click()

    def click_promotions_tab(self) -> None:
        """This function will find the Promotions tab and click on it"""
        promotions_tab: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.xpath_tab_promotions)),
            'promotions tab')
        promotions_tab.click()

    def click_content_management_tab(self) -> None:
        """This function will find the Content Management tab and click on it"""
        content_management_tab: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.xpath_tab_content_management)),
            'content management tab')
        content_management_tab.click()

    def click_configuration_tab(self) -> None:
        """This function will find the Configuration tab and click on it"""
        configuration_tab: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.xpath_tab_configuration)),
            'configuration tab')
        configuration_tab.click()

    def click_system_tab(self) -> None:
        """This function will find the System tab and click on it"""
        system_tab: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.xpath_tab_system)),
            'system tab')
        system_tab.click()

    def click_reports_tab(self) -> None:
        """This function will find the Reports tab and click on it"""
        reports_tab: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.xpath_tab_reports)),
            'reports tab')
        reports_tab.click()

    def click_help_tab(self) -> None:
        """This function will find the Help tab and click on it"""
        help_tab: WebElement = self.wait.until(
            EC.presence_of_element_located((By.XPATH, HomePageLocators.xpath_tab_help)),
            'system tab')
        help_tab.click()

    def alert_accept(self) -> None:
        """This function switches the driver to alert window and accepts it"""
        alert_window = self.driver.switch_to.alert
        alert_window.accept()

    def alert_dismiss(self) -> None:
        """This function switches the driver to alert window and dismisses it"""
        alert_window = self.driver.switch_to.alert
        alert_window.dismiss()
