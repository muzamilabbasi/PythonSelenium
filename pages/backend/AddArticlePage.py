
import time
from pages.backend import EditorialPage
from random import randint
import re
import unittest
from pages.backend import RamsPage
from selenium.webdriver.common.keys import Keys
<<<<<<< Updated upstream
from numpy.f2py.auxfuncs import throw_error
=======
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from __builtin__ import True
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from classes import helper as helperMethod
import random
>>>>>>> Stashed changes


class AddArticlePage(EditorialPage.EditorialPage):
    
    def __init__(self,driver,loadPage = " "):
        self.loadPage = loadPage
        EditorialPage.EditorialPage.__init__(self,driver,loadPage)
<<<<<<< Updated upstream
     

=======
        self.pgActions_ = pgactions.PageActions(self.driver)
        self.help = helperMethod.helper()
        
        
>>>>>>> Stashed changes
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
       
    def clickWYSIWYGFormatting(self,format,length,region = 'Dek'):
        if (region == 'Dek'):
            articleBodyText = self.getArticleDekBody()
<<<<<<< Updated upstream
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
=======
            #articleBodyText.send_keys(Keys.CONTROL,'A')
            for i in range(length):
                articleBodyText.send_keys(Keys.SHIFT + Keys.LEFT)
            checkFormatting = self.pgActions_.assert_elementPresent(By.XPATH,"//*[@data-command-name='"+format+"']")
            if (checkFormatting is True):
                formatting = self.pgActions_.find_ElementsByXpath("//*[@data-command-name='"+format+"']")
                formatting[0].click()
            else:
                raise Exception("Element Not Visible")
            
        elif (region == "body"):
            articleBody = self.getArticleBody()
            for i in range(length):
                articleBody.send_keys(Keys.SHIFT + Keys.LEFT)
            checkFormatting = self.pgActions_.assert_elementPresent(By.XPATH,"//*[@data-command-name='"+format+"']")
            if (checkFormatting is True):
                formatting = self.pgActions_.find_ElementsByXpath("//*[@data-command-name='"+format+"']")
                formatting[1].click()
            else:
                raise Exception("Element Not Visible")
>>>>>>> Stashed changes
        
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
<<<<<<< Updated upstream
        getButton.click()
