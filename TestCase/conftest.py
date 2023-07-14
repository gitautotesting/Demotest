import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', help='Valid options are chrome, edge, firefox')


@pytest.fixture
def browser(request):
    return request.config.getoption('--browser')


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print('Chrome browser initiated')
    elif browser == 'edge':
        driver = webdriver.Edge()
        print('Edge browser initiated')
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print('Firefox browser initiated')
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('Headless')
        driver = webdriver.Chrome(options=chrome_options)
    return driver



