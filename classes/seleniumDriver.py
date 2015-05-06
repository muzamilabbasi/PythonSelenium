'''
Created on Apr 20, 2015

@author: mabassi
This file sets up the driver & tears it down... 
'''
import unittest
from selenium import webdriver
from configobj import ConfigObj
from classes import loginController


class seleniumDriver(unittest.TestCase):
   
   
    def setUp(self):
        
        config = ConfigObj('/usr/local/bin/setup.cfg')
        browser = config['nosetests']['browser']
        site = config['nosetests']['site']
        env = config['nosetests']['environment']
        
        if (browser == "Chrome"):
            self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
            
        elif (browser == "PhantomJs"):
            self.driver = webdriver.Firefox()
        
        #elif (browser == "PhantomJs"):
         #   self.driver = webdriver.PhantomJS('../phantomjs-1.9.2-macosx/bin/phantomjs')
            
            
        url = 'https://rams-'+env+'.'+site+'.com'
        self.driver.get(url)
        self.driver.implicitly_wait(10)    
        self.login = loginController.loginController(self.driver)
        self.login.login()
        self.driver.maximize_window()
        return self.driver
        
    def tearDown(self):
        self.driver.save_screenshot('screenshot')
        self.driver.quit()
    
    if __name__ == "__main__":
        unittest.main()