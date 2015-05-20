from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver
import time
import unittest

class ArticleDekTest(seleniumDriver.seleniumDriver):

    def testSetFontBold(self):
        """Practitest id :282"""
        self.AddArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        self.AddArticlePage.getRandomEditorialArticle()
        
        currentTime = time.strftime("%H:%M:%S")        
        bodyText = "Default test value"+currentTime
        expectedBodyText = '<strong>'+bodyText+'</strong>'
        
        self.AddArticlePage.setArticleDekText(bodyText)
        self.AddArticlePage.clickWYSIWYGFormatting("bold","Dek")
        self.assertTrue(self.AddArticlePage.save(), "cannot save an Article")
        self.driver.refresh()
        
        self.AddArticlePage.clickHtmlView(0)
        self.assertEquals(expectedBodyText,self.AddArticlePage.getArticleDekHTML(),"Data Not Matched")
    
        self.AddArticlePage.loadUrl(self.AddArticlePage.getPreviewUrl())
        self.run = ArticlePage.ArticlePage(self.driver)
        time.sleep(1)
        
        self.assertEqual(bodyText,self.run.getArticleDekText(),"DEK text didn't matched")
    
    def testSetFontItalic(self):
        """Practitest id :283"""
        self.AddArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        
        self.AddArticlePage.getRandomEditorialArticle()
        
        currentTime = time.strftime("%H:%M:%S")        
        bodyText = "Default test value"+currentTime
        expectedBodyText = '<em>'+bodyText+'</em>'
        
        self.AddArticlePage.setArticleDekText(bodyText)
        self.AddArticlePage.clickWYSIWYGFormatting("italic","Dek")
        self.assertTrue(self.AddArticlePage.save(), "cannot save an Article")
        self.driver.refresh()
        
        self.AddArticlePage.clickHtmlView(0)
        self.assertEquals(expectedBodyText,self.AddArticlePage.getArticleDekHTML(),"Data Not Matched")
    
        self.AddArticlePage.loadUrl(self.AddArticlePage.getPreviewUrl())
        self.run = ArticlePage.ArticlePage(self.driver)
        time.sleep(1)
        self.assertEqual(bodyText,self.run.getArticleDekText(),"DEK text didn't matched")
    
    def testSetFontUnderline(self):
        """Practitest id :284"""
        self.AddArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        self.AddArticlePage.getRandomEditorialArticle()
        
        currentTime = time.strftime("%H:%M:%S")        
        bodyText = "Default test value"+currentTime
        expectedBodyText = '<u>'+bodyText+'</u>'
        
        self.AddArticlePage.setArticleDekText(bodyText)
        self.AddArticlePage.clickWYSIWYGFormatting("underline","Dek")
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
