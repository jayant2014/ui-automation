'''
Created on 02-Jun-2017

@author: jayant
'''
from pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("classSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, classSetUp):
        self.lp = LoginPage(self.driver)
    
    @pytest.mark.run(order=1)    
    def testValidLogin(self):

        self.lp.login("###########", "########")
        #user = driver.find_element(By.XPATH, "//*//span[text()='Jayant']")
        #if user is not None:
        #    print("Login Successful")
        #else:
        #    print("Login Failed")
        
        res = self.lp.verifyLoginSuccesful()
        assert res == True
    
    #@pytest.mark.run(order=1)
    #def testInvalidLogin(self):

    #    self.lp.login("##########", "#######")       
    #    res = self.lp.verifyLoginFailure()
    #    assert res == True
        
#ff = LoginTests()
#ff.testValidLogin()
