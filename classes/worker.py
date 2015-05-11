import pycurl
from urllib import urlencode
import json
from StringIO import StringIO 
from configobj import ConfigObj

class worker():
    
    def getApiData(self,):
        
        config = ConfigObj('/usr/local/bin/setup.cfg')
        site = config['nosetests']['site']
        env = config['nosetests']['environment']
        environment = env.replace("stage","staging")
        #response = cStringIO.StringIO()     
        b = StringIO()
        c = pycurl.Curl()
        #c.setopt(c.URL,'http://selenium.hdmtech.net/'+type+'/')type="unlockedlivearticleid"
        c.setopt(c.URL,'http://selenium.hdmtech.net/unlockedlivearticleid/')
        post_data = {'environment': environment, 'site': site}
        # Form data must be provided already urlencoded.
        postfields = urlencode(post_data)
        # Sets request method to POST,
        # Content-Type header to application/x-www-form-urlencoded
        # and data to send in request body.
        #c.setopt(c.WRITEFUNCTION, response.write) 
        c.setopt(c.POSTFIELDS, postfields)
        c.setopt(c.WRITEFUNCTION, b.write)
        #c.setopt(c.FOLLOWLOCATION, 1)
        #c.setopt(c.MAXREDIRS, 5)
        # put the server's output in here
        c.perform()
        html = b.getvalue()
        c.close()
        #print html.trim.replace("{","").replace('"result"',"").replace('"output"',"").replace("}","").replace(": 1,","").replace(":", "")
        makeList = list(html)
        data = ''.join(makeList)
        id = json.loads(data)
        if (id == " "):
            return False
        else:
            return id["output"]["id"]