=======
        getButton.click()'''
        time.sleep(.5)
        clickInsertButton = "$('.popup_imageInsertButton').click()"
        self.driver.execute_script(clickInsertButton)
>>>>>>> Stashed changes
        
    def getImageId(self):
        getBodytext = self.getHtmlBody()
        replaceStr = getBodytext.replace('loc="C"',"").replace('share="true"',"").replace('expand="true"',"").replace("image id=","").replace("[","").replace("]","").replace('"',"")
        return replaceStr
    
<<<<<<< Updated upstream
    def clickOnGalleryEmbedInsertButton(self,number = 0):
        getButton = self.driver.find_elements_by_xpath("//*[@id='popup_galleryRight']/button")
        if (getButton == " "):
=======
    def clickOnGalleryEmbedInsertButton(self):
        getButton = self.driver.find_element_by_xpath("//*[@id='popup_galleryRight']/button")
        #getButton = self.driver.find_element_by_css_selector("html body div#wrapper.wrapper.templates-present div#contents form.article_form.general_form div.table div.tablerow div.tablecell_rightnav div#body_box.segment div.panel.shaded div.row.article_body div.wysiwyg-toolbar.js-wysiwyg-toolbar div.toolbar-group div.toolbar-btn.btn-popup.rams-icon.rams-icon-gallery.active div.wysiwyg-popup.wysiwyg-popup-embed-gallery div#popup_galleryRight button.popup_galleryInsertButton.white")
        #("//*[@id='popup_galleryRight']")
        if (getButton is None):
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                throw_error("Error")
=======
                raise Exception("Cannot Click")
>>>>>>> Stashed changes
        
    
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
        
<<<<<<< Updated upstream
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
                
=======
    def setItemsToCart(self,text="Headline Test",data=[]):
        articleBody = self.getArticleBody()
        if (articleBody is None):
            raise Exception("Article Body Cannot Be Found")
            
        articleBody.clear()
        toolbar = self.getBodyToolbarNoSpan()
        
        if (toolbar is None):
            raise Exception("Toolbar cannot be found")
        
        toolbar[11].click()
        
        headline = self.driver.find_element_by_xpath("//*[@id='popup_shopHeadline']/input")
        headline.send_keys(text)
        getProductsTextField = self.driver.find_elements_by_xpath("//*[@id='popup_shopProducts']/div/input")
        fields = len(getProductsTextField)
        items = len(data)
        
        randomContent = random.sample(data,items)
        
        for i in range(fields):
            getProductsTextField[i].send_keys(randomContent[i])
        
        if (fields < items):
                insertButton = self.driver.find_element_by_xpath(".//*[@class='popup_shopButtons']/a/i")
                insertButton.click()
                getProductsTextField = self.driver.find_elements_by_xpath("//*[@id='popup_shopProducts']/div/input")
                getProductsTextField[3].send_keys(data[3])
                
        else:
                raise Exception("A Text field can't be added!")
        
        clickInsertButton = self.driver.find_element_by_xpath(".//*[@class='popup_shopButtons']/button")
        clickInsertButton.click()
        
        
    def returnSlugData(self):
        slugData = []
        getUrls = self.help.getRandomSlugs()
        if (getUrls == " "):
            raise Exception("No Slugs Returned")
        
        for url in getUrls:
            data = url.replace("http://shop.harpersbazaar.com/designers","")
            slugData.append(data)
        
        return slugData
    
    def checkForSlugsInArticles(self,slugData):
        myList = []
        getSlugs =  self.getHtmlBody()
        if (getSlugs is None):
            raise Exception("No Slugs found in HtmlBody")     
        
        slugs = getSlugs.replace("[shop headline=""\"TestHeadlines\" source=""\"bazaar\" slugs=\"","")
        strippedSlugs = slugs.split(',')
        for element in slugData:
            if element in strippedSlugs:
                myList.append(element)
            for i in myList:
                if i in strippedSlugs:
                    return True
                else:
                    return False

    def setghkItemsToCart(self,data,text="Headline Test"):
        articleBody = self.getArticleBody()
        if (articleBody is None):
            return False;
            
        articleBody.clear()
        toolbar = self.getBodyToolbarNoSpan()
        
        if (toolbar is None):
            return False
        
        toolbar[11].click()
        
        headline = self.driver.find_element_by_xpath(".//*[@id='popup_shopHeadline']/input")
        headline.send_keys(text)
        getProductsTextField = self.driver.find_element_by_xpath("//*[@id='popup_shopProductID']/input")
        getProductsTextField.send_keys(data)
        clickInsertButton = self.driver.find_element_by_xpath(".//*[@class='popup_shopButtons']/button")
        clickInsertButton.click()
    
    def getBodySlug(self):
        slug = self.pgActions_.assert_ElementIsPresent(By.XPATH, "//*[@id='slug']")
        return slug
    
    def clickImageUpload(self):
        script = "$('.header-content--overlay').click()"
        self.driver.execute_script(script)
      
    def clickUploadImage(self):
        uploadImage = self.driver.find_element_by_xpath("//*[@id='topTabs']/span[2]")
        if (uploadImage is None):
            return False
        uploadImage.click()
            
    def getDataImageId(self):
        if self.pgActions_.assert_elementPresent(By.ID, "popup_imagePlaceholder") is None:
            raise Exception
        return self.pgActions_.find_ElementByID("popup_imagePlaceholder").get_attribute("data-imageid")
        
    def clickLeadImageSearch(self):
        search = '$(".rams-icon-search").eq(1).click()'
        self.driver.execute_script(search)
        id = self.pgActions_.assert_elementPresent(By.ID,"searchInputResultsInner")
        
    def searchLeadImage(self,title):
        searchInput = "//*[@id='searchInputBox']/div/div[1]/input[2]"
        checkSearchInputBox = self.pgActions_.assert_ElementIsPresent(By.XPATH,searchInput)
        if (checkSearchInputBox is None):
            raise Exception
        if self.pgActions_.assert_ElementIsPresent(By.XPATH, "//*[@id='searchInputResults']/div/div") is None:
            raise Exception
        inputBox = self.pgActions_.find_ElementByXpath(searchInput)
        inputBox.send_keys(title)
    
    def clickImageInsideSearch(self, num=0, type = "data-url"):
        checkImageisPresent = self.pgActions_.assert_ElementIsPresent(By.XPATH,"//*[@id='searchInputResultsInner']/div")
        if checkImageisPresent is None:
            raise Exception
        lightBoxSearch = self.driver.find_elements_by_xpath("//*[@id='searchInputResultsInner']/div")
        if (lightBoxSearch == " "):
            return False
        getContentUrl = lightBoxSearch[num].get_attribute(type)
        getContentTitle = lightBoxSearch[num].get_attribute("data-title")
        if (getContentUrl == '' or getContentTitle == ''):
            raise Exception("Content not returned")
        lightBoxSearch[num].click()
        return (getContentUrl,getContentTitle)
        

    def getRandomProductIds(self):
        productIds = ['B00BNLRDZK','B00ICWK6RK','B00C1RX1AQ','B008DI8D7S','B00M7G7ZVW','B004Y1NMN8',
        'B00520C736','B00HNG8ZFQ','B007U9914K','B0080YHBR8','B00H1W9I6C','B009GMUL84','B007MQLMF2',
        'B00BNLRDZK','0672329468','1593272200','1449339530','0596005903','1466518030','1593275676']
        randomIDs = randint(0,len(productIds)-1)
        return productIds[randomIDs]
    
    def stripProductIds(self):
        returnIDMatch = re.findall('product_id="[a-z1-10A-Z1-10-a-z1-10A-z1-10\"]+"',self.getHtmlBody())
        for i in returnIDMatch:
            strippedID = i.replace("product_id=","").replace("\"","")
            return strippedID
>>>>>>> Stashed changes
