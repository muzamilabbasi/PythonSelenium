import time, unittest
from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from pages.backend import Images as editImage
from classes import seleniumDriver
<<<<<<< Updated upstream
=======
from configobj import ConfigObj
import sys
>>>>>>> Stashed changes

class testArticleRecipeImageEmbedTest(seleniumDriver.seleniumDriver):
    '''

    def testRecipeImageEmbedTest(self):
<<<<<<< Updated upstream
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        addArticlePage.clickTipsImageEmbed()
    
        imageId = addArticlePage.lightBox("data-imageid")
        addArticlePage.clickOnImageEmbedInsertButton()
        time.sleep(10)
=======
        """Practitest id :312"""
   
        if (sys.platform == "darwin"):
            config = ConfigObj('/usr/local/bin/setup.cfg')
        elif (sys.platform == "windows"):
            config = ConfigObj('../setup.cfg')    
            
        site = config['nosetests']['site']
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
             
            addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            addArticlePage.clickTipsImageEmbed()
>>>>>>> Stashed changes
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        
        assert imageId[0] in addArticlePage.getImageId()
        time.sleep(1)
        previewUrl = addArticlePage.getPreviewUrl()
        
        editImage = editImage.Images(self.driver)
        editImage.searchImagebyId(imageId[0])
        getImageCutUrl = editImage.getSourceImageCut()
        getImagePlaceholderCut = editImage.getImagePlaceHolderCuts()
        
        addArticlePage.loadUrl(previewUrl)
        articlePage = ArticlePage.ArticlePage(self.driver)
        time.sleep(2)
        assert articlePage.getimageUrl() in getImagePlaceholderCut or getImageCutUrl'''
        
if __name__ == "__main__":
    unittest.main()
