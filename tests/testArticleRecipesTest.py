from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver
import time,datetime
import unittest

class testArticleRecipesTest(seleniumDriver.seleniumDriver):
    '''
    def testRecipesTipsDirections(self):
        """Practitest id :322"""
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        currentTime = time.strftime("%H:%M:%S")        
        setText = "Default test value"
        
        #select ContentType by default it select Recipes
        addArticlePage.getContent()
        addArticlePage.setIngredientOne(setText)
        addArticlePage.setIngredientTwo(setText)
        addArticlePage.setDirectionsForRecipes(setText)
        addArticlePage.setTipsforRecipes(setText)
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        
        articlePage = ArticlePage.ArticlePage(self.driver)
        time.sleep(2)
        self.assertEquals('1'+" "+setText,articlePage.getIngredientsOne(), "Ingredients one aren't equal as provided")
        self.assertEquals('1'+" "+setText,articlePage.getIngredientsTwo(), "Ingredients two aren't equal as provided")
        self.assertEquals(setText,articlePage.getDirectionsText(),"Directions do not match")
    '''    