'''
Created on Apr 20, 2015

@author: mabassi
This file sets up the driver & tears it down... 
'''
import unittest
from selenium import webdriver
from configobj import ConfigObj
from classes import loginController
import time,sys
from classes import Result
from StringIO import StringIO

class seleniumDriver(unittest.TestCase):
   
    
    '''def setUp(self):
        sauce_url = "http://muzamilabbasi:1c963e98-ce3e-4a2b-844a-50346dd63ddc@ondemand.saucelabs.com:80/wd/hub"
        config = ConfigObj('C:\Python27\Scripts\PythonSelenium\setup.cfg')
        config = ConfigObj('/usr/local/bin/setup.cfg')
        browser = config['nosetests']['browser']
        site = config['nosetests']['site']
        env = config['nosetests']['environment']
        
        desired_capabilities = {
                                'platform': "Windows 8",
                                'browserName': "firefox",
                                'version': "32",
                                }

        self.driver = webdriver.Remote(desired_capabilities=desired_capabilities,command_executor=sauce_url)
        self.driver.implicitly_wait(10)
        url = 'https://rams-'+env+'.'+site+'.com'
        self.driver.get(url)
        self.login = loginController.loginController(self.driver)
        self.login.login()
        self.driver.maximize_window()
        self.startTime = time.time()
        return self.driver'''
        
    def setUp(self):
        config = ConfigObj('../setup.cfg')
        #config = ConfigObj('/usr/local/bin/setup.cfg')
        browser = config['nosetests']['browser']
        
        site = config['nosetests']['site']
        env = config['nosetests']['environment']
        
        if (browser == "Chrome"):
            self.driver = webdriver.Chrome('c:\chromedriver')
            
        elif (browser == "Firefox"):
            self.driver = webdriver.Firefox()
        
        elif (browser == "PhantomJs"):
            self.driver = webdriver.PhantomJS('../phantomjs-1.9.2-macosx/bin/phantomjs')
        else:
            raise Exception("Define your browser") 
        
        url = 'https://rams-'+env+'.'+site+'.com'
        self.driver.get(url)
        self.driver.implicitly_wait(10)    
        self.login = loginController.loginController(self.driver)
        self.login.login()
        self.driver.maximize_window()
        self.startTime = time.time()
        
        
        
        return self.driver
    
    
        
    '''def setUp(self):
        desired_cap = {'browser': 'Firefox', 'browser_version': '32.0', 'os': 'OS X', 'os_version': 'Yosemite', 'resolution': '1024x768' , 'browserstack.local': True}

        #config = ConfigObj('C:\Python27\Scripts\PythonSelenium\setup.cfg')
        config = ConfigObj('/usr/local/bin/setup.cfg')
        browser = config['nosetests']['browser']
        site = config['nosetests']['site']
        env = config['nosetests']['environment']


        self.driver = webdriver.Remote(command_executor='http://muzamilabbasi1:hViA1ywjK1FHK41d46d9@hub.browserstack.com:80/wd/hub',
        desired_capabilities=desired_cap)
        
        
        self.driver.implicitly_wait(10)
        url = 'https://rams-'+env+'.'+site+'.com'
        self.driver.get(url)
        self.login = loginController.loginController(self.driver)
        self.login.login()
        self.driver.maximize_window()
        self.startTime = time.time()
        return self.driver'''
    
    
    def tearDown(self):
        result_list = []
        #self.driver.save_screenshot('../screenshots/failureScreenshot')
        print "TearDown"
        #read the nosetest.xml file
        
        
        
        self.endTime = time.time()
        result = self._resultForDoCleanups
        resultString = str(result)
       
        run =  resultString[45:46]
        errors = resultString[54:55]
        fails = resultString[65:66]
        
    
        result = sys.exc_info()
        #result_list = [run,errors,fails]
        
        print self._resultForDoCleanups
        result = Result.Result(result)
        result.save(self)
        time.sleep(20)
        
        self.driver.quit()
    
    if __name__ == "__main__":
        unittest.main()
