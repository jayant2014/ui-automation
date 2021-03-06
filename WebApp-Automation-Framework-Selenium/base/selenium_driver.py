'''
Created on 26-May-2017

@author: jayant
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.my_logger as ml
import logging
import time
import os

class SeleniumDriver():

    log = ml.myLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        """
        Return the title of the page.
        Args : 
            None
        Returns :
            Title of the page
        """
        return self.driver.title
    
            
    def getByType(self, locatorType):
        """
        Get the element type
        Args :
            locatorType
        Returns :
            
        """        
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Failed to click on the element with locator : " + locator + " locatorType: " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Failed to send data on the element with locator : " + locator + " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found.")
                return True
            else:
                self.log.info("Element not found.")
                return False
        except:
            self.log.info("Element not found.")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found.")
                return True
            else:
                self.log.info("Element not found.")
                return False
        except:
            self.log.info("Element not found.")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException]) 
            element = wait.until(EC.element_to_be_clickable((byType, "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page.")
        except:
            self.log.info("Element not appeared on the web page.")
            print_stack()
        return element

    def getScreenshot(self, message):
        """
        Take screenshot of the current page
        """
        fileName = message + ".png"
        screenshotLocation = "../screenshots/"
        relativeFileName = screenshotLocation + fileName
        currentLocation = os.path.dirname(__file__)
        destinationFileName = os.path.join(currentLocation, relativeFileName)
        destinationLocation = os.path.join(currentLocation, screenshotLocation)
        
        try:
            if not os.path.exists(destinationLocation):
                os.makedirs(destinationLocation)
            self.driver.save_screenshot(destinationFileName)
            self.log.info("Screenshot saved to directory " + destinationFileName)
        except:
            self.log.error("Exception occurred!")
            print_stack()