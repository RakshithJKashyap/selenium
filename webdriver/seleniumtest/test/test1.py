from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("G:/coders_club/python/webdriver/seleniumtest/drivers/chromedriver.exe")
driver.set_page_load_timeout("10")
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("instagram")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()
