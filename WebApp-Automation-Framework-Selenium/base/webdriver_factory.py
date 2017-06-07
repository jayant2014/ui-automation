'''
Created on 29-May-2017

@author: jayant
'''
from selenium import webdriver

class WebDriverFactory():
    
    def __init__(self, browser):
        self.browser = browser
        
    def getWebDriverInstance(self):
        """
        Get WebDriver instance based on the browser configuration
        Args :
            Nobe
        Returns :
            Webdriver instance
        """
        baseURL = "https://www.facebook.com"
        if self.browser == "firefox":
            firefoxPath="/storage/Selenium/py-sel/geckodriver"
            driver = webdriver.Firefox(executable_path=firefoxPath)
        elif self.browser == "chrome":
            
            driver = webdriver.Chrome()
        elif self.browser == "ie":
            driver = webdriver.Ie()
        else:
            driver = webdriver.Chrome()
        
        driver.maximize_window()
        # Driver implicit timeout for an element, change it if your connection is slow
        driver.implicitly_wait(5)
        driver.get(baseURL)
        return driver