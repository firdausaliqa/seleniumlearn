import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://demowebshop.tricentis.com/')

class SaucedemoTest(unittest.Testcase):
    
    def setUp(self):
        self.browser = webdriver.Firefox
        browser.get('https://demowebshop.tricentis.com/')
        elem = browser.find_element(By.ID, '')


if __name__ == "__main__":
    unittest.main()