
import time
from pages.backend import EditorialPage
from random import randint
import re
import unittest
from pages.backend import RamsPage
from selenium.webdriver.common.keys import Keys
from numpy.f2py.auxfuncs import throw_error


class AddArticlePage(EditorialPage.EditorialPage):
    
    def __init__(self,driver,loadPage = " "):
        self.loadPage = loadPage
        EditorialPage.EditorialPage.__init__(self,driver,loadPage)
     

    def getArticleBody(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath("//*[@id='body_box']/div[2]/div/div[3]")
        
        #script = self.driver.execute_script("$('#body').prev()")
        #print script
        #return script 
    
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
            #articleDek.send_keys(Keys.BACKSPACE)
            formatting = self.driver.find_elements_by_xpath("//*[@data-command-name='"+format+"']")
            time.sleep(2)
            formatting[1].click()
        
        elif (region == "directions"):
            directionsBody = self.getDirectionsBody()
            directionsBody.send_keys(Keys.CONTROL,'A')
            formatting = self.driver.find_elements_by_xpath("//*[@data-command-name='"+format+"']")
            time.sleep(2)
            formatting[2].click()
            
        elif (region == "tips"):
            directionsBody = self.getTipsBody()
            directionsBody.send_keys(Keys.CONTROL,'A')
            formatting = self.driver.find_elements_by_xpath("//*[@data-command-name='"+format+"']")
            time.sleep(2)
            formatting[3].click()
        
    def clickHtmlView(self,num=1):
        htmlButton = self.driver.find_elements_by_xpath('//*[@class="toolbar-right"]/button[2]')
        htmlButton[num].click()
        
    def getHtmlBody(self):
        return self.driver.find_element_by_xpath("//*[@id='body']").text
    
    def getBodyToolbar(self):
        return self.driver.find_elements_by_xpath("//*[@class='toolbar-group']/div/span")
    
    def getArticleDekHTML(self):
        return self.driver.find_element_by_xpath("//*[@id='sub_heading']").text

    def getRecipeDirectionHTML(self):
        return self.driver.find_element_by_xpath("//*[@id='recipe-preparations']").text
        
    def getRecipeTipsHTML(self):
        return self.driver.find_element_by_xpath("//*[@id='recipe-body']").text
        
    
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
    
    def clickDirectionsInternalLinks(self):
        directionsBody = self.getDirectionsBody()
        if(directionsBody is None):
            return False
        directionsBody.clear()
        
        toolbar = self.getBodyToolbar()
        if (toolbar is None):
            return False
        toolbar[12].click()
        internalLink = '$(".js-insert-internal-link").click()'
        self.driver.execute_script(internalLink)
        
    def clickTipsInternalLinks(self):
        tipsBody = self.getTipsBody()
        if(tipsBody is None):
            return False
        tipsBody.clear()
        
        toolbar = self.getBodyToolbar()
        if (toolbar is None):
            return False
        toolbar[15].click()
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
    
    def clickDirectionsExternalLinks(self):
        directionsBody = self.getDirectionsBody()
        if(directionsBody is None):
            return False
        directionsBody.clear()
        toolbar = self.getBodyToolbar()
        if (toolbar is None):
            return False
        toolbar[12].click()
        
        internalLink = '$(".js-insert-external-link").click()'
        self.driver.execute_script(internalLink)
    
    def clickTipsExternalLinks(self):
        tipsBody = self.getTipsBody()
        if(tipsBody is None):
            return False
        tipsBody.clear()
        toolbar = self.getBodyToolbar()
        if (toolbar is None):
            return False
        toolbar[15].click()
        
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
    def clickTipsGalleryEmbed(self):
        tipsBody = self.getTipsBody()
        if(tipsBody is None):
            return False
        tipsBody.clear()
        
        toolbar = self.getBodyToolbar()
        if (toolbar is None):
            return False
        toolbar[20].click()
        time.sleep(10)
    
    def clickTipsImageEmbed(self):
        tipsBody = self.getTipsBody()
        if(tipsBody is None):
            return False
        tipsBody.clear()
        
        toolbar = self.getBodyToolbar()
        if (toolbar is None):
            return False
        toolbar[19].click()
        time.sleep(10)
    
    
    
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
    
    def getDirectionsContentUrlStripped(self): 
        htmlBody = self.getRecipeDirectionHTML()
        url =  re.findall('href="([^"]+)', htmlBody)
        
        data =  str(tuple(map(str, url)))
        lstrip = data.lstrip('(\'')
        rstrip = lstrip.rstrip('\',)')
        return rstrip
    
    def getTipsContentUrlStripped(self): 
        htmlBody = self.getRecipeTipsHTML()
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
    
    def clickOnGalleryEmbedInsertButton(self,number = 0):
        getButton = self.driver.find_elements_by_xpath("//*[@id='popup_galleryRight']/button")
        if (getButton == " "):
            return False
        #print "ClickButton"
        getButton[number].click()
        #embedButton = '$("#popup_galleryRight").eq(1).click()'
        #self.driver.execute_script(embedButton)
        
        
    def getGalleryId(self):
        getBodytext = self.getHtmlBody()
        replaceStr = getBodytext.replace('gid=',"").replace('embed_gallery',"").replace('type="simple"',"").replace("[","").replace("]","").replace('"',"")
        return replaceStr.strip()
    
    def getRecipeTipsGalleryId(self):
        getBodytext = self.getRecipeTipsHTML()
        replaceStr = getBodytext.replace('gid=',"").replace('embed_gallery',"").replace('type="simple"',"").replace("[","").replace("]","").replace('"',"")
        return replaceStr.strip()
    
    def getContent(self,type = "Recipes"):
        contentType = self.driver.find_element_by_xpath("//*[@id='content_type_id']")
        for option in contentType.find_elements_by_tag_name('option'):
            if option.text == type:
                option.click()
            else:
                throw_error("Error")
        
    
    def getIngredients(self):
        ingredients = self.driver.find_elements_by_xpath("//*[@id='recipe-ingredient-name']")
        if (ingredients == " "):
            return False
        return ingredients
    
    def setIngredientOne(self,text="Default Recipe"):
        ingredientOne = self.getIngredients()
        ingredientOne[0].clear()
        ingredientOne[0].send_keys(text)
    
    def setIngredientTwo(self,text="Default Recipe"):
        ingredientOne = self.getIngredients()
        ingredientOne[1].clear()
        ingredientOne[1].send_keys(text)
    
    def getDirectionsBody(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath("//*[@class='special-container']/div[1]/div/div[3]/div[2]")
    
    def getTipsBody(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath("//*[@class='special-container']/div[1]/div[2]/div[2]")

    def setDirectionsForRecipes(self,text = "Default Directions"):
        directionsTextBox = self.getDirectionsBody()
        if (directionsTextBox is None):
            return False
        
        directionsTextBox.clear()
        directionsTextBox.send_keys(text)
    
    def setTipsforRecipes(self,text = "Default Tips"):
        tipsTextBox = self.getTipsBody()
        if (tipsTextBox is None):
            return False
        tipsTextBox.clear()
        tipsTextBox.send_keys(text)
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
                
