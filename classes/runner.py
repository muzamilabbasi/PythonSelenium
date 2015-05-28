import unittest, doctest,sys

import glob
from concurrencytest import ConcurrentTestSuite, fork_for_tests




testFilePattern = 'tests/*Test.py'
test_files = glob.glob(testFilePattern)
print test_files
testList = []
#for test in test_files:
testList = [str[0:len(str)-3] for str in test_files] 
#print 'TestList: ', testList[0]
suites = [unittest.defaultTestLoader.loadTestsFromName(testList)]
testSuite = unittest.TestSuite(suites)
text_runner = unittest.TextTestRunner().run(testSuite)
#testRunner.teardown()


'''results = unittest.TestSuite()
results.addTest(unittest.makeSuite(testArticleBodyFormattingTest.testsArticleBodyFormattingTests))
results.addTest(unittest.makeSuite(testArticleGalleryEmbedTest.testArticleGalleryEmbedTest))
runner = unittest.TextTestRunner()
runner.run(results)

# Load tests from SampleTestCase defined above
#suite = unittest.TestLoader().loadTestsFromTestCase(SampleTestCase)
#runner = unittest.TextTestRunner()

# Run tests sequentially
#runner.run(suite)

# Run same tests across 4 processes
#concurrent_suite = ConcurrentTestSuite(results, fork_for_tests(4))
#runner.run(concurrent_suite)'''

