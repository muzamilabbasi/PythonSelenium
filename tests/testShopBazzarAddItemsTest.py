import pycurl
from urllib import urlencode
import json
from StringIO import StringIO 
from configobj import ConfigObj

import time 
import unittest
from classes import configurationManager as cfg
from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver, worker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.backend import AddGalleryPage as GP
import re
import sys
from random import randint
    

class testsShopBazzarAddItemsTest(seleniumDriver.seleniumDriver):
    
    def testAddItemsToCartInArticleBody(self):
        """Practitest id :None"""
            
        config = cfg.configuration()
        getConfig = config.getConfiguration()
        self.site = getConfig['site']
        
        if (self.site == "harpersbazaar"):
            
            addArticlePage = AP.AddArticlePage(self.driver, "m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            setText = "TestHeadlines"
            slugData = addArticlePage.returnSlugData()
            addArticlePage.setItemsToCart(setText, slugData)
            addArticlePage.save()
            self.driver.refresh()
            addArticlePage.clickHtmlView(1)
            self.assertTrue(addArticlePage.checkForSlugsInArticles(slugData), "Slugs Didn't matched")
            
        else:
            self.skipTest("This test only runs on harpersbazaar")
    
    def testAddItemsToCartInGalleryBody(self):
        """Practitest id :None"""
    
        config = cfg.configuration()
        getConfig = config.getConfiguration()
        self.site = getConfig['site']
        if (self.site == "harpersbazaar"):
            
            addGalleryPage = GP.AddGalleryPage(self.driver, "m.php?t=images_groups")
            addGalleryPage.getRandomGallery()
            addGalleryPage.clickCartToAddItems()
            slugData = addGalleryPage.returnSlugData()
           
            setText = "TestHeadlines"
            addGalleryPage.setItemsToCart(setText, slugData)
            addGalleryPage.save()
            self.driver.refresh()
            self.assertTrue(addGalleryPage.checkSlugsInGallery(slugData), "Slug didn't matched")
        
        else:
            self.skipTest("This test only runs on harpersbazaar")