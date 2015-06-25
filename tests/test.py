import pycurl
from urllib import urlencode
import json
from StringIO import StringIO 
from configobj import ConfigObj

import time, unittest
from classes import configurationManager as cfg
from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver, worker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.backend import AddGalleryPage as GP
import re
import sys
    

class testsShopBazzarAddItemsTest(seleniumDriver.seleniumDriver):
    
    def testAddItemsToCartInArticleBody(self):
        """Practitest id :None"""
   
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomSlugs()