import time

import pytest

from POM.Orange_Login_Page import Login_page
from Utilities.ReadProperties import ReadConfig
from Utilities import XlUtils
from Utilities.Logging import LogGenerator


@pytest.mark.DDT
class Test_orangeHRM_DDT:
    url = ReadConfig.get_url_orange()
    file_name = 'D:\\Classes\\Demo_practice\\TestData\\test_data.xlsx'
    sheet_name = 'demo_data'
    row_count = XlUtils.get_row_count(file_name, sheet_name)
    log = LogGenerator.loggen()
    result_list = []
    screenshot_path = 'D:\\Classes\\Demo_practice\\Screenshots'

    def test_orangehrm_login_ddt_003(self, setup):
        self.driver = setup
        self.log.info('************** test_orangehrm_login_DDT_003 ***************** ')
        self.driver.get(self.url)
        self.log.info('Orange HRM URL opened ')
        self.driver.maximize_window()
        self.lp = Login_page(self.driver)
        time.sleep(3)

        for r in range(2, self.row_count+1):
            username = XlUtils.readdata(self.file_name, self.sheet_name, r, 1)
            password = XlUtils.readdata(self.file_name, self.sheet_name, r, 2)
            expected_result = XlUtils.readdata(self.file_name, self.sheet_name, r, 3)

            self.lp.get_username(username)
            self.log.info(f'Username --> {username}  entered')
            self.lp.get_password(password)
            self.log.info(f'password --> {password}  entered')
            time.sleep(2)
            self.lp.click_login_button()
            time.sleep(2)
            self.log.info('clicking on Login Button')

            if self.lp.login_status() == True:
                if expected_result == 'Pass':
                    self.result_list.append('Pass')
                    self.lp.click_profile_button()
                    self.driver.save_screenshot(self.screenshot_path+'\\loginsucessfull.png')
                    self.log.info('clicking on profile Button')
                    self.lp.click_logout_button()
                    time.sleep(2)
                    self.log.info('Clicking on Logout button')
                    self.log.info('Login passed with Valid credentials')
                else:
                    self.result_list.append('Fail')
                    self.lp.click_profile_button()
                    self.log.info('clicking on profile Button')
                    self.lp.click_logout_button()
                    time.sleep(2)
                    self.log.info('Clicking on Logout button')
                    self.log.info('Login passed with Invalid credentials')

            else:
                if expected_result == 'Fail':
                    self.log.info('Login Failed with invalid credentials')
                    self.driver.save_screenshot(self.screenshot_path+'\\loginfailed.png')
                    self.result_list.append('Pass')
                else:
                    self.log.critical('Login passed with invalid credentials')
                    self.driver.save_screenshot(self.screenshot_path + '\\loginwithinvalid.png')
                    self.result_list.append('Fail')

        if 'Fail' in self.result_list:
            assert False
        else:
            assert True

        self.driver.quit()







