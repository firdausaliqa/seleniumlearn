import unittest #adding framework jadi output lebih jelas
from selenium import webdriver
from selenium.webdriver.common.by import By #library untuk cari element
from selenium.webdriver.common.keys import Keys #library untuk input key

class SaucedemoTest(unittest.TestCase):
    
    def a_setUp(self):
        self.browser = webdriver.Firefox() #untuk define browser apa yg digunakan

    def b_register(self):
        browser = self.browser
        browser.get('https://demowebshop.tricentis.com/')
        self.assertIn('Demo Web Shop', self.browser.title)

if __name__ == "__main__":
    unittest.main()