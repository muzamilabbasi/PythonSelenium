import time, unittest
from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver
<<<<<<< Updated upstream
=======
from configobj import ConfigObj
import sys
>>>>>>> Stashed changes

class testArticleRecipeGalleryEmbedTest(seleniumDriver.seleniumDriver):
    '''

    def testRecipeGalleryEmbedTest(self):
<<<<<<< Updated upstream
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        #select ContentType by default it select Recipes
        addArticlePage.getContent()
        
        currentTime = time.strftime("%H:%M:%S")        
        setText = "Default test value"
       
        time.sleep(2)
        addArticlePage.setIngredientOne(setText)
        addArticlePage.setIngredientTwo(setText)
        addArticlePage.setDirectionsForRecipes(setText)
        
        addArticlePage.clickTipsGalleryEmbed()
        
        dataId = addArticlePage.lightBox("data-id")
        addArticlePage.clickOnGalleryEmbedInsertButton(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(3)
        
        assert dataId[0] in addArticlePage.getRecipeTipsGalleryId()
        
        time.sleep(1)
        previewUrl = addArticlePage.getPreviewUrl()
        addArticlePage.loadUrl(previewUrl)
        articlePage = ArticlePage.ArticlePage(self.driver)
        time.sleep(2)
        assert dataId[1] in articlePage.getRecipeRelatedGalleryEmbed()'''
        
=======
        """Practitest id :311"""
    
        if (sys.platform == "darwin"):
            config = ConfigObj('/usr/local/bin/setup.cfg')
        elif (sys.platform == "windows"):
            config = ConfigObj('../setup.cfg')    
            
        site = config['nosetests']['site']
        
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
            
            addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            
            #select ContentType by default it select Recipes
            addArticlePage.getContent()
            
            currentTime = time.strftime("%H:%M:%S")        
            setText = "Default test value"
           
            time.sleep(2)
            addArticlePage.setIngredientOne(setText)
            addArticlePage.setIngredientTwo(setText)
            addArticlePage.setDirectionsForRecipes(setText)
            
            addArticlePage.clickTipsGalleryEmbed()
            
            dataId = addArticlePage.lightBox("data-id")
            addArticlePage.clickOnGalleryEmbedInsertButton(1)
            
            addArticlePage.save()
            self.driver.refresh()
            addArticlePage.clickHtmlView(3)
            
            assert dataId[0] in addArticlePage.getRecipeTipsGalleryId()
                
            time.sleep(1)
            previewUrl = addArticlePage.getPreviewUrl()
            addArticlePage.loadUrl(previewUrl)
            articlePage = ArticlePage.ArticlePage(self.driver)
            time.sleep(2)
            assert dataId[1] in articlePage.getRecipeRelatedGalleryEmbed()
            
        else: 
            print "Skipping the test because the site provided is incorrect to run test on!"
            self.skipTest("The specified site don't run this test!")
            
>>>>>>> Stashed changes
if __name__ == "__main__":
    unittest.main()
