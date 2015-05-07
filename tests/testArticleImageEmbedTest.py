import time, unittest
from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from pages.backend import Images as editImages
from classes import seleniumDriver

class ArticleImageEmbedTest(seleniumDriver.seleniumDriver):


    def testArticleImageEmbedTest(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        addArticlePage.clickBodyImageEmbed()
    
        imageId = addArticlePage.lightBox("data-imageid")
        addArticlePage.clickOnImageEmbedInsertButton()
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        time.sleep(2)
        assert imageId[0] in addArticlePage.getImageId()
        previewUrl = addArticlePage.getPreviewUrl()
        
        editImage = editImages.Images(self.driver)
        editImage.searchImagebyId(imageId[0])
        getImageCutUrl = editImage.getSourceImageCut()
        getImagePlaceholderCut = editImage.getImagePlaceHolderCuts()
        
        addArticlePage.loadUrl(previewUrl)
        articlePage = ArticlePage.ArticlePage(self.driver)
        time.sleep(2)
        assert articlePage.getimageUrl() in getImagePlaceholderCut or getImageCutUrl
        
if __name__ == "__main__":
    unittest.main()
