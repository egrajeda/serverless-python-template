import unittest

from lib.function import main


class TestSuite(unittest.TestCase):
    def test_main(self):
        self.assertTrue(main({}, {}))
