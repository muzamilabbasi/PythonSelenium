import glob
import unittest
from classes import Result
import sys,time

class runner(unittest.TestCase):

    def testrun(self):
        testSuite = unittest.TestSuite()
        test_file_strings = glob.glob('Test*.py')
        module_strings = [str[0:len(str)-3] for str in test_file_strings]
        self.startTime = time.time()
        
        [__import__(str) for str in module_strings]
        
        suites = [unittest.TestLoader().loadTestsFromName(str) for str in module_strings]
        
        [testSuite.addTest(suites[0])]#for suite in suites
        print testSuite 
        
        result = unittest.TestResult()
        testSuite.run(result)
        
        #print 'This is the result' ,result.wasSuccessful()
        print 'failure', len(result.failures)
        print 'errors',len(result.errors)
        
        print "Runner Running"
        
        #Ok, at this point, I have a result, how do I display it as the normal unit test
        #command line output?
if __name__ == "__main__":
        unittest.main()