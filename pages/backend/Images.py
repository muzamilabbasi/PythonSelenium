import os
import random
import datetime
from numpy.oldnumeric.random_array import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from classes import configurationManager as cfg
from classes import PageActions as pgactions
from pages.backend import EditorialPage
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes

class Images(EditorialPage.EditorialPage):

    
<<<<<<< Updated upstream
    def __init__(self,driver,loadPage = ""):
        self.loadPage = loadPage
        self.driver = driver
        self.driver.get("http://rams-stage.cosmopolitan.com/img.php")
        #EditorialPage.EditorialPage.__init__(self,driver,loadPage)
=======
    def __init__(self, driver, loadPage=""):
        EditorialPage.EditorialPage.__init__(self, driver, loadPage)
        self.pgActions_ = pgactions.PageActions(self.driver)
        config = cfg.configuration()
        getConfig = config.getConfiguration()
        self.site = getConfig['site']
        self.environment = getConfig['environment']
        
    def loadImagePage(self):
        self.driver.get("http://rams-"+self.environment+"."+self.site+".com/img.php")
            
    def searchImagebyId(self, id=1):
        searchBox = "query"
        _searchBoxIsVisible = self.pgActions_.assert_elementPresent(By.NAME, searchBox)
        
        if (_searchBoxIsVisible is None):
            raise Exception("image search box not visible")
        self.pgActions_.find_ElementByName(searchBox).send_keys(id)
        
        searchButton = "//*[@id='contents']/form/div[1]/div/div/div/div/div/button"
        _searchButtonIsVisible = self.pgActions_.assert_elementPresent(By.XPATH, searchButton)
        if (_searchButtonIsVisible is None):
            raise Exception("Seach Button isn't visible")
        self.pgActions_.find_ElementByXpath(searchButton).click()
