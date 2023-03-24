import configparser

config = configparser.RawConfigParser()
config.read(r'D:\GitHubProjects\Test-Framework\configs\config.ini')


class ConfigReader:

    @staticmethod
    def get_url():
        url = config.get('common info', 'base_url')
        return url

    @staticmethod
    def get_email():
        username = config.get('common info', 'email_data')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password_data')
        return password
