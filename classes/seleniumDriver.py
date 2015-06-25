'''
Created on Apr 20, 2015

@author: mabassi
This file sets up the driver & tears it down... 
'''
import unittest
from selenium import webdriver
from configobj import ConfigObj
<<<<<<< Updated upstream
from classes import loginController


class seleniumDriver(unittest.TestCase):
   
   
    def setUp(self):
        
        config = ConfigObj('/usr/local/bin/setup.cfg')
=======
from classes import loginController, worker
import time,sys,platform
from classes import Result
from StringIO import StringIO
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

class seleniumDriver(unittest.TestCase):
        
    def setUp(self):
        if (sys.platform == "darwin"):
            config = ConfigObj('/usr/local/bin/setup.cfg')
        elif (sys.platform == "win32"):
            config = ConfigObj('C:\setup.cfg')    
>>>>>>> Stashed changes
        browser = config['nosetests']['browser']
        site = config['nosetests']['site']
        env = config['nosetests']['environment']
        
        if (browser == "Chrome"):
            self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
            
<<<<<<< Updated upstream
=======
        elif (browser == "Firefox"):
            
            fp = webdriver.FirefoxProfile()
            fp.set_preference("browser.cache.disk.enable", False)
            fp.set_preference("browser.cache.memory.enable",False)
            fp.set_preference("browser.cache.offline.enable",False)
            fp.set_preference("network.http.use-cache",False)
            
            #driver = webdriver.Firefox(firefox_profile=fp)

            self.driver = webdriver.Firefox(firefox_profile=fp)
        
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        return self.driver
        
    def tearDown(self):
        self.driver.save_screenshot('screenshot')
=======
        self.startTime = time.strftime("%H:%M:%S")
        return self.driver
    
    def tearDown(self):
        '''self.endTime = time.strftime("%H:%M:%S")  
        result = sys.exc_info()
        result = Result.Result(result)
        result.save(self)
        sessionEnd = worker.worker()
        sessionEnd.unlockSession(self.driver.session_id,"unlocksession")
        '''
>>>>>>> Stashed changes
        self.driver.quit()
    
    if __name__ == "__main__":
        unittest.main()