>>>>>>> Stashed changes
        
        _checkIfTagPresent = self.pgActions_.assert_elementPresent(By.XPATH, "//*[@id='contents']/h1")
        if (_checkIfTagPresent is None):
            raise Exception("image tag not visible")
        
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
        
    def setImageTitle(self, imgtitle):
        title = self.pgActions_.find_ElementByXpath("//*[@id='image_title']")
        if title is None:
            raise Exception("Element not found")
        title.clear()
        title.send_keys(imgtitle)
        
    def setImageDescription(self, description):
        self.driver.find_element_by_id("description").send_keys(description)
        
    def setImageCaption(self, caption):
        self.driver.find_element_by_id("image_caption").send_keys(caption)
        
    def setImagePeopleTag(self, tags):
        self.driver.find_element_by_xpath("//*[@id='workspace']/div[3]/div/div[4]/div/x-hdm-tagsinput/div/div[1]/input").send_keys(tags)
       
    def setImageTags(self, type, text):
        if (type == 'Product'):
            self.setTags(5, text)
        elif(type == 'Brand'):
            self.setTags(6, text)
        elif(type == 'Content'):
            self.setTags(7, text)
     
    def setTags(self, num, text):
        clickExpand = self.pgActions_.assert_ElementIsPresent(By.XPATH, "//*[@id='workspace']/div[3]/div/div["+str(num)+"]/label/i")
        if clickExpand is False:
            raise Exception("Element not found")
        self.driver.find_element_by_xpath("//*[@id='workspace']/div[3]/div/div["+str(num)+"]/label/i").click()
        self.driver.find_element_by_xpath("//*[@id='workspace']/div[3]/div/div["+str(num)+"]/div/x-hdm-tagsinput/div/div[1]/input").send_keys(text)
    
    def setImageCopyright(self):
        imageCopyRight = self.driver.find_element_by_xpath("//*[@id='image_provider']")
        option = imageCopyRight.find_elements_by_tag_name('option')
        option[randint(0, len(option)-1)].click() 
            
    def setImagePhotographer(self, text):
        imagePhotographer = self.driver.find_element_by_xpath("//*[@id='copyright']")
        imagePhotographer.send_keys(text)
    
    def setImageSyndication(self):
        imageSyndication = self.driver.find_element_by_xpath("//*[@id='syndication_rights']")
        option = imageSyndication.find_elements_by_tag_name('option')
        option[randint(0, len(option)-1)].click()
        
    def setImageRights(self):
        imageRights = self.driver.find_element_by_xpath("//*[@id='image_rights']")
        option = imageRights.find_elements_by_tag_name('option')
        option[randint(0, len(option)-1)].click()
    
    def setEmbargoDate(self):
        self.driver.find_element_by_xpath("//*[@id='workspace']/div[3]/div/div[12]/label/i").click()
        self.setNowInCalendar(0)
        embargoDate = self.pgActions_.find_ElementByID("date")
        convertedDate = datetime.datetime.fromtimestamp(int(embargoDate.get_attribute("value"))).strftime('%Y-%m-%d %H:%M:%S')
        return convertedDate
    
    def setExpiryDate(self):
        self.driver.find_element_by_xpath("//*[@id='workspace']/div[3]/div/div[13]/label/i").click()
        self.setNowInCalendar(1)
        expiryDate = self.pgActions_.find_ElementByID("date_expiry")
        convertedDate = datetime.datetime.fromtimestamp(int(expiryDate.get_attribute("value"))).strftime('%Y-%m-%d %H:%M:%S')
        return convertedDate
    
    def setNowInCalendar(self, num):
        dp = self.driver.find_elements_by_class_name("hasDatepicker")
        dp[num].click()
        self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div[3]/button[1]").click()
        self.driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div[3]/button[2]").click()
    
    def saveImageToServer(self, type='article'):
        button = "//*[@id='workspace']/div[4]/div/div/button"
        clickButton = self.pgActions_.assert_elementPresent(By.XPATH, button)
        if clickButton is None:
            raise Exception("Element Not Found")
        if type == 'article':
            self.pgActions_.find_ElementByXpath(button).click()
            wait = WebDriverWait(self.driver, 120)
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='status positive']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='another']/a[1]")))
        else:
            self.pgActions_.find_ElementByXpath(button).click()
            self.clickEditImage()
            
    def clickEditImage(self):
        button = "//*[@class='another']/a[1]"
        isButton = self.pgActions_.assert_elementPresent(By.XPATH, button)
        if (isButton is False):
            raise Exception("Element Not Found")
        self.driver.find_element_by_xpath(button).click()
    
    def uploadImage(self, location):
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1])", self.driver.find_element_by_xpath("//input[@type='file']"), "0")
        self.driver.execute_script("arguments[0].setAttribute('class', arguments[1])", self.driver.find_element_by_xpath("//input[@type='file']"), "a")
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(location)
    
    def getImageTitle(self):
        imageTitlexpath = "//*[@id='image_title']"
        imageTitle = self.pgActions_.assert_ElementIsPresent(By.XPATH, imageTitlexpath)
        if (imageTitle is None):
            raise Exception("Element Not Found")
        return self.pgActions_.find_ElementByXpath(imageTitlexpath).get_attribute("value")
    
    def getImageMetaData(self):
        metaData = self.driver.find_element_by_xpath("//*[@id='description']")
        if (metaData is None):
            raise Exception("Element Not Found")
        return metaData.text
    
    def getImageCaption(self):
        imageCaption = "//*[@id='image_caption']"
        imageCaptionCheck = self.pgActions_.assert_ElementIsPresent(By.XPATH, imageCaption)
        if (imageCaptionCheck is None):
            raise Exception("Element Not Found")
        return self.pgActions_.find_ElementByXpath(imageCaption).get_attribute("value")
    
    def getImageCopyright(self):
        imageCopyright = self.driver.find_element_by_xpath("//*[@id='image_provider']")
        if (imageCopyright is None):
            raise Exception("Element Not Found")
        myselect = Select(imageCopyright)
        return myselect.first_selected_option.text
    
    def getImagePhotgrapherName(self):
        imagePhotographer = self.driver.find_element_by_xpath("//*[@id='copyright']")
        if (imagePhotographer is None):
            raise Exception("Element Not Found")
        return imagePhotographer.get_attribute("value")
    
    def getSyndicationRights(self):
        syndicationRights = self.driver.find_element_by_xpath("//*[@id='syndication_rights']")
        if (syndicationRights is None):
            raise Exception("Element Not Found")
        myselect = Select(syndicationRights)
        return myselect.first_selected_option.text
    
    def getImageRights(self):
        imageRights = self.driver.find_element_by_xpath("//*[@id='image_rights']")
        if (imageRights is None):
            raise Exception("Element Not Found")
        myselect = Select(imageRights)
        return myselect.first_selected_option.text
    
    def getTags(self, recordNum=1):
        tags = self.driver.find_element_by_xpath("//*[@id='contents']/form/div/div/div[1]/div[3]/div[2]/div['"+str(recordNum)+"']/div/x-hdm-tagsinput/div/div[1]")
        if (tags is None):
            raise Exception("Element Not Found")
        return tags
    
    def getPeopleTags(self):
        self.driver.execute_script("return $('.xtagsChoices:nth-child(1)').html()")
    
    def getProductTags(self):
        productTags = self.getTags(2)
        return productTags.get_attribute("data-value")
    
    def getBrandTags(self):
        self.driver.execute_script("$('.xtagsChoices').first().find('.xtagsTaggedSpan').map(function(){return $(this).attr('data-value');}).get()")
    
    def getContentTags(self):
        contentTags = self.getTags(4)
        return contentTags.get_attribute("data-value")
    
    def getImageFromDir(self):
        PROJECT_ROOT = os.path.expanduser('/Volumes/Data/Users/mabassi/Documents/workspace/newProj')
        imagesDirectory = PROJECT_ROOT + '/images'
        files = os.listdir(imagesDirectory)
        selectImage = random.choice(files)
        return imagesDirectory + '/' + selectImage
    
    def getDates(self):
        imgDates = "//*[@class='date_label note']"
        _checkDateVisible = self.pgActions_.assert_elementPresent(By.XPATH, imgDates)
        if (_checkDateVisible is None):
            raise Exception("image dates not found on edit image page")
        return self.pgActions_.find_ElementsByXpath(imgDates)
    
    def getEmbargoDate(self):
        embargoDate = self.getDates()
        date = datetime.datetime.strptime(embargoDate[0].text, '%b %d %Y %I:%M %p')
        convertedDate = date.strftime('%Y-%m-%d %H:%M:%S')
        return convertedDate
        
    def getExpiryDate(self):
        expiryDate = self.getDates()
        date = datetime.datetime.strptime(expiryDate[0].text, '%b %d %Y %I:%M %p')
        convertedDate = date.strftime('%Y-%m-%d %H:%M:%S')
        return convertedDate
