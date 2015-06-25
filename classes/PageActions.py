from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re, datetime


class PageActions(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver
       
    '''this function is Waits for an element to be found,'''    
    def assert_elementPresent(self, how, what):
        try:
<<<<<<< Updated upstream
            wait = WebDriverWait(self.driver,5)
=======
            wait = WebDriverWait(self.driver,60)
>>>>>>> Stashed changes
            wait.until(EC.presence_of_element_located((how,what)))
            return True
        except:
            return False
        
    ''''Not in use'''
    def assert_ExpectedConditions(self,how,what):
        if self.driver.find_element(by=how, value=what).is_displayed():
            return True
        else:
            return False
    
    '''this function is universal for finding elements, but only it does it finds'''        
    def assert_ElementIsPresent(self,how,what):
        if self.assert_elementPresent(how,what):
            return self.driver.find_element(by=how,value=what)
    
    
    '''generic functions'''
    
    def find_ElementByName(self,a):    
        return self.driver.find_element_by_name(a)
    
    def find_ElementByID(self,id): 
        return self.driver.find_element_by_id(id)
    
    def find_ElementByTagName(self,tag): 
        return self.driver.find_element_by_tag_name(tag)
        
    def find_ElementByLinkText(self,text):
        return self.driver.find_element_by_link_text(text)
    
    def find_ElementByCssSelector(self,selector):
        return self.driver.find_element_by_css_selector(selector)
    
    
    
    '''page related functions'''
    def typeElementName(self,how,what,text):
        time.sleep(1)
        if self.assert_elementPresent(how,what):
            self.find_ElementByName(what).send_keys(text)
    
    def clickElementTagName(self, how, what):
        time.sleep(1)
        if self.assert_elementPresent(how,what):
            self.find_ElementByTagName(what).click()
        
    def submitForm(self,how,what):
        time.sleep(1)
        if self.assert_elementPresent(how,what):
            self.find_ElementByTagName(what).submit()
    
    def clickElementLinkText(self,how,what):
        time.sleep(1)             
        if self.assert_elementPresent(how,what):
            self.find_ElementByLinkText(what).click()
            
    def submitButtonCssSelector(self,how,what):
        time.sleep(1)             
        if self.assert_elementPresent(how,what):
            self.find_ElementByCssSelector(what).click()
    
    def verifyElementLinkText(self,how,what):
        time.sleep(1)             
        if self.assert_elementPresent(how,what):
            element = self.find_ElementByLinkText(what)
            #print element
            return self.find_ElementByLinkText(what)
        
    def clickElementID(self,how,what):
        time.sleep(1)             
        if self.assert_elementPresent(how,what):
            self.find_ElementByID(what).click()
    
    def clickElementCss(self,how,what):
        time.sleep(1)             
        if self.assert_elementPresent(how,what):
            self.find_ElementByCssSelector(what).click()
            
    '''helper functions'''
            
    def switchNewWindows(self,how,what):
        driver = self.driver
        currentwindows = driver.window_handles # set of windows already open
        # the code that opens the new window
        if self.assert_elementPresent(how, what):
            findElement = self.assert_ElementIsPresent(how, what)
            findElement.click()
            
        newwindows = driver.window_handles # 1 extra window shows up here.
        newwindow = list(set(newwindows) - set(currentwindows))[0]
        driver.switch_to_window(newwindow)
        time.sleep(3)
    
    def switchCurrentWindows(self):
        driver = self.driver
        currentwindows = driver.window_handles # set of windows already open
        newscreen = currentwindows[0]
        driver.switch_to_window(newscreen)
        time.sleep(15)
        
  