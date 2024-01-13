import unittest

from get_dig_test import *
from get_digits_test import *


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_get_dig))
    suite.addTest(unittest.makeSuite(test_get_digits))
    return suite


if __name__ == "__main__":
    test_suite = suite()
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
