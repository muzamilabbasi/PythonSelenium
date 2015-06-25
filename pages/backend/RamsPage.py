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
<<<<<<< Updated upstream
        randomString = randint(5000,100000)
        searchBox = self.driver.find_element_by_id("id")
        searchBox.send_keys(randomString)
        
        
=======
        sessionId = self.driver.session_id
        print sessionId
        randomId = worker.worker()
        id = randomId.getApiData(sessionId)
        time.sleep(2)
        searchBox = self.driver.find_element_by_id("id")
        searchBox.send_keys(id)
>>>>>>> Stashed changes
        getResults = self.driver.find_element_by_xpath("//*[@id='results_table']/table/tbody/tr/td[1]")
        if (getResults != ''):
            count = 1
            currentPageUrl = self.driver.current_url
<<<<<<< Updated upstream
            loadPage = currentPageUrl+"&edit&id="+str(getResults.text)
            self.loadUrl(loadPage)
            #return AddArticlePage.AddArticlePage(self.driver,getResults.text)
=======
            loadPage = currentPageUrl+"&edit&id="+str(id)
            self.loadUrl(loadPage)
            
>>>>>>> Stashed changes
        else:
            count = 0
            return False

    def getRandomEditor(self):
        resultRows = self.driver.find_elements_by_xpath("//*[@id='results_table']/table/tbody/tr")
        num = len(resultRows)
        id = []
        for i in range(num):
                ids = self.driver.find_element_by_xpath("//*[@id='results_table']/table/tbody/tr['"+str(i)+"']/td['"+str(i)+"']/a")
                id.append(ids)
        
        time.sleep(2)
        searchBox = self.driver.find_element_by_id("id")
        searchBox.send_keys(id[0].text)
        getResults = self.driver.find_element_by_xpath("//*[@id='results_table']/table/tbody/tr/td[1]")
        if (getResults != ''):
            count = 1
            
            currentPageUrl = self.driver.current_url
            loadPage = currentPageUrl+"&edit&id="+id[0].text
            self.loadUrl(loadPage)
        else:
            count = 0
            raise Exception
    
    def loadUrl(self,url):
        return self.driver.get(url)
    
    def loadHomePageUrl(self):
        return self.driver.loadPage("http://rams-stage.cosmopolitan.com")
    
    def getRandomGallery(self):
        sessionId = self.driver.session_id
        randomId = worker.worker()
        id = randomId.getApiData(sessionId,"unlockedlivegalleryid")
        time.sleep(2)
        searchBox = self.driver.find_element_by_id("group_id")
        searchBox.send_keys(id)
        
        getResults = self.driver.find_element_by_xpath("//*[@id='results_table']/table/tbody/tr/td[1]")
       
        if (getResults != ''):
            count = 1
            currentPageUrl = self.driver.current_url
            loadPage = currentPageUrl+"&edit&group_id="+str(id)
            self.loadUrl(loadPage)
        else:
            count = 0
            return False
