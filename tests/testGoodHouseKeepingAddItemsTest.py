from classes import seleniumDriver
from classes import configurationManager as cfg

from pages.backend import AddArticlePage as AP
    

class testsGoodHouseKeepingAddItemsTest(seleniumDriver.seleniumDriver):
    
    def testAddItemsToCartInArticleBody(self):
        """Practitest id :None"""
    
        config = cfg.configuration()
        getConfig = config.getConfiguration()
        self.site = getConfig['site']
        
        if (self.site == "goodhousekeeping"):
            addArticlePage = AP.AddArticlePage(self.driver, "m.php?t=articles") 
            addArticlePage.getRandomEditorialArticle()
            setText = "TestHeadlines"
            productId = addArticlePage.getRandomProductIds()
            addArticlePage.setghkItemsToCart(productId, setText)
            
            self.assertTrue(addArticlePage.save(), "cannot save an Article")
            self.driver.refresh()
            addArticlePage.clickHtmlView(1)
            self.assertEqual(productId, addArticlePage.stripProductIds(), "Product Id's don't match")
        else:
            self.skipTest("This test only runs on GoodHouseKeeping!")