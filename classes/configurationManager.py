import sys
from configobj import ConfigObj

class configuration():
   
    def getConfiguration(self):
        if (sys.platform == "darwin"):
            config = ConfigObj('/usr/local/bin/setup.cfg')
            
        elif (sys.platform == "win32"):
            config = ConfigObj('C:\setup.cfg')
        
        else:
            raise Exception("Please Specify the platform")    
        
        return config['nosetests']
