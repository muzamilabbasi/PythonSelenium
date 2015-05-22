import argparse
from subprocess import call
import os
    
if __name__ == '__main__':
    
    #grab the arguments when the script is ran
    parser = argparse.ArgumentParser(description='List options')
    parser.add_argument('--site','-s',help='site information',default='cosmopolitan')
    parser.add_argument('--browser','-b',help='browser information',default='Firefox')
    parser.add_argument('--env','-e',help='environment information',default='stage')
    parser.add_argument('--processes','-p',help='define parallel processes',default=' ')
    parser.add_argument('--ptimeout','-pt',help='define processes timeouts',default='120')
    args = parser.parse_args()
    
    
    if(args.processes != " "):
            #file = open("/usr/local/bin/setup.cfg", "w")
            file = open("C:/setup.cfg", "w")
            #file = open("/Users/mabassi/Documents/workspace/newProj/tests/setup.cfg", "w")
            file.write("[nosetests]\n")
            file.write("browser = \""+args.browser+"\"\n")
            file.write("site = \""+args.site+"\"\n")
            file.write("environment = \""+args.env+"\"\n")
            file.close()
            os.system("nosetests --processes="+args.processes+" "+"--process-timeout="+args.ptimeout+" "+"tests")
    else:
        #file = open("/usr/local/bin/setup.cfg", "w")
        file = open("C:/setup.cfg", "w")
        #file = open("/Users/mabassi/Documents/workspace/newProj/tests/setup.cfg", "w")
        file.write("[nosetests]\n")
        file.write("browser = \""+args.browser+"\"\n")
        file.write("site = \""+args.site+"\"\n")
        file.write("environment = \""+args.env+"\"\n")
        file.close()
        
        #print os.path.expanduser(path)
        #call(["nosetests","\tests"])
        os.system("nosetests tests")
