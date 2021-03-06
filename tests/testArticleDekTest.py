from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver
import time,datetime
import unittest

class ArticleDekTest(seleniumDriver.seleniumDriver):


    def testSetFontBold(self):
        self.AddArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        self.AddArticlePage.getRandomEditorialArticle()
        
        currentTime = time.strftime("%H:%M:%S")        
        bodyText = "Default test value"+currentTime
        expectedBodyText = '<strong>'+bodyText+'</strong>'
        lengthofText = len(bodyText)
        self.AddArticlePage.setArticleDekText(bodyText)
        self.AddArticlePage.clickWYSIWYGFormatting("bold",lengthofText,"Dek")
        self.assertTrue(self.AddArticlePage.save(), "cannot save an Article")
        self.driver.refresh()
        
        self.AddArticlePage.clickHtmlView(0)
        self.assertEquals(expectedBodyText,self.AddArticlePage.getArticleDekHTML(),"Data Not Matched")
    
        self.AddArticlePage.loadUrl(self.AddArticlePage.getPreviewUrl())
        self.run = ArticlePage.ArticlePage(self.driver)
        time.sleep(1)
        
        self.assertEqual(bodyText,self.run.getArticleDekText(),"DEK text didn't matched")
    
    def testSetFontItalic(self):
        self.AddArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        self.AddArticlePage.getRandomEditorialArticle()
        
        currentTime = time.strftime("%H:%M:%S")        
        bodyText = "Default test value"+currentTime
        expectedBodyText = '<em>'+bodyText+'</em>'
        lengthofText = len(bodyText)
        self.AddArticlePage.setArticleDekText(bodyText)
        self.AddArticlePage.clickWYSIWYGFormatting("italic",lengthofText,"Dek")
        self.assertTrue(self.AddArticlePage.save(), "cannot save an Article")
        self.driver.refresh()
        
        self.AddArticlePage.clickHtmlView(0)
        self.assertEquals(expectedBodyText,self.AddArticlePage.getArticleDekHTML(),"Data Not Matched")
    
        self.AddArticlePage.loadUrl(self.AddArticlePage.getPreviewUrl())
        self.run = ArticlePage.ArticlePage(self.driver)
        time.sleep(1)
        self.assertEqual(bodyText,self.run.getArticleDekText(),"DEK text didn't matched")
    
    def testSetFontUnderline(self):
        self.AddArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        self.AddArticlePage.getRandomEditorialArticle()
        
        currentTime = time.strftime("%H:%M:%S")        
        bodyText = "Default test value"+currentTime
        expectedBodyText = '<u>'+bodyText+'</u>'
        lengthofText = len(bodyText)
        self.AddArticlePage.setArticleDekText(bodyText)
        self.AddArticlePage.clickWYSIWYGFormatting("underline",lengthofText,"Dek")
        self.assertTrue(self.AddArticlePage.save(), "cannot save an Article")
        self.driver.refresh()
        
        self.AddArticlePage.clickHtmlView(0)
        self.assertEquals(expectedBodyText,self.AddArticlePage.getArticleDekHTML(),"Data Not Matched")
    
        self.AddArticlePage.loadUrl(self.AddArticlePage.getPreviewUrl())
        self.run = ArticlePage.ArticlePage(self.driver)
        time.sleep(1)
        
        self.assertEqual(bodyText,self.run.getArticleDekText(),"DEK text didn't matched")
        
    if __name__ == "__main__":
        unittest.main()
