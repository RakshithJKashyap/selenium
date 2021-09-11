from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

PATH = "G:/coders_club/python/webdriver/selenium/webdriver/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://techwithtim.net")
link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,"Beginner Python Tutorials")))
    element.click()
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"sow-button-19310003")))
    element.click()
    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()
except:
    driver.quit()






'''
driver.get("https://www.google.com")
search = driver.find_element_by_name('q')
search.send_keys("Instagram")
search.send_keys(Keys.RETURN)
name = driver.find_element_by_link_text('Instagram')
'''
