import time, unittest
from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver

class ArticleInternalLinksTest(seleniumDriver.seleniumDriver):

    def testArticleBodyInternalLinksTest(self):
        """Practitest id :308"""
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        addArticlePage.clickBodyInternalLinks()
    
        addedContentUrl = addArticlePage.lightBox()
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        time.sleep(1)
        self.assertEqual(addedContentUrl[0],addArticlePage.getContentUrlStripped(), "The text is not equal")
        
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        
        articlePage.clickInternalLinkContent()
        
        browserUrl = self.driver.current_url
        assert addedContentUrl[0] in browserUrl
        
    
    def testArticleDekInternalLinksTest(self):
        """Practitest id :309"""
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        addArticlePage.clickDekInternalLinks()
        
        addedContentUrl = addArticlePage.lightBox()
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(0)
        
        time.sleep(1)
        self.assertEqual(addedContentUrl[0],addArticlePage.getDekContentUrlStripped(), "The text is not equal")
        
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        
        articlePage.clickDekInternalLinkContent()
        browserUrl = self.driver.current_url
        assert addedContentUrl[0] in browserUrl
        
if __name__ == "__main__":
    unittest.main()
