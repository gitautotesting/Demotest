import pytest

from POM.Orange_Login_Page import Login_page
from Utilities.ReadProperties import ReadConfig
from Utilities.Logging import LogGenerator


@pytest.mark.sanity
class Test_login:
    url = ReadConfig.get_url_orange()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    log = LogGenerator.loggen()

    def test_login_002(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.log.info('Opening Orange HRM URL')
        self.driver.maximize_window()
        self.log.info('Maximize window')
        self.lp = Login_page(self.driver)
        self.driver.implicitly_wait(3)
        self.lp.get_username(self.username)
        self.log.info(f'Entering Username as :  {self.username}')
        self.lp.get_password(self.password)
        self.log.info(f'Entering Password as :  {self.password}')

        self.lp.click_login_button()
        self.log.info(f'click on login button')

        if self.lp.login_status():
            self.driver.close()
            self.log.info('Login Sucessfull, Test Passed')
            assert True
        else:
            self.driver.close()
            self.log.critical('test case Failed')
            self.driver.save_screenshot('D:\\Classes\\Demo_practice\\Screenshots\\test_login_002.png')
            assert False
