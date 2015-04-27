import unittest

class ArticlePage(unittest.TestCase):
    
    def __init__(self,driver):
        
        '''if (id != ''):
            self.driver = driver
            url =  "http://rams-stage.cosmopolitan.com/m.php?t=articles&edit&id="+str(id)
            driver.get(str(url))
        else:'''
        self.driver = driver
    
    def getBodyTextStyle(self):
        getElements = self.driver.find_elements_by_xpath("//*[@class='article-body--content']/div[2]/p")
        for i in getElements:
            attr = i.get_attribute("innerHTML")
            return attr
        
    def getArticleDekText(self):
        getText = self.driver.find_element_by_class_name("article-sub-title")
        return getText.text
    
    def getPullQuoteText(self):
        pullQuote = self.driver.find_element_by_xpath("//*[@class='article-body--content']/div[2]/div[2]/p")
        if (pullQuote is None):
            return False
        return pullQuote.get_attribute("innerHTML")
    
    def getPullQuoteIcon(self):
        pullQuoteIcon = self.driver.find_elements_by_xpath("//*[@class='article-body--content']/div[2]/div[2]/div")
        if (pullQuoteIcon is None):
            return False
        return True
    
    def clickInternalLinkContent(self):
        internalLink = self.driver.find_element_by_xpath("//*[@class='article-body--content']/div[2]/p/a")
        if (internalLink is None):
            return False
        return internalLink.click()

    def clickDekInternalLinkContent(self):
        internalLink = self.driver.find_element_by_xpath("//*[@id='site-wrapper']/article/header/h2/a")
        if (internalLink is None):
            return False
        return internalLink.click()
    
    
    def getFacebookEmbeddedQuoteUrl(self):
        getUrl = self.driver.find_element_by_class_name("fb_iframe_widget")
        if (getUrl is None):
            return False
        
        url = getUrl.get_attribute("data-href")
        return url
    
    def getTwitterEmbeddedQuoteUrl(self):
        getUrl = self.driver.find_element_by_xpath("//*[@id='twitter-widget-0']/blockquote/div[1]/div/a")
        
        print getUrl
        '''if (getUrl is None):
            print "NONE IS"
            return False
        
        url = getUrl.get_attribute("cite")
        return url'''
    
    def getYoutubeEmbeddedQuoteUrl(self):
        getUrl = self.driver.find_element_by_xpath("//*[@class='embed--iframe-container']/iframe")
        
        if (getUrl is None):
            return False
        
        url = getUrl.get_attribute("data-src")
                
        formattedUrl = url.replace('embed/', 'watch?v=')
        return formattedUrl
    
    def getInstagramUrl(self):
        getUrl = self.driver.find_element_by_xpath("//*[@class='embed--inner']/iframe")
        
        if (getUrl is None):
            return False
        
        url = getUrl.get_attribute("src")
        return url.replace("/embed/captioned/?v=4"," ")
    
    
    def getPinterestUrl(self):
        getUrl = self.driver.find_element_by_xpath("//*[@id='site-wrapper']/article/div[1]/div[2]/div[2]/div[2]/div[2]/span/a")
        
        if (getUrl is None):
            return False
        
        url = getUrl.get_attribute("data-pin-href")
        return url.replace("repin/x/", " ")

    
    def getVineUrl(self):
        getUrl = self.driver.find_element_by_xpath("//*[@class='embed--iframe-container']/iframe")
        
        if (getUrl is None):
            return False
        
        url = getUrl.get_attribute("src")
        return url
    
    def getVevoUrl(self):
        getUrl = self.driver.find_element_by_xpath("//*[@class='embed--iframe-container']/iframe")
        
        if (getUrl is None):
            return False
        
        url = getUrl.get_attribute("src")
        replacedUrl = url.replace("cache", "www")
        strippedUrl = replacedUrl.replace("m/html/embed.html?video=","watch/")
        return strippedUrl
    
    
    def getSpotifyUrl(self):
        getUrl = self.driver.find_element_by_xpath("//*[@class='embed--inner']/div/iframe")
        
        if (getUrl is None):
            return False
        
        url = getUrl.get_attribute("data-src")
        return url.replace("https://embed.spotify.com/?uri=","")
    
    
    def getMtvVideoID(self):
        getUrl = self.driver.find_element_by_xpath("/html/body/div[4]/article/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/iframe")
        if (getUrl is None):
            return False
        
        url = getUrl.get_attribute("src")
        return url.replace("http://media.mtvnservices.com/embed/mgid:uma:video:mtv.com:", " ")
    
    def getFunnyOrDieUrl(self):
        getUrl = self.driver.find_element_by_xpath("//*[@id='videoContainer']/div[1]/div/video")
        if (getUrl is None):
            return False
        
        #url = getUrl.get_attribute("data-src")
        return getUrl
    
    
    def getPlayBuzzUrl(self):
        getUrl = self.driver.find_element_by_css_selector("html body.gamedetailsbackground section.main_section.feed_main_section.autoHeight.multiple_items_display div.play_main_container.isHover.play_language_en-US div#columns_container div.game_left_col div#open_page_container div.opening_page_wrapper div.opening_page_data div.game_image_wrapper img.game_image_inner")
        if (getUrl is None):
            return False
        
        #url = getUrl.get_attribute("data-src")
        return getUrl
    
    def getNYMAGtitle(self):
        getTitle = self.driver.find_element_by_xpath("//*[@id='magnify_player_title_link']")
        print getTitle.text
        
    def getVogueUrl(self):
        getUrl = self.driver.find_element_by_xpath("//*[@id='site-wrapper']/article/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/iframe")
        if (getUrl is None):
            return False
        
        url = getUrl.get_attribute("data-src")
        return url
    
    
    def getMediaMattersVideoID(self):
        getUrl = self.driver.find_element_by_xpath("//*[@id='site-wrapper']/article/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/iframe")
        if (getUrl is None):
            return False
        
        url = getUrl.get_attribute("data-src")
        return url.replace("http://mediamatters.org/embed/","")
    
    def getTMZID(self):
        getId = self.driver.find_element_by_xpath("xhtml:html/xhtml:body/xhtml:embed")
        print getId
        
    def getAbcVideoUrl(self):
        getUrl = self.driver.find_element_by_xpath("//*[@id='site-wrapper']/article/div[1]/div[2]/div[2]/div[2]/div[2]/iframe")
        if (getUrl is None):
            return False
        
        url = getUrl.get_attribute("data-src")
        return url.replace("http://abc.go.com/embed/","")
    
    def getSoundCloudUrl(self):
        getUrl = self.driver.find_element_by_xpath("//*[@ID='WIDGET']/DIV[2]/DIV/DIV[1]/DIV/DIV[2]/DIV/DIV/DIV[3]/DIV/A[2]")
        if (getUrl is None):
            return False
        
        #url = getUrl.get_attribute("href")
        return getUrl
    
    def getimageUrl(self,type = "src"):
        imageUrl = self.driver.find_element_by_xpath("//*[@class='embedded-image--inner']/img")
        if (imageUrl is None):
            return False
        return imageUrl.get_attribute(type)
    
    def getGalleryShortTitle(self):
        return self.driver.find_element_by_xpath("//*[@id='site-wrapper']/article/div[1]/div[2]/div[2]/div[2]/div[2]/a/div[2]/div[2]").text
        
    
    