import time, unittest
from pages.backend import AddArticlePage as AP
from classes import PageActions
from selenium.webdriver.common.by import By
from classes import seleniumDriver
from pages.frontend import ArticlePage
from configobj import ConfigObj

class testArticleRecipesInternallLink(seleniumDriver.seleniumDriver):
   
    def testArticleDirectionsInternalLinksTest(self):
        """Practitest id :320"""

        config = ConfigObj('\..\setup.cfg')
        site = config['nosetests']['site']
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
        
            addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            
            #select ContentType by default it select Recipes
            addArticlePage.getContent()
            
            currentTime = time.strftime("%H:%M:%S")        
            setText = "Default test value"
           
            addArticlePage.setIngredientOne(setText)
            addArticlePage.setIngredientTwo(setText)
            addArticlePage.clickDirectionsInternalLinks()
            addedContentUrl = addArticlePage.lightBox()
            addArticlePage.setTipsforRecipes(setText)
            addArticlePage.save()
            self.driver.refresh()
            
            addArticlePage.clickHtmlView(2)
            self.assertEqual(addedContentUrl[0],addArticlePage.getDirectionsContentUrlStripped(), "The text is not equal")
            
            addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
            # click on the linked article
            self.driver.find_element_by_xpath('//*[@id="site-wrapper"]/article/div[1]/div[2]/div[2]/div[2]/section/section[2]/section[2]/ol/li/a').click()
            #articlePage.getDirectionTextElement()
            browserUrl = self.driver.current_url
            assert addedContentUrl[0] in browserUrl
            
        else:
            print "Skipping the test because the site provided is incorrect to run test on!"
            self.skipTest("The specified site don't run this test!")  
    
    def testArticleTipsInternalLinksTest(self):
        """Practitest id :321"""
        
        config = ConfigObj('\..\setup.cfg')
        site = config['nosetests']['site']
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
        
            addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            
            #select ContentType by default it select Recipes
            addArticlePage.getContent()
            
            currentTime = time.strftime("%H:%M:%S")        
            setText = "Default test value"
           
            addArticlePage.setIngredientOne(setText)
            addArticlePage.setIngredientTwo(setText)
            addArticlePage.setDirectionsForRecipes(setText)
            
            addArticlePage.clickTipsInternalLinks()
            addedContentUrl = addArticlePage.lightBox()
            addArticlePage.save()
            self.driver.refresh()
            
            addArticlePage.clickHtmlView(3)
            self.assertEqual(addedContentUrl[0],addArticlePage.getTipsContentUrlStripped(), "The text is not equal")
            
            addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
            articlePage = ArticlePage.ArticlePage(self.driver)
            articlePage.getTipsElement("link").click()
            browserUrl = self.driver.current_url
            assert addedContentUrl[0] in browserUrl
            
        else:
            print "Skipping the test because the site provided is incorrect to run test on!"
            self.skipTest("The specified site don't run this test!")  

if __name__ == "__main__":
    unittest.main()
