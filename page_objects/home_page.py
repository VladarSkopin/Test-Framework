from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
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
            EC.presence_of_element_located(HomePageLocators.xpath_btn_logout.value),
            'logout button')
        logout_btn.click()

    def click_dashboard_tab(self) -> None:
        """This function will find the Dashboard tab and click on it"""
        dashboard_tab: WebElement = self.wait.until(
            EC.element_to_be_clickable(HomePageLocators.xpath_tab_dashboard.value),
            'dashboard tab')
        ActionChains(self.driver).move_to_element(dashboard_tab).click(dashboard_tab).perform()

    def click_catalog_tab(self) -> None:
        """This function will find the Catalog tab and click on it"""
        catalog_tab: WebElement = self.wait.until(
            EC.element_to_be_clickable(HomePageLocators.xpath_tab_catalog.value),
            'catalog tab')
        ActionChains(self.driver).move_to_element(catalog_tab).click(catalog_tab).perform()

    def click_sales_tab(self) -> None:
        """This function will find the Sales tab and click on it"""
        sales_tab: WebElement = self.wait.until(
            EC.element_to_be_clickable(HomePageLocators.xpath_tab_sales.value),
            'sales tab')
        ActionChains(self.driver).move_to_element(sales_tab).click(sales_tab).perform()

    def click_customers_tab(self) -> None:
        """This function will find the Customers tab and click on it"""
        customers_tab: WebElement = self.wait.until(
            EC.element_to_be_clickable(HomePageLocators.xpath_tab_customers.value),
            'customers tab')
        ActionChains(self.driver).move_to_element(customers_tab).click(customers_tab).perform()

    def click_promotions_tab(self) -> None:
        """This function will find the Promotions tab and click on it"""
        promotions_tab: WebElement = self.wait.until(
            EC.element_to_be_clickable(HomePageLocators.xpath_tab_promotions.value),
            'promotions tab')
        ActionChains(self.driver).move_to_element(promotions_tab).click(promotions_tab).perform()

    def click_content_management_tab(self) -> None:
        """This function will find the Content Management tab and click on it"""
        content_management_tab: WebElement = self.wait.until(
            EC.element_to_be_clickable(HomePageLocators.xpath_tab_content_management.value),
            'content management tab')
        ActionChains(self.driver).move_to_element(content_management_tab).click(content_management_tab).perform()

    def click_configuration_tab(self) -> None:
        """This function will find the Configuration tab and click on it"""
        configuration_tab: WebElement = self.wait.until(
            EC.element_to_be_clickable(HomePageLocators.xpath_tab_configuration.value),
            'configuration tab')
        ActionChains(self.driver).move_to_element(configuration_tab).click(configuration_tab).perform()

    def click_system_tab(self) -> None:
        """This function will find the System tab and click on it"""
        system_tab: WebElement = self.wait.until(
            EC.element_to_be_clickable(HomePageLocators.xpath_tab_system.value),
            'system tab')
        ActionChains(self.driver).move_to_element(system_tab).click(system_tab).perform()

    def click_reports_tab(self) -> None:
        """This function will find the Reports tab and click on it"""
        reports_tab: WebElement = self.wait.until(
            EC.element_to_be_clickable(HomePageLocators.xpath_tab_reports.value),
            'reports tab')
        ActionChains(self.driver).move_to_element(reports_tab).click(reports_tab).perform()

    def click_help_tab(self) -> None:
        """This function will find the Help tab and click on it"""
        help_tab: WebElement = self.wait.until(
            EC.element_to_be_clickable(HomePageLocators.xpath_tab_help.value),
            'system tab')
        ActionChains(self.driver).move_to_element(help_tab).click(help_tab).perform()

    def click_customers_option(self) -> None:
        """This function will find the Customers option and click on it"""
        customers_option: WebElement = self.wait.until(
            EC.presence_of_element_located(HomePageLocators.xpath_option_customers.value),
            'system tab')
        customers_option.click()

    def click_add_customer_button(self) -> None:
        """This function will find the button to add new customers and click on it"""
        add_customer_btn: WebElement = self.wait.until(
            EC.presence_of_element_located(HomePageLocators.css_btn_add_customer.value),
            'system tab')
        add_customer_btn.click()

    def alert_accept(self) -> None:
        """This function switches the driver to alert window and accepts it"""
        alert_window = self.driver.switch_to.alert
        alert_window.accept()

    def alert_dismiss(self) -> None:
        """This function switches the driver to alert window and dismisses it"""
        alert_window = self.driver.switch_to.alert
        alert_window.dismiss()
