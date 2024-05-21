import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.saucedemo.com/v1/')

class SaucedemoTest(unittest.Testcase):
    
    def setUp(self):
        self.browser = webdriver.Firefox
        browser.get('https://www.saucedemo.com/')


if __name__ == "__main__":
    unittest.main()