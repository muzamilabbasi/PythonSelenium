from selenium.webdriver.common.keys import Keys
import time
from pages.backend import EditorialPage
from random import randint
import re
import unittest
from pages.backend import RamsPage


class AddArticlePage(EditorialPage.EditorialPage):
    
    def __init__(self,driver,loadPage = " "):
        self.loadPage = loadPage
        EditorialPage.EditorialPage.__init__(self,driver,loadPage)
     

    def getArticleBody(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath("//*[@id='body_box']/div[2]/div/div[3]")
    
    def setArticleBodyText(self,text):
        articleBodyText = self.getArticleBody()
        articleBodyText.clear()
        articleBodyText.send_keys(text)
        
    def getArticleDekBody(self):
        articleDek = self.driver.find_element_by_xpath("//*[@class='row sub_heading_div']/div[2]")
        if (articleDek is None):
            return False 
        time.sleep(2)
        return articleDek
    
    def setArticleDekText(self,text):
        articleDek = self.getArticleDekBody()
        articleDek.clear()
        articleDek.send_keys(text)
       
    def clickWYSIWYGFormatting(self,format,region = 'Dek'):
        if (region == 'Dek'):
            articleBodyText = self.getArticleDekBody()
            articleBodyText.send_keys(Keys.CONTROL,'A')
            formatting = self.driver.find_elements_by_xpath("//*[@data-command-name='"+format+"']")
            time.sleep(2)
            formatting[0].click()
        
        elif (region == "body"):
            articleDek = self.getArticleBody()
            articleDek.send_keys(Keys.CONTROL,'A')
            formatting = self.driver.find_elements_by_xpath("//*[@data-command-name='"+format+"']")
            time.sleep(2)
            formatting[1].click()
        
    def clickHtmlView(self,num=1):
        htmlButton = self.driver.find_elements_by_xpath('//*[@class="toolbar-right"]/button[2]')
        htmlButton[num].click()
        
    def getHtmlBody(self):
        return self.driver.find_element_by_xpath("//*[@id='body']").text
    
    def getBodyToolbar(self):
        return self.driver.find_elements_by_xpath("//*[@class='toolbar-group']/div/span")
    
    def getArticleDekHTML(self):
        return self.driver.find_element_by_xpath("//*[@id='sub_heading']").text
    
    def setPullQuotes(self,text):
        articleBody = self.getArticleBody()
        if (articleBody is None):
            return False;
            
        articleBody.clear()
        
        toolbar = self.getBodyToolbar()
        
        if (toolbar is None):
            return False
        
        toolbar[5].click()
        textBox = self.driver.find_element_by_xpath("//*[@class='toolbar-btn btn-popup rams-icon rams-icon-pullquote active']/div/div[1]/textarea")
        if (textBox is None):
            return False;
        textBox.clear()
        textBox.send_keys(text)
    
    def popUpButtons(self,num = 0):
        buttons = self.driver.find_elements_by_xpath("//*[@class='popup-actions']/button")
        if (buttons is None):
            return False
        buttons[num].click()
        
    def clickBodyInternalLinks(self):
        articleBody = self.getArticleBody()
        if(articleBody is None):
            return False
        articleBody.clear()
        
        toolbar = self.getBodyToolbar()
        if (toolbar is None):
            return False
        toolbar[3].click()
        
        internalLink = '$(".js-insert-internal-link").click()'
        self.driver.execute_script(internalLink)
        
    def clickDekInternalLinks(self):
        articleBody = self.getArticleDekBody()
        if(articleBody is None):
            return False
        articleBody.clear()
        
        toolbar = self.getBodyToolbar()
        if (toolbar is None):
            return False
        toolbar[1].click()
        
        internalLink = '$(".js-insert-internal-link").click()'
        self.driver.execute_script(internalLink)
        
    def clickDekExternalLinks(self):
        articleBody = self.getArticleDekBody()
        if(articleBody is None):
            return False
        articleBody.clear()
        
        toolbar = self.getBodyToolbar()
        if (toolbar is None):
            return False
        toolbar[1].click()
        
        internalLink = '$(".js-insert-external-link").click()'
        self.driver.execute_script(internalLink)
            
    def clickBodyExternalLinks(self):
        articleBody = self.getArticleBody()
        if(articleBody is None):
            return False
        articleBody.clear()
        
        toolbar = self.getBodyToolbar()
        if (toolbar is None):
            return False
        toolbar[3].click()
        
        internalLink = '$(".js-insert-external-link").click()'
        self.driver.execute_script(internalLink)
        
    def clickBoxLinks(self,num = 1):
        #links  = self.driver.find_element_by_xpath("//*[@id='body_box']/div[2]/div/div[2]/div[1]/div[2]/ul/li[1]")
        #("//*[@class='toolbar-group']/div[2]/ul/li[1]")
        time.sleep(2)
    
          
    def clickBodyImageEmbed(self):
        articleBody = self.getArticleBody()
        if(articleBody is None):
            return False
        articleBody.clear()
        
        toolbar = self.getBodyToolbar()
        if (toolbar is None):
            return False
        toolbar[7].click()
        
    def clickBodyGalleryEmbed(self):
        articleBody = self.getArticleBody()
        if(articleBody is None):
            return False
        articleBody.clear()
        
        toolbar = self.getBodyToolbar()
        if (toolbar is None):
            return False
        toolbar[8].click()
        
        
        #internalLink = '$(".js-insert-internal-link").click()'
        #self.driver.execute_script(internalLink)    
    
    def lightBox(self,type = "data-url"):
        
        lightBox = self.driver.find_element_by_id("lightbox")
        if (lightBox is None):
            return False
        lightBoxSearch = self.driver.find_elements_by_xpath("//*[@id='searchInputResultsInner']/div")
        if (lightBoxSearch == " "):
            return False
        
        randomContent = randint(0,len(lightBoxSearch))
        
        getContentUrl = lightBoxSearch[randomContent].get_attribute(type) 
        getContentTitle = lightBoxSearch[randomContent].get_attribute("data-title")
        
    
        lightBoxSearch[randomContent].click()
        return (getContentUrl,getContentTitle)
        #<a href="/entertainment/celebs/news/g4747/mtv-movie-awards-2015-red-carpet-photos/">Link (gallery.4747)</a>
        #'''if (not(lightBox.is_visible())):
        #   return False'''
        #if (selector == 'article'):
        #selector = '3'
        #else:
        # selector = "4"
        #searchType = self.driver.find_element_by_xpath(".//*[@id='searchInputOptions']/a[5]")
        #searchType = '$("#searchInputOptions").find("a:eq(3)").click()'
        #self.driver.execute_script(searchType)
        
    def getContentUrlStripped(self):
        htmlBody = self.getHtmlBody()
        url =  re.findall('href="([^"]+)', htmlBody)
        
        data =  str(tuple(map(str, url)))
        lstrip = data.lstrip('(\'')
        rstrip = lstrip.rstrip('\',)')
        return rstrip
    
    def getDekContentUrlStripped(self):
        htmlBody = self.getArticleDekHTML()
        url =  re.findall('href="([^"]+)', htmlBody)
        
        data =  str(tuple(map(str, url)))
        lstrip = data.lstrip('(\'')
        rstrip = lstrip.rstrip('\',)')
        return rstrip
    
    def setArticleEmbedQuote(self,text="abcd",type="facebook"):
        articleBody = self.getArticleBody()
        if (articleBody is None):
            return False;
            
        articleBody.clear()
        
        toolbar = self.getBodyToolbar()
        
        if (toolbar is None):
            return False
        toolbar[6].click()
        
        textBox = self.driver.find_element_by_xpath("//*[@class='toolbar-btn btn-popup rams-icon rams-icon-embed active']/div/textarea")
        if (textBox is None):
            return False;
        textBox.clear()
        textBox.send_keys(text)
        
        dropDownList = self.driver.find_element_by_xpath("//*[@class='toolbar-btn btn-popup rams-icon rams-icon-embed active']/div/div/select[1]")
        dropDownList.find_element_by_xpath("//option[@value='"+type+"']").click()    
        
    def clickOnImageEmbedInsertButton(self):
        getButton = self.driver.find_element_by_xpath("//*[@id='body_box']/div[2]/div/div[2]/div[3]/div[3]/div/button")
        if (getButton is None):
            return False
        getButton.click()
        
    def getImageId(self):
        getBodytext = self.getHtmlBody()
        replaceStr = getBodytext.replace('loc="C"',"").replace('share="true"',"").replace('expand="true"',"").replace("image id=","").replace("[","").replace("]","").replace('"',"")
        return replaceStr
    
    def clickOnGalleryEmbedInsertButton(self):
        getButton = self.driver.find_element_by_xpath("//*[@id='popup_galleryRight']/button")
        if (getButton is None):
            return False
        getButton.click()
        
    def getGalleryId(self):
        getBodytext = self.getHtmlBody()
        replaceStr = getBodytext.replace('gid=',"").replace('embed_gallery',"").replace('type="simple"',"").replace("[","").replace("]","").replace('"',"")
        return replaceStr.strip()
        
                
