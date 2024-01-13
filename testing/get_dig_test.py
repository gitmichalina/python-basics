import unittest
from get_dig import *


class test_get_dig(unittest.TestCase):
    def test_get_digits(self):
        s = get_dig("<0.12-34 56abc789x")
        self.assertEqual(list("0123456789"), get_dig(s))
        self.assertEqual(list("1230"), get_dig(1230))


if __name__ == '__main__':
    unittest.main()


