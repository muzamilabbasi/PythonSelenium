import pycurl
from urllib import urlencode
import json
from StringIO import StringIO 
from configobj import ConfigObj

    
        
#config = ConfigObj('../setup.cfg')
config = ConfigObj('/usr/local/bin/setup.cfg')

env = config['nosetests']['environment']
site = config['nosetests']['site']
environment = env.replace("stage","staging")
#response = cStringIO.StringIO()     
b = StringIO()
c = pycurl.Curl()

session = 'a3eb197e-790b-344b-8e6e-5df2301f4c11'
c.setopt(c.URL,'http://selenium.hdmtech.net/unlocksession/')
post_data = {'environment': environment, 'site': site, 'session': ''+session+''}



#c.setopt(c.URL,'http://selenium.hdmtech.net/'+type+'/')type="unlockedlivearticleid"
#c.setopt(c.URL,'http://selenium.hdmtech.net/unlockedlivearticleid/')
#post_data = {'environment': environment, 'site': site}
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
print html

c.close()
#print html.trim.replace("{","").replace('"result"',"").replace('"output"',"").replace("}","").replace(": 1,","").replace(":", "")
makeList = list(html)
data = ''.join(makeList)
id = json.loads(data)
try:
    if (id != " "):
        print id["output"]["id"]
except ValueError as e:
        raise Exception("Cannot return Id's from API")
               
           
           



