'''
Created on 08-Jun-2017

@author: jayant
'''
from base.selenium_driver import SeleniumDriver
import utilities.my_logger as ml
import logging
from traceback import print_stack

class TestStatus(SeleniumDriver):
    
    log = ml.myLogger(logging.INFO)
    
    def __init__(self, driver):
        SeleniumDriver.__init__(self, driver)
        self.resultList = []
    
    def setResult(self, result, message):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASSED")
                    self.log.info("Verification Successful : " + message)
                else:
                    self.resultList.append("FAILED")
                    self.log.error("Verification Failed : " + message)
                    self.getScreenshot(message)
            else:
                self.resultList.append("FAILED")
                self.log.error("Verification Failed : " + message)
                self.getScreenshot(message)
        except:
            self.resultList.append("FAILED")
            self.log.error("Exception occurred!")
            self.getScreenshot(message)
            print_stack()
            
    def mark(self, result, message):
        """
        Mark the result of the verification in a test case
        """
        self.setResult(result, message)
        
    def markFinal(self, testName, result, message):
        """
        Mark the final result of the verification in a test case. This is the final status.
        """
        self.setResult(result, message)
        if "FAILED" in self.resultList:
            self.log.error(testName + " Test Failed.")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " Test Passed.")
            self.resultList.clear()
            assert True == True
            