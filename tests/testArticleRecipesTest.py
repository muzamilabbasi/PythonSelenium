from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver
import time,datetime
import unittest
<<<<<<< Updated upstream
from numpy.f2py.auxfuncs import throw_error
=======
from configobj import ConfigObj
import sys
>>>>>>> Stashed changes

class testArticleRecipesTest(seleniumDriver.seleniumDriver):
    
    '''
    def testRecipesTipsDirections(self):
       
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
<<<<<<< Updated upstream
        currentTime = time.strftime("%H:%M:%S")        
        setText = "Default test value"
=======
        if (sys.platform == "darwin"):
            config = ConfigObj('/usr/local/bin/setup.cfg')
        elif (sys.platform == "windows"):
            config = ConfigObj('../setup.cfg')    
            
        site = config['nosetests']['site']
        if (site == "goodhousekeeping"  or site == "countryliving" or site == "womansdays" or site == "delish" or site == "redbook"):
>>>>>>> Stashed changes
        
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
        self.assertEquals(setText,articlePage.getDirectionsText(),"Directions do not match")'''
        
