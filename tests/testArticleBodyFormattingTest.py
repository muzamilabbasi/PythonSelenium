import time, unittest

from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class testsArticleBodyFormattingTests(seleniumDriver.seleniumDriver):
    
    
    def testSetFontBold(self):
        """Practitest id :278"""
        self.AddArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        self.AddArticlePage.getRandomEditorialArticle()
        
        currentTime = time.strftime("%H:%M:%S")        
        bodyText = "Default test value"+currentTime
        expectedBodyText = '<strong>'+bodyText+'</strong>'
        
        self.AddArticlePage.setArticleBodyText(bodyText)
        self.AddArticlePage.clickWYSIWYGFormatting("bold","body")
        self.assertTrue(self.AddArticlePage.save(), "cannot save an Article")
        
        
        self.driver.refresh()
        self.AddArticlePage.clickHtmlView(1)
        
        self.assertEquals(expectedBodyText,self.AddArticlePage.getHtmlBody(),"Data Not Matched")
        previewUrl = self.AddArticlePage.getPreviewUrl()
        self.AddArticlePage.loadUrl(previewUrl)
        self.run = ArticlePage.ArticlePage(self.driver)
        self.assertEqual(expectedBodyText,self.run.getBodyTextStyle(),"Body text didn't matched")
        
    def testSetFontItalic(self):
        """Practitest id :279"""
        self.AddArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        self.AddArticlePage.getRandomEditorialArticle()
        
        currentTime = time.strftime("%H:%M:%S")        
        bodyText = "Default test value"+currentTime
        expectedBodyText = '<em>'+bodyText+'</em>'
        
        self.AddArticlePage.setArticleBodyText(bodyText)
        self.AddArticlePage.clickWYSIWYGFormatting("italic","body")
        self.assertTrue(self.AddArticlePage.save(), "cannot save an Article")
        
        self.driver.refresh()
        self.AddArticlePage.clickHtmlView(1)
        
        self.assertEquals(expectedBodyText,self.AddArticlePage.getHtmlBody(),"Data Not Matched")
        
        self.AddArticlePage.loadUrl(self.AddArticlePage.getPreviewUrl())
        self.run = ArticlePage.ArticlePage(self.driver)
        self.assertEqual(expectedBodyText,self.run.getBodyTextStyle(),"Body text didn't matched")
    
    def testSetFontUnderline(self):
        """Practitest id :280"""
        self.AddArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        self.AddArticlePage.getRandomEditorialArticle()
        
        currentTime = time.strftime("%H:%M:%S")        
        bodyText = "Default test value"+currentTime
        expectedBodyText = '<u>'+bodyText+'</u>'
        
        self.AddArticlePage.setArticleBodyText(bodyText)
        self.AddArticlePage.clickWYSIWYGFormatting("underline","body")
        self.assertTrue(self.AddArticlePage.save(), "cannot save an Article")
        
        self.driver.refresh()
        self.AddArticlePage.clickHtmlView(1)
        
        self.assertEquals(expectedBodyText,self.AddArticlePage.getHtmlBody(),"Data Not Matched")
        
        self.AddArticlePage.loadUrl(self.AddArticlePage.getPreviewUrl())
        self.run = ArticlePage.ArticlePage(self.driver)
        self.assertEqual(expectedBodyText,self.run.getBodyTextStyle(),"Body text didn't matched")
    
if __name__ == "__main__":
    unittest.main()
