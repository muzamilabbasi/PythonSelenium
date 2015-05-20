import time, unittest
from pages.backend import AddArticlePage as AP

from selenium.webdriver.common.by import By
from classes import seleniumDriver
from pages.frontend import ArticlePage
from pages.backend import PageActions

class testArticleExternalLinksTest(seleniumDriver.seleniumDriver):

    def testArticleBodyExternalLinksTest(self):
        """Practitest id :304"""
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
            
        addArticlePage.getRandomEditorialArticle()
        
        keys = "https://www.google.com/?gws_rd=ssl"
        addArticlePage.clickBodyExternalLinks()
        self.pageAction = PageActions.PageActions(self.driver)
        alert = self.driver.switch_to.alert
        
        alert.send_keys(keys)
        print alert
        
        alert.accept()
        alert.dismiss()
        
            
        time.sleep(5)
        self.assertTrue(self.AddArticlePage.save(), "cannot save an Article")
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        self.assertEqual(keys,addArticlePage.getContentUrlStripped(), "The text is not equal")
        
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        self.run = ArticlePage.ArticlePage(self.driver)
        
        self.pageAction.switchNewWindows(By.XPATH, "//*[@class='article-body--content']/div[2]/p/a")
        time.sleep(2)
        browserUrl = self.driver.current_url
        assert keys in browserUrl
    '''
    def testArticleDekExternalLinksTest(self):
        """Practitest id :305"""
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        keys = "https://www.google.com/?gws_rd=ssl"
        
        addArticlePage.clickDekExternalLinks()
        self.pageAction = PageActions.PageActions(self.driver)
        alert = self.driver.switch_to_alert()
        alert.send_keys(keys)
        alert.accept()
        alert.send_keys(keys)
        alert.accept()
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(0)
        
        assert keys in addArticlePage.getDekContentUrlStripped()
        
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        
        self.pageAction.switchNewWindows(By.XPATH, "//*[@id='site-wrapper']/article/header/h2/a")
        time.sleep(2)
        browserUrl = self.driver.current_url
        assert keys in browserUrl'''


if __name__ == "__main__":
    unittest.main()
