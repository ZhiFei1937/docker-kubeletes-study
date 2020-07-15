"""
['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
'__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_addExpectedFailure', '_addSkip', 
'_addUnexpectedSuccess', '_baseAssertEqual', '_classSetupFailed', '_cleanups', '_deprecate', 
'_diffThreshold', '_feedErrorsToResult', '_formatMessage', '_getAssertEqualityFunc', '_outcome', 
'_subtest', '_testMethodDoc', '_testMethodName', '_truncateMessage', '_type_equality_funcs', 
'addCleanup', 'addTypeEqualityFunc', 'assertAlmostEqual', 'assertAlmostEquals', 'assertCountEqual', 
'assertDictContainsSubset', 'assertDictEqual', 'assertEqual', 'assertEquals', 'assertFalse', 
'assertGreater', 'assertGreaterEqual', 'assertIn', 'assertIs', 'assertIsInstance', 'assertIsNone', 
'assertIsNot', 'assertIsNotNone', 'assertLess', 'assertLessEqual', 'assertListEqual', 'assertLogs', 
'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals', 'assertNotEqual', 'assertNotEquals', 
'assertNotIn', 'assertNotIsInstance', 'assertNotRegex', 'assertNotRegexpMatches', 'assertRaises', 
'assertRaisesRegex', 'assertRaisesRegexp', 'assertRegex', 'assertRegexpMatches', 'assertSequenceEqual', 
'assertSetEqual', 'assertTrue', 'assertTupleEqual', 'assertWarns', 'assertWarnsRegex', 'assert_', 'countTestCases', 'debug', 
'defaultTestResult', 'doCleanups', 'fail', 'failIf', 'failIfAlmostEqual', 'failIfEqual', 'failUnless', 
'failUnlessAlmostEqual', 'failUnlessEqual', 'failUnlessRaises', 'failureException', 'id', 'longMessage', 
'maxDiff', 'run', 'setUp', 'setUpClass', 'shortDescription', 'skipTest', 'subTest', 'tearDown', 'tearDownClass']
"""

import os, sys
import unittest
import time
from unittest import mock

class TestHashtable(unittest.TestCase):
    def setUp(self):
        print('do which before test')

    def tearDown(self):
        print('do which after test')

    def test_value(self):
        # time.sleep(3)
        print(dir(self))
        self.assertIn('ac', ['ac'])

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestHashtable('test_value'))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)

    # unittest.main()