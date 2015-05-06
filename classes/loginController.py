from selenium import webdriver
import unittest



class loginController(unittest.TestCase):
    
    def __init__(self,driver):

        self.driver = driver
      
    def login(self):
        username = self.driver.find_element_by_id("username")
        username.clear()
        username.send_keys("mabassi")
        password = self.driver.find_element_by_id("password")
        password.clear()
        password.send_keys("123456")
        loginButton = self.driver.find_element_by_xpath("//*[@id='contents']/form/div/button")
        #loginButton = self.driver.find_element_by_xpath("//*[@id='contents']/form/div/p[4]/button")
        loginButton.click()
    

    
