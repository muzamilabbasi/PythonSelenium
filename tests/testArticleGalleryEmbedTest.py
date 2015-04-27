import time, unittest
from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver

class ArticleGalleryEmbedTest(seleniumDriver.seleniumDriver):


    def testArticleGalleryEmbedTest(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        addArticlePage.clickBodyGalleryEmbed()
    
        dataId = addArticlePage.lightBox("data-id")
        addArticlePage.clickOnGalleryEmbedInsertButton()
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        
        assert dataId[0] in addArticlePage.getGalleryId()
        
        time.sleep(1)
        previewUrl = addArticlePage.getPreviewUrl()
        addArticlePage.loadUrl(previewUrl)
        articlePage = ArticlePage.ArticlePage(self.driver)
        time.sleep(2)
        assert dataId[1] in articlePage.getGalleryShortTitle()
        
if __name__ == "__main__":
    unittest.main()
