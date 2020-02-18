import unittest
from peme import execute

class MyTestCase(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(15, execute("(+ 1 13 1)"))


if __name__ == '__main__':
    unittest.main()
