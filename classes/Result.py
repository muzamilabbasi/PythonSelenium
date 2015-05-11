from configobj import ConfigObj

import pycurl
from urllib import urlencode
import json
from StringIO import StringIO 

class Result(): 
    
    def save(self,test):
        result = self.create(test)
        self.send(result)
        
    def create(self,test): 
        data = {}   
        
        data['startTime'] = test.startTime
        data['endTime'] = test.endTime
        
        config = ConfigObj('C:\Python27\Scripts\PythonSelenium\setup.cfg')
        
        data['browser'] =  config['nosetests']['browser']
        data['environment'] = config['nosetests']['environment']
        data['site'] = config['nosetests']['site']
        
        if data['environment'] == 'stage':
            data['environment'] = 'staging'
            
     #  data['status'] = test.status   
     #   data['message'] = ''
     #   data['id'] = ''    
     #   data['screenshot'] = ""
        data['url'] = test.driver.current_url
     
        return data;
        
    def send(self,result): 
        
        c = pycurl.Curl()
        c.setopt(c.URL,'http://selenium.hdmtech.net/saveresult/')
        postfields = urlencode(result)

        c.setopt(c.POSTFIELDS, postfields)
        c.perform()        
        c.close()
       
            
        