import time, unittest
from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from pages.backend import Images as editImages
from classes import seleniumDriver

class testArticleImageEmbedTest(seleniumDriver.seleniumDriver):

    def testArticleImageEmbedTest(self):
        """Practitest id :307"""
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        addArticlePage.clickBodyImageEmbed()
    
        imageId = addArticlePage.lightBox("data-imageid")
        addArticlePage.clickOnImageEmbedInsertButton()
        self.assertTrue(addArticlePage.save(), "cannot save an Article")
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        
        assert imageId[0] in addArticlePage.getImageId()
        previewUrl = addArticlePage.getPreviewUrl()
        time.sleep(2)
        editImage = editImages.Images(self.driver)
        editImage.searchImagebyId(imageId[0])
        getImageCutUrl = editImage.getSourceImageCut()
        getImagePlaceholderCut = editImage.getImagePlaceHolderCuts()
        
        addArticlePage.loadUrl(previewUrl)
        articlePage = ArticlePage.ArticlePage(self.driver)
        
        assert articlePage.getimageUrl() in getImagePlaceholderCut or getImageCutUrl
        
if __name__ == "__main__":
    unittest.main()
