# WebApp Automation Framework Using Selenium and Python

This is a Webapp Automation Framework created using Selenium-webdriver and Python. This framework is created using pytest framework with Selenium-webdriver.

Directory structure of the framework.

```
├── base
│   ├── __init__.py
│   ├── selenium_driver.py
│   ├── webdriver_factory.py
├── configfiles
│   └── __init__.py
├── framework.log
├── geckodriver.log
├── pages
│   ├── home
│   │   ├── __init__.py
│   │   ├── login_page.py
│   ├── __init__.py
├── screenshots
├── tests
│   ├── home
│   │   ├── conftest.py
│   │   ├── geckodriver.log
│   │   ├── __init__.py
│   │   ├── login_tests.py
│   │   └── __pycache__
│   ├── __init__.py
└── utilities
    ├── __init__.py
    ├── my_logger.py
    
```
To use the framework, go to home directory. Execute pytest command as below.

>>**pytest -s -v tests/home/login_tests.py --browser firefox**

Following is a sample output of the execution.
```
jayant@jayant-ThinkPad-L440:/storage/Selenium/py-sel/mock-UI$ pytest -s -v tests/home/login_tests.py --browser firefox
============================================================= test session starts =============================================================
platform linux2 -- Python 2.7.12, pytest-3.1.0, py-1.4.33, pluggy-0.4.0 -- /usr/bin/python
cachedir: .cache
metadata: {'Python': '2.7.12', 'Platform': 'Linux-4.4.0-78-generic-x86_64-with-Ubuntu-16.04-xenial', 'Packages': {'py': '1.4.33', 'pytest': '3.1.0', 'pluggy': '0.4.0'}, 'JAVA_HOME': '/opt/jdk/jdk1.8.0_45/', 'Plugins': {'html': '1.14.2', 'metadata': '1.5.0'}}
rootdir: /storage/Selenium/py-sel/mock-UI, inifile:
plugins: html-1.14.2, metadata-1.5.0
collected 1 items 

tests/home/login_tests.py::LoginTests::testValidLogin Running class level setup.
Running method level setup.
PASSEDRunning method level teardown.
Running class level teardown.


========================================================== 1 passed in 11.33 seconds ==========================================================
jayant@jayant-ThinkPad-L440:/storage/Selenium/py-sel/mock-UI$
```
