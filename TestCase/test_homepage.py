import pytest

from POM.Homepage import Homepage
from Utilities.Logging import LogGenerator
from Utilities.ReadProperties import ReadConfig



class Test_homepage:
    text_input_data = ReadConfig.text_data()
    text_area_data = ReadConfig.get_text_area_data()
    url = ReadConfig.get_url_demo()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_inputfield_001(self, setup):
        self.log.info('******** test_inputfield_001 *********')
        self.driver = setup
        self.driver.get(self.url)
        self.log.info('Opening Url : '+self.url)
        hp = Homepage(self.driver)
        hp.enter_input_text(self.text_input_data)
        self.log.info('Enter the text '+self.text_input_data + "in text box ")
        input_value = hp.get_data_text_input()

        if input_value == 'Automation':
            self.log.info('input text is validated and correct')
            self.driver.save_screenshot('D:\\Classes\\Demo_practice\\Screenshots\\test_inputfield_001.png')
            assert True
        else:
            self.log.critical(' data Validation Fail')
            self.driver.implicitly_wait(3)
            assert False
        self.driver.quit()


    def
