import pycurl
from urllib import urlencode
import json,sys
from StringIO import StringIO 
from configobj import ConfigObj

class worker():
    
    def getApiData(self,session,type="unlockedlivearticleid"):
        if (sys.platform == "darwin"):
            config = ConfigObj('/usr/local/bin/setup.cfg')
        elif (sys.platform == "win32"):
            config = ConfigObj('C:\setup.cfg')    
        env = config['nosetests']['environment']
        site = config['nosetests']['site']
        environment = env.replace("stage","staging")
        b = StringIO()
        c = pycurl.Curl()
        
        c.setopt(c.URL,'http://selenium.hdmtech.net/'+type+'/')
        post_data = {'environment': environment, 'site': site, 'session': ''+session+'' }
        postfields = urlencode(post_data)
        c.setopt(c.POSTFIELDS, postfields)
        c.setopt(c.WRITEFUNCTION, b.write)
        c.perform()
        html = b.getvalue()
        c.close()
        
        makeList = list(html)
        data = ''.join(makeList)
        id = json.loads(data)
        try:
            if (id !=" "):
                return id["output"]["id"]
            
        except ValueError as e:
                raise Exception("Cannot return Id's from API")
                
    def getItems(self,site="harpersbazaar"):
        num=4
        b = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL,'http://selenium.hdmtech.net/products/'+site+'/'+str(num)+'')
        post_data = {}
        postfields = urlencode(post_data)
        c.setopt(c.POSTFIELDS, postfields)
        c.setopt(c.WRITEFUNCTION, b.write)
        c.perform()
        html = b.getvalue()
        c.close()
        makeList = list(html)
        data = ''.join(makeList)
        url = json.loads(data)
        try:
            if (url != ""):
                return url['output']['products']
        except ValueError as e:
                raise Exception("Cannot return data from API")
            

    def unlockSession(self,session,type):
        if (sys.platform == "darwin"):
            config = ConfigObj('/usr/local/bin/setup.cfg')
        elif (sys.platform == "win32"):
            config = ConfigObj('C:\setup.cfg')    
        env = config['nosetests']['environment']
        site = config['nosetests']['site']
        environment = env.replace("stage","staging")
        b = StringIO()
        c = pycurl.Curl()
        
        c.setopt(c.URL,'http://selenium.hdmtech.net/'+type+'/')
        post_data = {'environment': environment, 'site': site, 'session': ''+session+'' }
        postfields = urlencode(post_data)
        c.setopt(c.POSTFIELDS, postfields)
        c.setopt(c.WRITEFUNCTION, b.write)
        c.perform()
        html = b.getvalue()
        c.close()
        
    def getUrls(self,type):
        if (sys.platform == "darwin"):
            config = ConfigObj('/usr/local/bin/setup.cfg')
        elif (sys.platform == "win32"):
            config = ConfigObj('C:\setup.cfg')    
        env = config['nosetests']['environment']
        site = config['nosetests']['site']
        environment = env.replace("stage","staging")
        b = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL,'http://selenium.hdmtech.net/'+type+'/')
        post_data = {'environment': environment, 'site': site}
        postfields = urlencode(post_data)
        c.setopt(c.POSTFIELDS, postfields)
        c.setopt(c.WRITEFUNCTION, b.write)
        c.perform()
        html = b.getvalue()
        c.close()
        makeList = list(html)
        data = ''.join(makeList)
        url = json.loads(data)
        try:
            if (url != ""):
                return url['output']['urls']
        except ValueError as e:
                raise Exception("Cannot return data from API")