'''
Created on 26-May-2017

@author: jayant
'''
import inspect
import logging

def myLogger(logLevel=logging.DEBUG):
    
    
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("framework.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger