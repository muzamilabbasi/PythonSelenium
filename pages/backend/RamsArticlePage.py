from pages.backend import EditorialPage


class AddArticlePage(EditorialPage.EditorialPage):
    
    def __init__(self,driver,loadPage="m.php?t=articles&add"):
        
        '''if (id != ''):
            self.driver = driver
            url =  "http://rams-stage.cosmopolitan.com/m.php?t=articles&edit&id="+str(id)
            driver.get(str(url))
        else:'''
        EditorialPage.EditorialPage.__init__(self,driver,loadPage)
        #driver.get(url)