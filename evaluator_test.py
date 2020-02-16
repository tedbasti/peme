import unittest
from evaluator import *

class MyTestCase(unittest.TestCase):
    def test_evaluate_int(self):
        result = execute([("number", "1")])[0]
        self.assertEqual(type(1), type(result))
        self.assertEqual(result, 1)

    def test_evaluate_float(self):
        result = execute([("number", "1.5")])[0]
        self.assertEqual(type(1.5), type(result))
        self.assertEqual(1.5, result)


    def test_evaluate_plus(self):
        self.assertEqual(6, execute([[("identifier", "+"), ("number", "2"), ("number", "4")]])[0])


if __name__ == '__main__':
    unittest.main()
