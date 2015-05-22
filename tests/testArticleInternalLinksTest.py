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
        self.assertEqual(addedContentUrl[0],addArticlePage.getContentUrlStripped(), "The text is not equal")
        
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        
        articlePage.clickInternalLinkContent()
        time.sleep(2)
        browserUrl = self.driver.current_url
        print browserUrl
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
        
        time.sleep(2)
        print addedContentUrl[0]
        print addArticlePage.getDekContentUrlStripped()
        self.assertEqual(addedContentUrl[0],addArticlePage.getDekContentUrlStripped(), "The text is not equal")
        
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        
        articlePage.clickDekInternalLinkContent()
        time.sleep(3)
        browserUrl = self.driver.current_url
        print addedContentUrl[0]
        print browserUrl
        assert addedContentUrl[0] in browserUrl
        
if __name__ == "__main__":
    unittest.main()
