'''
Created on 02-Jun-2017

@author: jayant
'''
from base.selenium_driver import SeleniumDriver
import utilities.my_logger as ml
import logging

class LoginPage(SeleniumDriver):
    
    log = ml.myLogger(logging.DEBUG)

    def __init__(self, driver):
        #super().__init__(driver)
        SeleniumDriver.__init__(self, driver)
        self.driver = driver

    # Locators
    _email_field = "email"
    _password_field = "pass"
    _login_button = "u_0_q"
       
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button)

    def login(self, email="", password=""):       
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        
    def verifyLoginSuccesful(self):
        result = self.isElementPresent("//*//span[text()='Jayant']", locatorType="xpath")
        return result
    
    def verifyLoginFailure(self):
        result = self.isElementPresent("//div[contains(text(),'Incorrect password')]", locatorType="xpath")
        return result