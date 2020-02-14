import unittest
from parser import parser

class MyTestCase(unittest.TestCase):
    def test_empty_token(self):
        self.assertEqual(parser([]), [])


if __name__ == '__main__':
    unittest.main()
