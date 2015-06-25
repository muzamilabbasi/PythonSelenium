'''
@author:muze
This class is created for the functions 
which are used in gallery and article, 
the resusable funcs..s
'''
import sys
from configobj import ConfigObj


class helper():
    
    def getRandomSlugs(self):
        with open('/Volumes/Data/Users/mabassi/Documents/workspace/newProj/util/slugs.txt', 'r') as f:
            slugs = [line.strip() for line in f.readlines()]
            return slugs
