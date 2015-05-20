from configobj import ConfigObj

import pycurl
from urllib import urlencode
import json
from StringIO import StringIO 
import unittest



class Result(): 
    
    def __init__(self,mylist = []):
        self.run = mylist[0]
        self.errors = mylist[1]
        self.fails = mylist[2]
        
        
    def save(self,test):
        result = self.create(test)
        self.send(result)
        
    def create(self,test): 
        data = {}   
        
        data['startTime'] = test.startTime
        data['endTime'] = test.endTime
       
        #config = ConfigObj('C:\Python27\Scripts\PythonSelenium\setup.cfg')
        config = ConfigObj('/usr/local/bin/setup.cfg')
        data['browser'] =  config['nosetests']['browser']
        data['environment'] = config['nosetests']['environment']
        data['site'] = config['nosetests']['site']
        
        if data['environment'] == 'stage':
            data['environment'] = 'staging'
            
        dataid = unittest.TestCase.shortDescription(test)
        data['id'] = dataid.replace("Practitest id :","")
        data['url'] = test.driver.current_url    
        
        if(self.fails > '1' and self.run > '1'):
            data['passed'] = 0
            
        elif (self.fails == '0'):
            print "IAM THIS BEING USED NOW"
            data['passed'] = 1
            
        elif(self.fails == '1'):
            print "OLLa Me Failed"
            data['status'] = 0
            
        elif(self.errors == '1'):
            data['passed'] = 0
        
        data['message'] = ''
        data['screenshot'] = "../screenshot.png"
        data['testset_id'] = 38
        return data;
        
    def send(self,result): 
        c = pycurl.Curl()
        send = c.setopt(c.URL,'http://selenium.hdmtech.net/saveresult/')
        postfields = urlencode(result)
        c.setopt(c.POSTFIELDS, postfields)
        c.perform()        
        c.close()
       
            
        