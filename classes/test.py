
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUbuntuHomepage(unittest.TestCase):

    def setUp(self):
        print "hello firest"
        #self.driver = webdriver.Remote(desired_capabilities={
        #   "browserName": "firefox"
        #})

        capabilities = DesiredCapabilities.FIREFOX
        self.driver = webdriver.Remote("http://localhost:4444/wd/hub",capabilities)
        #self.driver = webdriver("http://172.16.205.129:4444", "firefox", "ANY")
        print "hello"

    def testTitle(self):
        print "i am  atest"
        self.browser.get('http://www.ubuntu.com/')
        self.assertIn('Ubuntu', self.browser.title)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

