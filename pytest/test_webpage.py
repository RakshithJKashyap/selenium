from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.google.com')
    assert driver.title == "Google"
    time.sleep(4)
    driver.quit()


def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.facebook.com')
    assert driver.title == "Facebook - log in or sign up"
    time.sleep(4)
    driver.quit()


def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.gmail.com')
    assert driver.title == "Gmail"
    time.sleep(4)
    driver.quit()


def test_rediff():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.rediff.com')
    time.sleep(4)
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
    driver.quit()
    
