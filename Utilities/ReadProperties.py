import configparser

config = configparser.RawConfigParser()

config.read('D:\\Classes\\Demo_practice\\Configurations\\config.ini')


class ReadConfig:

    @staticmethod
    def text_data():
        testdata = config.get('test data', 'textbox')
        return testdata

    @staticmethod
    def get_url_demo():
        url = config.get('test data', 'url')
        return url

    @staticmethod
    def get_text_area_data():
        data = config.get('test data', 'text_area_data')
        return data

    @staticmethod
    def get_url_orange():
        url = config.get('orange HRM', 'url')
        return url

    @staticmethod
    def get_username():
        username = config.get('orange HRM', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('orange HRM', 'password')
        return password
