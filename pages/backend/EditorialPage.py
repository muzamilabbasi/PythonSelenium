import time
from pages.backend import RamsPage
import re


class EditorialPage(RamsPage.RamsPage):

    def __init__(self,driver,loadPage = " "):
        self.loadPage = loadPage
        #url = "http://rams-stage.cosmopolitan.com/m.php?t=articlesreturn  driver.get(url)
        RamsPage.RamsPage.__init__(self,driver,loadPage)
        
   
    def save(self):                 
        lastSaveTimeElement = self.driver.find_element_by_class_name('last_saved');
        if(lastSaveTimeElement is None):
            return False
        lastSaveTime = lastSaveTimeElement.text    
        element = self.driver.find_element_by_class_name('save_button')
        if(element is None):
            return False
        
        element.click()
<<<<<<< Updated upstream
        time.sleep(2)
       
=======
        time.sleep(5)
>>>>>>> Stashed changes
        if(lastSaveTimeElement.text not in lastSaveTime):
            return True;
        else:
            raise Exception("Cannot Save")

    def getPreviewUrl(self):
        previewUrlElement = self.driver.find_element_by_class_name('preview')
        if (previewUrlElement is None):
            return False
        #if (previewUrlElement == ''):
        #   return False
             
        innerHTML =  previewUrlElement.get_attribute('outerHTML')
        url =  re.findall('url="([^"]+)', innerHTML)
        #if(url == ''):
        #   return False;
        return url        
            
        
            
                