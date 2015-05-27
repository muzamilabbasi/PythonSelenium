import time, unittest
from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver

class testArticleGalleryEmbedTest(seleniumDriver.seleniumDriver):

    def testArticleGalleryEmbedTest(self):
        """Practitest id :306"""
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        addArticlePage.clickBodyGalleryEmbed()
    
        dataId = addArticlePage.lightBox("data-id")
        addArticlePage.clickOnGalleryEmbedInsertButton()
        self.assertTrue(addArticlePage.save(), "cannot save an Article")
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        
        assert dataId[0] in addArticlePage.getGalleryId()
        
        previewUrl = addArticlePage.getPreviewUrl()
        addArticlePage.loadUrl(previewUrl)
        articlePage = ArticlePage.ArticlePage(self.driver)
        
        assert dataId[1] in articlePage.getGalleryShortTitle()
        
if __name__ == "__main__":
    unittest.main()
