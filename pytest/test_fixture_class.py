import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='class')
def init_driver(request):
    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver
    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def init_ff_driver(request):
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


@pytest.mark.usefixtures("init_driver")
class Base_Chrome_test:
    pass
class Test_google_chrome(Base_Chrome_test):
    def test_google_title_ch(self):
        self.driver.get("http://www.google.com")

