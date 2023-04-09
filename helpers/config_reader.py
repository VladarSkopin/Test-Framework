import configparser

config = configparser.RawConfigParser()
config.read(r'D:\GitHubProjects\Test-Framework\configs\config.ini')


class ConfigReader:

    @staticmethod
    def get_url() -> str:
        url: str = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_email() -> str:
        username: str = config.get('common info', 'email_data')
        return username

    @staticmethod
    def get_password() -> str:
        password: str = config.get('common info', 'password_data')
        return password

    @staticmethod
    def get_first_name() -> str:
        first_name: str = config.get('common info', 'first_name')
        return first_name

    @staticmethod
    def get_last_name() -> str:
        last_name: str = config.get('common info', 'last_name')
        return last_name

    @staticmethod
    def get_birth_date() -> str:
        birth_date: str = config.get('common info', 'date_of_birth')
        return birth_date

    @staticmethod
    def get_company_name() -> str:
        company_name: str = config.get('common info', 'company_name')
        return company_name

    @staticmethod
    def get_newsletter_option() -> str:
        newsletter_option: str = config.get('common info', 'newsletter_select_option')
        return newsletter_option

    @staticmethod
    def get_customer_role_option() -> str:
        customer_role_option: str = config.get('common info', 'customer_role_select_option')
        return customer_role_option

    @staticmethod
    def get_manager_of_vendor_option() -> str:
        manager_option: str = config.get('common info', 'manager_of_vendor_select_option')
        return manager_option

    @staticmethod
    def get_admin_comment() -> str:
        admin_comment: str = config.get('common info', 'admin_comment')
        return admin_comment
