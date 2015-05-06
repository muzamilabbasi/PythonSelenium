from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from classes import seleniumDriver
import time,datetime
import unittest

class testSyndicationTest(seleniumDriver.seleniumDriver):
    
    def testURl(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles&syndication") 
        setUrl = self.driver.find_element_by_xpath("//*[@id='contents']/div/div[1]/div[1]/input[1]")
        setUrl.send_keys("http://www-stage.cosmopolitan.com/entertainment/celebs/news/a39687/chris-evans-shaves-beard-for-captain-america-3/")
        clickButton = self.driver.find_element_by_xpath("//*[@id='contents']/div/div[1]/div[2]/button")
        clickButton.click()
        time.sleep(2)
        self.driver.save_screenshot("/usr/local/bin/syndication.png")