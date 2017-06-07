'''
Created on 07-Jun-2017

@author: jayant
'''
import pytest
from selenium import webdriver
from base.webdriver_factory import WebDriverFactory

@pytest.yield_fixture()
def setUp():
    print("Running method level setup.")
    yield
    print("Running method level teardown.")

@pytest.yield_fixture(scope="class")
def classSetUp(request, browser):
    print("Running class level setup.")
    wf = WebDriverFactory(browser)
    driver = wf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running class level teardown.")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
