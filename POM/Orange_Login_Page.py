from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException as ec
from selenium.webdriver.support import expected_conditions as ex
from selenium.webdriver.support.ui import WebDriverWait


class Login_page:

    text_username_Name = By.NAME, 'username'
    text_password_name = By.NAME, 'password'
    button_login_xpath = By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    button_profile_xpath = By.XPATH, '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p'
    button_logout_xpath = By.XPATH, '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'

    def __init__(self, driver):
        self.driver = driver

    def get_username(self, username):
        self.driver.find_element(*Login_page.text_username_Name).send_keys(username)

    def get_password(self, password):
        self.driver.find_element(*Login_page.text_password_name).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*Login_page.button_login_xpath).click()

    def click_profile_button(self):
        self.driver.find_element(*Login_page.button_profile_xpath).click()

    def click_logout_button(self):
        self.driver.find_element(*Login_page.button_logout_xpath).click()

    def login_status(self):
        self.driver.implicitly_wait(3)
        try:
            self.driver.find_element(*Login_page.button_profile_xpath)
            return True
        except ec:
            return False
