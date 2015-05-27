from pages.backend import EditorialPage
from configobj import ConfigObj

class Images(EditorialPage.EditorialPage):
    
    def __init__(self,driver,loadPage = ""):
        self.loadPage = loadPage
        self.driver = driver
        #config = ConfigObj('C:\Python27\Scripts\PythonSelenium\setup.cfg')
        config = ConfigObj('/usr/local/bin/setup.cfg')
        site = config['nosetests']['site']
        env = config['nosetests']['environment']
        self.driver.get("http://rams-stage."+site+".com/img.php")
        
        
          
        
        #self.driver.get("http://rams-stage.cosmopolitan.com/img.php")
        #EditorialPage.EditorialPage.__init__(self,driver,loadPage)
        
    def searchImagebyId(self,id = 1):
        textBox = self.driver.find_element_by_name("query")
        
        if (textBox is None):
            return False
        textBox.clear()
        textBox.send_keys(id)
        
        button = self.driver.find_element_by_xpath("//*[@id='contents']/form/div[1]/div/div/div/div/div/button")
        if (button is None):
            return False
        button.click()
        
    def getSourceImageCut(self):
        source = self.driver.find_element_by_xpath("//*[@class='row']/a")
        if (source is None):
            return False
        return source.get_attribute("href")
    
    
    def getImagePlaceHolderCuts(self):
        imageCuts = self.driver.find_elements_by_xpath("//*[@class='image_placeholder']/a/img")
        if (imageCuts == " "):
            return False
        data = []
        for i in imageCuts:
            data = i.get_attribute("src")
            return [data for i in imageCuts]
        