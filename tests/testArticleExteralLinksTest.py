import time, unittest
from pages.backend import AddArticlePage as AP
from classes import PageActions
from selenium.webdriver.common.by import By
from classes import seleniumDriver
from pages.frontend import ArticlePage

class ArticleExternalLinksTest(seleniumDriver.seleniumDriver):


<<<<<<< Updated upstream
    def testArticleBodyExternalLinksTest(self):
=======
    '''def testArticleBodyExternalLinksTest(self):
        """Practitest id :304"""
>>>>>>> Stashed changes
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        keys = "https://www.google.com/?gws_rd=ssl"
        addArticlePage.clickBodyExternalLinks()
<<<<<<< Updated upstream
        self.pageAction = PageActions.PageActions(self.driver)
        alert = self.driver.switch_to_alert()
        alert.send_keys(keys)
        alert.accept()
        alert.accept()
        
        addArticlePage.save()
=======
        alert = self.driver.switch_to.alert
        alert.send_keys(keys)
        alert.accept()
        alert.accept()
            
        self.assertTrue(addArticlePage.save(), "cannot save an Article")
>>>>>>> Stashed changes
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        self.assertEqual(keys,addArticlePage.getContentUrlStripped(), "The text is not equal")
        
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        self.run = ArticlePage.ArticlePage(self.driver)
        
        self.pageAction.switchNewWindows(By.XPATH, "//*[@class='article-body--content']/div[2]/p/a")
        time.sleep(2)
        browserUrl = self.driver.current_url
<<<<<<< Updated upstream
        assert keys in browserUrl
        
=======
        assert keys in browserUrl'''
    
>>>>>>> Stashed changes
    def testArticleDekExternalLinksTest(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        keys = "https://www.google.com/?gws_rd=ssl"
        
        addArticlePage.clickDekExternalLinks()
<<<<<<< Updated upstream
        self.pageAction = PageActions.PageActions(self.driver)
        alert = self.driver.switch_to_alert()
        alert.send_keys(keys)
        alert.accept()
=======
        
        alert = self.driver.switch_to_alert()
>>>>>>> Stashed changes
        alert.send_keys(keys)
        alert.accept()
<<<<<<< Updated upstream
        
        addArticlePage.save()
=======
        self.assertTrue(addArticlePage.save(), "cannot save an Article")
>>>>>>> Stashed changes
        self.driver.refresh()
        addArticlePage.clickHtmlView(0)
        
        assert keys in addArticlePage.getDekContentUrlStripped()
        
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        
        self.pageAction.switchNewWindows(By.XPATH, "//*[@id='site-wrapper']/article/header/h2/a")
        time.sleep(2)
        browserUrl = self.driver.current_url
        assert keys in browserUrl

if __name__ == "__main__":
    unittest.main()
