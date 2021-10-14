import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class ChromeTest():
    def __init__(self):
        print("in init")

    def setupChromeTest(self):
        self.driver = webdriver.Chrome()
        self.driver. implicitly_wait(40)
        self.driver.set_page_load_timeout(50)
        self.driver.get('https://google.com')
        
    def testSearch(self):
        googleSearchBar = self.driver.find_element_by_name('q')
        googleSearchBar.clear()
        googleSearchBar.send_keys('python init')
        googleSearchBar.send_keys(Keys.RETURN)

myChromeTest = ChromeTest()
myChromeTest.setupChromeTest()
myChromeTest.testSearch()