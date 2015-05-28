import time, unittest
from pages.backend import AddArticlePage as AP
from classes import PageActions
from selenium.webdriver.common.by import By
from classes import seleniumDriver
from pages.frontend import ArticlePage
from configobj import ConfigObj

class testArticleRecipesExternalLink(seleniumDriver.seleniumDriver):
    
    def testRecipeDirectionsExternalLinksTest(self):
        """Practitest id :313"""
        
        config = ConfigObj('\..\setup.cfg')
        site = config['nosetests']['site']
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
         
            addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            
            #select ContentType by default it select Recipes
            addArticlePage.getContent()
            keys = "https://www.google.com/?gws_rd=ssl"
            addArticlePage.clickDirectionsExternalLinks()
            
            currentTime = time.strftime("%H:%M:%S")        
            setText = "Default test value"
            
            self.pageAction = PageActions.PageActions(self.driver)
            alert = self.driver.switch_to_alert()
            alert.send_keys(keys)
            alert.accept()
            alert.dismiss()
            alert.dismiss()
            alert.dismiss()
            
            addArticlePage.setIngredientOne(setText)
            addArticlePage.setIngredientTwo(setText)
            
            addArticlePage.setTipsforRecipes(setText)
            
             
            addArticlePage.save() 
            self.driver.refresh()
            
            addArticlePage.clickHtmlView(2)
            
            time.sleep(2)
            assert keys in addArticlePage.getDirectionsContentUrlStripped() 
            
            addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
            articlePage = ArticlePage.ArticlePage(self.driver)
            urlText = articlePage.getDirectionsText()
            assert keys in urlText 
        
        else:
            print "Skipping the test because the site provided is incorrect to run test on!"
            self.skipTest("The specified site don't run this test!")
        
    def testRecipeTipsExternalLinksTest(self):
        """Practitest id :314"""
        
        config = ConfigObj('\..\setup.cfg')
        site = config['nosetests']['site']
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
         
            addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            
            #select ContentType by default it select Recipes
            addArticlePage.getContent()
            keys = "https://www.google.com/?gws_rd=ssl"
            addArticlePage.clickTipsExternalLinks()
            
            currentTime = time.strftime("%H:%M:%S")        
            setText = "Default test value"
            
            self.pageAction = PageActions.PageActions(self.driver)
            alert = self.driver.switch_to_alert()
            alert.send_keys(keys)
            alert.accept()
            alert.dismiss()
            alert.dismiss()
            alert.dismiss()
            
            addArticlePage.setIngredientOne(setText)
            addArticlePage.setIngredientTwo(setText)
            addArticlePage.setDirectionsForRecipes(setText)
            
            addArticlePage.save() 
            self.driver.refresh()
            addArticlePage.clickHtmlView(3)
            
            time.sleep(2)
            assert keys in addArticlePage.getTipsContentUrlStripped() 
            
            addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
            articlePage = ArticlePage.ArticlePage(self.driver)
            #need to get tips text on front end
            #urlText = articlePage
            #assert keys in urlText'''
    
        else:
            print "Skipping the test because the site provided is incorrect to run test on!"
            self.skipTest("The specified site don't run this test!")

if __name__ == "__main__":
    unittest.main()
