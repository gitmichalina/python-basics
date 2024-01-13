import unittest
import testfoo, testbar


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testfoo.TestFoo))
    suite.addTest(unittest.makeSuite(testbar.TestBar))
    return suite


if __name__ == "__main__":
    test_suite = suite()
    runner = unittest.TextTestRunner()
    runner.run(test_suite)