import unittest #adding framework jadi output lebih jelas
from selenium import webdriver
from selenium.webdriver.common.by import By #library untuk cari element
from selenium.webdriver.common.keys import Keys #library untuk input key
from pageObject.saucePage import loginPage, loginData
import sauceBaseLogin

class SaucedemoTest(unittest.TestCase):
    
    def setUp(self): #setUp adalah function awal jangan dirubah
        self.browser = webdriver.Firefox() #untuk define browser apa yg digunakan
    
    #def b_register(self):
       # browser = self.browser
       # browser.get('https://demowebshop.tricentis.com/')
       # self.assertIn('Demo Web Shop', self.browser.title)
       # browser.quit()

    def test_a_login_success(self):
        browser = self.browser
        browser.get(loginData.url)
        self.assertIn(loginData.title, self.browser.title)
        browser.find_element(By.NAME, loginPage.user).send_keys(loginData.user_valid)
        browser.find_element(By.NAME, loginPage.psw).send_keys(loginData.pass_valid)
        browser.find_element(By.ID, loginPage.login_btn).click()
        url = browser.current_url
        self.assertEqual(url, loginData.url_login)
        browser.quit()
    
    def test_b_login_locked(self):
        sauceBaseLogin.test_baseLoginFailed(self,loginData.user_locked,loginData.pass_valid,loginData.msg_locked)
        
    def test_c_login_failed_wrong_user(self):
        sauceBaseLogin.test_baseLoginFailed(self, loginData.user_wrong, loginData.pass_valid, loginData.msg_match)
    
    def test_d_login_failed_wrong_password(self):
        sauceBaseLogin.test_baseLoginFailed(self,loginData.user_valid,loginData.pass_invalid,loginData.msg_match)
        
    def test_e_login_failed_empty_user(self):
        sauceBaseLogin.test_baseLoginFailed(self,"",loginData.pass_valid,loginData.msg_user_req)

    def test_f_login_failed_empty_pass(self):
        sauceBaseLogin.test_baseLoginFailed(self,loginData.user_valid,"",loginData.msg_pass_req)

if __name__ == "__main__":
    unittest.main()