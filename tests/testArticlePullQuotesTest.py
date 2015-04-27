import time, unittest
from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver

class ArticlePullQuotesTest(seleniumDriver.seleniumDriver):

    def testSetArticlePullQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        currentTime = time.strftime("%H:%M:%S")        
        bodyText = "Default test value"+currentTime
        expectedBodyText = '[pullquote align="L" ]'+bodyText+'[/pullquote]'
        
        addArticlePage.setPullQuotes(bodyText)
        addArticlePage.popUpButtons()
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        time.sleep(2)
        self.assertEqual(expectedBodyText, addArticlePage.getHtmlBody(),"Pull Quotes Inserted Doesn't matches the Article Body Text")
        
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        time.sleep(2)
        self.assertEqual(bodyText,articlePage.getPullQuoteText(),"Assertion Failed")
        self.assertTrue(articlePage.getPullQuoteIcon,"Pull Quotes Icon Not Visible...")
        
if __name__ == "__main__":
    unittest.main()
