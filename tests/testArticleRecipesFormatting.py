from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver
import time,datetime
import unittest
from selenium.webdriver.common import alert

class testArticleRecipesFormatting(seleniumDriver.seleniumDriver):
    
    def testSetFontBoldDirections(self):
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
        
    def testSetFontItalicDirections(self):
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
        
    def testSetFontUnderlineDirections(self):
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
        
    def testSetFontBoldTips(self):
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
        
    def testSetFontItalicTips(self):
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
        
    def testSetFontUnderlineTips(self):
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