# pip install selenium
#  then web driver in mycase for chrome(chromedriver.exe)
#  https://sites.google.com/a/chromium.org/chromedriver/downloads
# https://chromedriver.chromium.org/downloads
# copy chromedriver.exe tob bin folder
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import driver


driver = webdriver.Firefox()
driver.get("https://github.com")
signin_link = driver.find_element_by_xpath("//a[@href='/Sign in']")
signin_link.click()


username_box = driver.find_element_by_id("login_field")
username_box.send_keys("Melaku05")
password_box = driver.find_element_by_id("password")
password_box.send_keys("Boge11@#melaku@#@#")
password_box.submit()
