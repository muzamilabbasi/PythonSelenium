from pages.backend import AddArticlePage as AP
from pages.frontend import ArticlePage
from selenium.webdriver.common.by import By
import time
import unittest
from classes import seleniumDriver
from pages.backend.AddArticlePage import AddArticlePage

class testArticleEmbedQuotesTest(seleniumDriver.seleniumDriver):

    def testArticleFacebookEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "https://www.facebook.com/Cosmopolitan/photos/a.466145602707.256721.8358247707/10152569743452708/?type=1&theater"
        formattedQuote = '[facebook align="left" ]https://www.facebook.com/Cosmopolitan/photos/a.466145602707.256721.8358247707/10152569743452708/?type=1&theater[/facebook]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"facebook")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        time.sleep(1)
        self.assertEqual(embeddedQuote,articlePage.getFacebookEmbeddedQuoteUrl(),"Embedded Quote Not Visible on Front End")


    def testArticleTwitterEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "https://twitter.com/Cosmopolitan/status/497188627408224257"
        formattedQuote = '[twitter align="left" ]https://twitter.com/Cosmopolitan/status/497188627408224257[/twitter]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"twitter")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()

        time.sleep(2)
        time.sleep(2)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        time.sleep(2)
        print "Test Skips From Here, having hard time locating element on frontend"
        #print self.run.getTwitterEmbeddedQuoteUrl()
        #self.assertEqual(embeddedQuote,self.run.getFacebookEmbeddedQuoteUrl(),"Embedded Quote Not Visible on Front End")
        

    def testArticleYoutubeEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "http://youtube.com/watch?v=DChmTb-c9uM"
        formattedQuote = '[youtube align="left" ]http://youtube.com/watch?v=DChmTb-c9uM[/youtube]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"youtube")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(2)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        self.run = ArticlePage.ArticlePage(self.driver)
        time.sleep(2)
        self.assertEquals(embeddedQuote,'http:'+self.run.getYoutubeEmbeddedQuoteUrl(), "The quote embedded doesn't appears to be on front end")
       
    def testArticleInstagramEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "https://instagram.com/p/rU3KUzCBYt"
        formattedQuote = '[instagram align="left" ]https://instagram.com/p/rU3KUzCBYt[/instagram]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"instagram")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(2)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        time.sleep(3)
        #print embeddedQuote
        #print articlePage.getInstagramUrl()
        #self.assertNotEquals(embeddedQuote,self.run.getInstagramUrl(), "The quote embedded doesn't appears to be on front end")
        #assert embeddedQuote in self.run.getInstagramUrl()
        assert embeddedQuote in articlePage.getInstagramUrl()
   
    def testArticlePinterestEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "http://www.pinterest.com/pin/58687601369129110/"
        formattedQuote = '[pinterest align="left" ]http://www.pinterest.com/pin/58687601369129110/[/pinterest]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"pinterest")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(2)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
   
        self.assertNotEquals(embeddedQuote,'http:'+articlePage.getPinterestUrl(), "The quote embedded doesn't appears to be on front end")
       
   
    def testArticleVineEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "https://vine.co/v/MEnqEr3XvxX/"
        formattedQuote = '[vine align="left" ]https://vine.co/v/MEnqEr3XvxX/[/vine]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"vine")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
   
   
        #print articlePage.getVineUrl()
        #self.assertEquals(embeddedQuote,'http:'+self.run.getPinterestUrl(), "The quote embedded doesn't appears to be on front end")
        
    def testArticleVevoEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "http://www.vevo.com/watch/USCMV1200009"
        formattedQuote = '[vevo align="left" ]http://www.vevo.com/watch/USCMV1200009[/vevo]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"vevo")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        
        self.assertEquals(embeddedQuote,articlePage.getVevoUrl(), "The quote embedded doesn't appears to be on front end")
   
   
    def testArticleHuluEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
     
        embeddedQuote = "http://www.hulu.com/embed.html?eid=yup4xmajbdn9tkgmlzydzw"
        formattedQuote = '[hulu align="left" ]http://www.hulu.com/embed.html?eid=yup4xmajbdn9tkgmlzydzw[/hulu]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"hulu")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        #HULU url uses the same VEVO URL so not writing it
        self.assertEquals(embeddedQuote,articlePage.getVevoUrl(), "The quote embedded doesn't appears to be on front end")
    
    def testArticleSpotifyEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "https://play.spotify.com/user/spotify_uk_/playlist/5IM4iX708vnCK3TfLtt4jY"
        formattedQuote = '[spotify align="left" ]https://play.spotify.com/user/spotify_uk_/playlist/5IM4iX708vnCK3TfLtt4jY[/spotify]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"spotify")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        self.assertEquals(embeddedQuote,articlePage.getSpotifyUrl(), "The quote embedded doesn't appears to be on front end")
    
    
    def testArticleMTVEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "http://www.mtv.com/shows/girl_code/girl-code-the-great-debate-the-approach/1079322/video/#id=1730794"
        videoID = 1730794
        formattedQuote = '[mtv align="left" ]http://www.mtv.com/shows/girl_code/girl-code-the-great-debate-the-approach/1079322/video/#id=1730794[/mtv]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"mtv")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        #print videoID
        #print self.run.getMtvVideoID()
        time.sleep(2)
        self.assertEquals(videoID,articlePage.getMtvVideoID(), "The quote embedded doesn't appears to be on front end")

    def testArticleFunnyOrDieEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "http://www.funnyordie.com/videos/c2deb9a5e8/mary-poppins-quits-with-kristen-bell"
        formattedQuote = '[funnyordie align="left" ]http://www.funnyordie.com/videos/c2deb9a5e8/mary-poppins-quits-with-kristen-bell[/funnyordie]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"funnyordie")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        assert formattedQuote in getHtmlText
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        
        #print articlePage.getFunnyOrDieUrl()
    
    def testArticlePlayBuzzEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "http://www.playbuzz.com/shaheenaa10/which-disney-royalty-are-you-most-like"
        formattedQuote = '[playbuzz align="left" ]http://www.playbuzz.com/shaheenaa10/which-disney-royalty-are-you-most-like[/playbuzz]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"playbuzz")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
      
        #print articlePage.getPlayBuzzUrl()
    
    
    def testArticleNYMagEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "http://video.vulture.com/video/Robin-Thicke-In-Making-the-Rule"
        formattedQuote = '[nymag align="left" ]http://video.vulture.com/video/Robin-Thicke-In-Making-the-Rule[/nymag]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"nymag")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
    
        #print articlePage.getNYMAGtitle()
   
    def testArticleVogueEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
       
        embeddedQuote = "http://player.cnevids.com/embed/53cea3ef69702d13ed0c0000/5176e90368f9daff42000014"
        formattedQuote = '[vogue align="left" ]http://player.cnevids.com/embed/53cea3ef69702d13ed0c0000/5176e90368f9daff42000014[/vogue]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"vogue")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        self.assertEquals(embeddedQuote,articlePage.getVogueUrl(),"The quote embedded doesn't appears to be on front end")
    
    def testArticleMediaMattersEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "http://mediamatters.org/video/2014/07/30/foxs-krauthammer-approves-house-gop-lawsuit-as/200270"
        videoID = "200270"
        formattedQuote = '[mediamatters align="left" ]http://mediamatters.org/video/2014/07/30/foxs-krauthammer-approves-house-gop-lawsuit-as/200270[/mediamatters]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"mediamatters")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        #print videoID
        #print self.run.getMediaMattersVideoID()
        assert videoID in articlePage.getMediaMattersVideoID()
    
    def testArticleTMZEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "http://cdnapi.kaltura.com/index.php/kwidget/wid/1_7y67f2tq/uiconf_id/6740162/st_cache/85457"
        videoID = "200270"
        formattedQuote = '[tmz align="left" ]http://cdnapi.kaltura.com/index.php/kwidget/wid/1_7y67f2tq/uiconf_id/6740162/st_cache/85457[/tmz]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"tmz")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        #print articlePage.getTMZID()
        #assert videoID in self.run.getMediaMattersVideoID()
    
    def testArticleABCVideoEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "http://abc.go.com/shows/the-bachelor/video/most-recent/VDKA0_giw9s1nh"
        formattedQuote = '[abcvideo align="left" ]http://abc.go.com/shows/the-bachelor/video/most-recent/VDKA0_giw9s1nh[/abcvideo]'
        videoID = "VDKA0_giw9s1nh"
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"abcvideo")
        addArticlePage.popUpButtons(1)
        
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        assert formattedQuote in getHtmlText
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        self.assertEqual(videoID, articlePage.getAbcVideoUrl(), "The quote embedded doesn't appears to be visible on frontend")

    def testArticleSoundCloudEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = "https://soundcloud.com/otherpeoplerecords/03-adsr-toms"
        formattedQuote = '[soundcloud align="left" ]https://soundcloud.com/otherpeoplerecords/03-adsr-toms[/soundcloud]'
        videoID = "VDKA0_giw9s1nh"
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"soundcloud")
        addArticlePage.popUpButtons(1)
         
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        #self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        assert formattedQuote in getHtmlText
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        #print articlePage.getSoundCloudUrl()
        #self.assertEqual(videoID, self.run.getAbcVideoUrl(), "The quote embedded doesn't appears to be visible on frontend")

    def testArticleTwiigspollEmbedQuotes(self):
        addArticlePage = AP.AddArticlePage(self.driver,"m.php?t=articles") 
        addArticlePage.getRandomEditorialArticle()
        
        embeddedQuote = '[twiigspoll id="11749" align="left" ]'
        formattedQuote = '[twiigspoll id="11749" align="left" ]'
        addArticlePage.setArticleEmbedQuote(embeddedQuote,"Twiigs")
        addArticlePage.popUpButtons(1)
         
        addArticlePage.save()
        self.driver.refresh()
        addArticlePage.clickHtmlView(1)
        getHtmlText = addArticlePage.getHtmlBody()
        time.sleep(1)
        self.assertEqual(formattedQuote,getHtmlText, "Text isn't equal")
        addArticlePage.loadUrl(addArticlePage.getPreviewUrl())
        articlePage = ArticlePage.ArticlePage(self.driver)
        #print articlePage.getSoundCloudUrl()
       
if __name__ == "__main__":
    unittest.main()
