import unittest
from random import randint
from string import count


class RamsPage(unittest.TestCase):
    
    def __init__(self,driver,loadPage = " "):
        self.driver = driver
        
        self.loadPage = loadPage
        newPageUrl = self.driver.current_url+loadPage
        self.loadUrl(newPageUrl)
            
        ''''if (pageUrl != ""):  
            print "Its me IF" 
            #if (pageUrl in self.loadHomePageUrl() == False):
            newPageUrl = self.driver.current_url+pageUrl
            self.loadPage(newPageUrl)
            #EditorialPage.EditorialPage(self.driver)
        #self.driver.get("http://rams-stage.cosmopolitan.com/m.php?t=articles") '''
            
    def getRandomEditorialArticle(self):
        randomString = randint(1000,10000)
        searchBox = self.driver.find_element_by_id("id")
        searchBox.send_keys(randomString)
        
        
        getResults = self.driver.find_element_by_xpath("//*[@id='results_table']/table/tbody/tr/td[1]")
        if (getResults != ''):
            count = 1
            
            #self.driver.get("http://rams-stage.cosmopolitan.com/m.php?t=articles&edit&id="+str(getResults.text))
            
            currentPageUrl = self.driver.current_url
            loadPage = currentPageUrl+"&edit&id="+str(getResults.text)
            self.loadUrl(loadPage)
            #return AddArticlePage.AddArticlePage(self.driver,getResults.text)
        else:
            count = 0
            return False

        
    def loadUrl(self,url):
        return self.driver.get(url)
    
    
    def loadHomePageUrl(self):
        return self.driver.loadPage("http://rams-stage.cosmopolitan.com")
        
    
    
    