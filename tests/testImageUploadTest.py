import time

from classes import PageActions as pgactions
from classes import seleniumDriver
from pages.backend import AddArticlePage as AP
from pages.backend import Images as IMG
from pages.frontend import ArticlePage 


class TestImageUploadTest(seleniumDriver.seleniumDriver):
    
    def testArticleImageUploadTest(self):
        """Practitest id :None"""
        self.pgActions_ = pgactions.PageActions(self.driver)
        imageObj = IMG.Images(self.driver)
        addArticlePage = AP.AddArticlePage(self.driver, "m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        addArticlePage.clickImageUpload()
        addArticlePage.clickUploadImage()
        imageObj.uploadImage(imageObj.getImageFromDir())
        
        title = "TestImage" + time.strftime("%H:%M:%S") 
        imageObj.setImageTitle(title)
        imageObj.saveImageToServer('article')
        self.driver.refresh()
        addArticlePage.clickLeadImageSearch()
        addArticlePage.searchLeadImage(title)
        imageTitle = addArticlePage.clickImageInsideSearch() 
        
        self.assertTrue(addArticlePage.save(), "Cannot save an article")
        time.sleep(.5)
        self.assertEquals(title, imageTitle[1], "Image Title are not equal")
    
    def testImageUploadTest(self):
        """Practitest id :None"""
        
        self.pgActions_ = pgactions.PageActions(self.driver)
        imageObj = IMG.Images(self.driver, "img.php?action=upload")
        
        imageObj.uploadImage(imageObj.getImageFromDir())
        
        title = "TestImage" + time.strftime("%H:%M:%S")    
        description = "Image Description" + time.strftime("%H:%M:%S")
        caption = "Image Caption" + time.strftime("%H:%M:%S")
        copyright = "Image Copyright" + time.strftime("%H:%M:%S")
        photographerName = "Image Photographer" + time.strftime("%H:%M:%S")
        peopleTag = "People Tag" + time.strftime("%H:%M:%S")
        
        imageObj.setImageTitle(title)
        imageObj.setImageDescription(description)
        imageObj.setImageCaption(caption)
        imageObj.setImageCopyright()
        imgCopyright = imageObj.getImageCopyright()
        
        imageObj.setImagePhotographer(photographerName)
        
        imageObj.setImageRights()
        imgRights = imageObj.getImageRights()
        
        imageObj.setImageSyndication()
        syndication = imageObj.getSyndicationRights()
        
        imageObj.setImagePeopleTag(peopleTag)
        imageObj.setImageTags('Product', title)
        imageObj.setImageTags('Content', title)
        imageObj.setImageTags('Brand', title)
        embargoDate = imageObj.setEmbargoDate()
        expiryDate = imageObj.setExpiryDate()
        imageObj.saveImageToServer('image')

        self.assertEquals(title, imageObj.getImageTitle())
        self.assertEquals(description, imageObj.getImageMetaData()) 
        self.assertEquals(caption, imageObj.getImageCaption()) 
        self.assertEquals(imgCopyright, imageObj.getImageCopyright()) 
        self.assertEquals(photographerName, imageObj.getImagePhotgrapherName()) 
        self.assertEquals(imgRights, imageObj.getImageRights()) 
        self.assertEquals(syndication, imageObj.getSyndicationRights()) 
        self.assertEquals(embargoDate, imageObj.getEmbargoDate()) 
        self.assertEquals(expiryDate, imageObj.getExpiryDate())
        
    def testArticleImageEmbedUploadTest(self):
        """Practitest id :None"""

        imageObj = IMG.Images(self.driver)
        addArticlePage = AP.AddArticlePage(self.driver, "m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        addArticlePage.clickBodyImageEmbed()
        addArticlePage.clickUploadImage()
        imageObj.uploadImage(imageObj.getImageFromDir())
        
        title = "TestImage" + time.strftime("%H:%M:%S")    
        description = "Image Description" + time.strftime("%H:%M:%S")
        caption = "Image Caption" + time.strftime("%H:%M:%S")
        copyright = "Image Copyright" + time.strftime("%H:%M:%S")
        photographerName = "Image Photographer" + time.strftime("%H:%M:%S")
        peopleTag = "People Tag" + time.strftime("%H:%M:%S")
        
        imageObj.setImageTitle(title)
        imageObj.setImageDescription(description)
        imageObj.setImageCaption(caption)
        
        imageObj.setImagePeopleTag(peopleTag)
        imageObj.setImageTags('Product', title)
        imageObj.setImageTags('Content', title)
        imageObj.setImageTags('Brand', title)
        
        imageObj.setImageCopyright()
        imgCopyright = imageObj.getImageCopyright()
        imageObj.setImagePhotographer(photographerName)
        imageObj.setImageRights()
        imgRights = imageObj.getImageRights()
        
        imageObj.setEmbargoDate()
        imageObj.setExpiryDate()

        imageObj.saveImageToServer('article')
        addArticlePage.clickOnImageEmbedInsertButton()
        
        self.assertTrue(addArticlePage.save(), "cannot save an Article")
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        imageId = addArticlePage.getImageId()
        previewUrl = addArticlePage.getPreviewUrl()

        imageObj.loadImagePage()        
        imageObj.searchImagebyId(imageId)

        self.assertEquals(title, imageObj.getImageTitle())
        self.assertEquals(description, imageObj.getImageMetaData())
        self.assertEquals(caption, imageObj.getImageCaption())
        self.assertEquals(imgCopyright, imageObj.getImageCopyright())
        self.assertEquals(photographerName, imageObj.getImagePhotgrapherName())
        self.assertEquals(imgRights, imageObj.getImageRights())
        
        getImageCutUrl = imageObj.getSourceImageCut()
        getImagePlaceholderCut = imageObj.getImagePlaceHolderCuts()
        addArticlePage.loadUrl(previewUrl) 
        articlePage = ArticlePage.ArticlePage(self.driver)
        
        assert articlePage.getimageUrl() in getImagePlaceholderCut or getImageCutUrl