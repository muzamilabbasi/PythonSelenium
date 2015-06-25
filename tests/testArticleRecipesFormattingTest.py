from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver
import time,datetime
import unittest
from selenium.webdriver.common import alert
from configobj import ConfigObj
import sys

class testArticleRecipesFormatting(seleniumDriver.seleniumDriver):

    def testSetFontBoldDirections(self):
        """Practitest id :314"""
        
        if (sys.platform == "darwin"):
            config = ConfigObj('/usr/local/bin/setup.cfg')
        elif (sys.platform == "windows"):
            config = ConfigObj('../setup.cfg')    
            
        site = config['nosetests']['site']
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
         
            addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            
            currentTime = time.strftime("%H:%M:%S")        
            setText = "Default test value"
            expectedText = "<strong>"+setText+"</strong>"
            #select ContentType
            addArticlePage.getContent()
            #alert = self.driver.switch_to_alert()
            #alert.accept()
            
            addArticlePage.setIngredientOne(setText)
            addArticlePage.setIngredientTwo(setText)
            addArticlePage.setDirectionsForRecipes(setText)
            addArticlePage.clickWYSIWYGFormatting("bold","directions")
            addArticlePage.setTipsforRecipes(setText)
            self.assertTrue(addArticlePage.save(), "cannot save an Article")
            addArticlePage.clickHtmlView(2)
            #NEED AN ASSERTION HERE TOO
            addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
            articlePage = ArticlePage.ArticlePage(self.driver)
            self.assertEquals(expectedText,articlePage.getDirectionsTextInnerHtml(),"The Expected Text Didn't Matched")
            
        else:
            print "Skipping the test because the site provided is incorrect to run test on!"
            self.skipTest("The specified site don't run this test!")
        
    def testSetFontItalicDirections(self):
        """Practitest id :315"""
        
        if (sys.platform == "darwin"):
            config = ConfigObj('/usr/local/bin/setup.cfg')
        elif (sys.platform == "windows"):
            config = ConfigObj('../setup.cfg')    
            
        site = config['nosetests']['site']
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
         
            addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            
            currentTime = time.strftime("%H:%M:%S")        
            setText = "Default test value"
            expectedText = "<em>"+setText+"</em>"
            #select ContentType
            addArticlePage.getContent()
            #alert = self.driver.switch_to_alert()
            #alert.accept()
            
            addArticlePage.setIngredientOne(setText)
            addArticlePage.setIngredientTwo(setText)
            addArticlePage.setDirectionsForRecipes(setText)
            addArticlePage.clickWYSIWYGFormatting("italic","directions")
            addArticlePage.setTipsforRecipes(setText)
            self.assertTrue(addArticlePage.save(), "cannot save an Article")
            addArticlePage.clickHtmlView(2)
            #NEED AN ASSERTION HERE TOO
            addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
            articlePage = ArticlePage.ArticlePage(self.driver)
            self.assertEquals(expectedText,articlePage.getDirectionsTextInnerHtml(),"The Expected Text Didn't Matched")
        
        else:
            print "Skipping the test because the site provided is incorrect to run test on!"
            self.skipTest("The specified site don't run this test!")
        
    def testSetFontUnderlineDirections(self):
        """Practitest id :316"""
        
        if (sys.platform == "darwin"):
            config = ConfigObj('/usr/local/bin/setup.cfg')
        elif (sys.platform == "windows"):
            config = ConfigObj('../setup.cfg')    
            
        site = config['nosetests']['site']
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
         
            addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            
            currentTime = time.strftime("%H:%M:%S")        
            setText = "Default test value"
            expectedText = "<u>"+setText+"</u>"
            #select ContentType
            addArticlePage.getContent()
            #alert = self.driver.switch_to_alert()
            #alert.accept()
            
            addArticlePage.setIngredientOne(setText)
            addArticlePage.setIngredientTwo(setText)
            addArticlePage.setDirectionsForRecipes(setText)
            addArticlePage.clickWYSIWYGFormatting("underline","directions")
            addArticlePage.setTipsforRecipes(setText)
            self.assertTrue(addArticlePage.save(), "cannot save an Article")
            addArticlePage.clickHtmlView(2)
            #NEED AN ASSERTION HERE TOO
            addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
            articlePage = ArticlePage.ArticlePage(self.driver)
            self.assertEquals(expectedText,articlePage.getDirectionsTextInnerHtml(),"The Expected Text Didn't Matched")
        
        else:
            print "Skipping the test because the site provided is incorrect to run test on!"
            self.skipTest("The specified site don't run this test!")
        
    def testSetFontBoldTips(self):
        """Practitest id :317"""
        
        config = ConfigObj('\..\setup.cfg')
        site = config['nosetests']['site']
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
         
            addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            
            currentTime = time.strftime("%H:%M:%S")        
            setText = "Default test value"
            expectedText = "<u>"+setText+"</u>"
            #select ContentType
            addArticlePage.getContent()
            #alert = self.driver.switch_to_alert()
            #alert.accept()
            
            addArticlePage.setIngredientOne(setText)
            addArticlePage.setIngredientTwo(setText)
            addArticlePage.setDirectionsForRecipes(setText)
            addArticlePage.setTipsforRecipes(setText)
            addArticlePage.clickWYSIWYGFormatting("bold","tips")
            self.assertTrue(addArticlePage.save(), "cannot save an Article")
            addArticlePage.clickHtmlView(2)
            #NEED AN ASSERTION HERE TOO
            addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
            articlePage = ArticlePage.ArticlePage(self.driver)
            self.assertEquals(expectedText,articlePage.getDirectionsTextInnerHtml(),"The Expected Text Didn't Matched")
            
        else:
            print "Skipping the test because the site provided is incorrect to run test on!"
            self.skipTest("The specified site don't run this test!")
        
    def testSetFontItalicTips(self):
        """Practitest id :318"""   
        
        config = ConfigObj('\..\setup.cfg')
        site = config['nosetests']['site']
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
        
            addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            
            currentTime = time.strftime("%H:%M:%S")        
            setText = "Default test value"
            expectedText = "<u>"+setText+"</u>"
            #select ContentType
            addArticlePage.getContent()
            #alert = self.driver.switch_to_alert()
            #alert.accept()
            
            addArticlePage.setIngredientOne(setText)
            addArticlePage.setIngredientTwo(setText)
            addArticlePage.setDirectionsForRecipes(setText)
            time.sleep(1)
            addArticlePage.setTipsforRecipes(setText)
            addArticlePage.clickWYSIWYGFormatting("italic","tips")
            self.assertTrue(addArticlePage.save(), "cannot save an Article")
            addArticlePage.clickHtmlView(2)
            #NEED AN ASSERTION HERE TOO
            addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
            articlePage = ArticlePage.ArticlePage(self.driver)
            self.assertEquals(expectedText,articlePage.getDirectionsTextInnerHtml(),"The Expected Text Didn't Matched")
            
        else:
            print "Skipping the test because the site provided is incorrect to run test on!"
            self.skipTest("The specified site don't run this test!")
            
    def testSetFontUnderlineTips(self):
        """Practitest id :319"""
        
        config = ConfigObj('\..\setup.cfg')
        site = config['nosetests']['site']
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
        
            addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            
            currentTime = time.strftime("%H:%M:%S")        
            setText = "Default test value"
            expectedText = "<u>"+setText+"</u>"
            #select ContentType
            addArticlePage.getContent()
            #alert = self.driver.switch_to_alert()
            #alert.accept()
            
            addArticlePage.setIngredientOne(setText)
            addArticlePage.setIngredientTwo(setText)
            addArticlePage.setDirectionsForRecipes(setText)
            time.sleep(1)
            addArticlePage.setTipsforRecipes(setText)
            addArticlePage.clickWYSIWYGFormatting("underline","tips")
            self.assertTrue(addArticlePage.save(), "cannot save an Article")
            addArticlePage.clickHtmlView(2)
            #NEED AN ASSERTION HERE TOO
            addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
            articlePage = ArticlePage.ArticlePage(self.driver)
            self.assertEquals(expectedText,articlePage.getDirectionsTextInnerHtml(),"The Expected Text Didn't Matched")
        
        else:
            print "Skipping the test because the site provided is incorrect to run test on!"
            self.skipTest("The specified site don't run this test!")  
            
            
if __name__ == "__main__":
    unittest.main()

        