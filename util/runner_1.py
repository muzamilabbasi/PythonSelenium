from tests import testArticleDekTest.ArticleDekTest as testArticleDek
from tests import testArticleEmbedQuotesTest.testArticleEmbedQuotesTest as testArticleEmbeddedQuotes
from tests import testArticleExteralLinksTest.testArticleExternalLinksTest as testArticleExternalLinks
from tests import testArticleGalleryEmbedTest.testArticleGalleryEmbedTest as testArticleEmbeddedGallery
from tests import testArticleImageEmbedTest.testArticleImageEmbedTest as testArticleImageEmbed
from tests import testArticleInternalLinksTest.ArticleInternalLinksTest as testArticleInternalLinks
from tests import testArticlePullQuotesTest.ArticlePullQuotesTest as testArticlePullQuotes
from tests import testArticleRecipeGalleryEmbedTest.testArticleRecipeGalleryEmbedTest as testArticleRecipeEmbed
from tests import testArticleRecipeImageEmbedTest.testArticleRecipeImageEmbedTest as testArtcleRecipeImageEmbed
from tests import testArticleRecipesExternalLink.testArticleRecipesExternalLink as testArticleRecipeExternallink
from tests import testArticleBodyFormattingTest.testsArticleBodyFormattingTests as testArticleBody

import unittest, doctest,sys
import glob
import ntpath
from concurrencytest import ConcurrentTestSuite, fork_for_tests
from __builtin__ import str



results = unittest.TestSuite()
results.addTest(unittest.makeSuite(testArticleDek))

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

