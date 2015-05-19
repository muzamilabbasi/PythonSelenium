from classes import Result
import pycurl
from urllib import urlencode
import urllib

class sendResults():


    def sendRes(self):
        result = Result.Result()
        data =  "status=1&screenshot=abcd&url=https%3A%2F%2Frams-stage.cosmopolitan.com%2Fm.php%3Ft%3Darticles%26edit%26id%3D29347&site=cosmopolitan&environment=staging&startTime=1431709114.63&message=Test+passed&endTime=1431709158.64&id=280&browser=Firefox"   
        url=urllib.unquote(data).decode('utf8') 
        output = result.send(url)
        print "Send Result Class Output",output