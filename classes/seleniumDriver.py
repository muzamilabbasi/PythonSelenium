'''
Created on Apr 20, 2015

@author: mabassi
This file sets up the driver & tears it down... 
'''
import unittest
from selenium import webdriver
from configobj import ConfigObj
from classes import loginController
import time
from classes import Result

class seleniumDriver(unittest.TestCase):
   
    
    def setUp(self):
        
        #config = ConfigObj('C:\Python27\Scripts\PythonSelenium\setup.cfg')
        config = ConfigObj('/usr/local/bin/setup.cfg')
        browser = config['nosetests']['browser']
        site = config['nosetests']['site']
        env = config['nosetests']['environment']
        
        if (browser == "Chrome"):
            self.driver = webdriver.Chrome('c:\chromedriver')
            
        elif (browser == "Firefox"):
            self.driver = webdriver.Firefox()
        
        #elif (browser == "PhantomJs"):
         #   self.driver = webdriver.PhantomJS('../phantomjs-1.9.2-macosx/bin/phantomjs')
            
            
        url = 'https://rams-'+env+'.'+site+'.com'
        self.driver.get(url)
        self.driver.implicitly_wait(10)    
        self.login = loginController.loginController(self.driver)
        self.login.login()
        self.driver.maximize_window()
        
        self.startTime = time.time()
        return self.driver
        
    def tearDown(self):
        self.driver.save_screenshot('screenshot')
        self.endTime = time.time()
        result = Result.Result()
        result.save(self)
        self.driver.quit()
    
    if __name__ == "__main__":
        unittest.main()
