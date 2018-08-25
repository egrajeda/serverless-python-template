import os
import unittest

from lib.function import main


class TestSuite(unittest.TestCase):
    def test_main(self):
        os.environ["NAME"] = "Jane Doe"
        self.assertEqual(main({}, {}), {
            "statusCode": 200,
            "body": "Hello! My name is Jane Doe."
        })
