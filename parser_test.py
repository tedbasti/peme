import unittest
from parser import *


class MyTestCase(unittest.TestCase):
    def test_empty_token(self):
        self.assertEqual([], parser([]))

    def test_atom_object(self):
        self.assertEqual([("identifier", "atom")],
                         parser([("identifier", "atom")]))

    def test_atom_object_brackets(self):
        self.assertEqual([[("identifier", "atom")]],
                         parser([("(", ""), ("identifier", "atom"), (")", "")]))

    def test_wrong_brackets(self):
        with self.assertRaises(ParserException):
            parser(['(', ')', ')'])

    def test_huge(self):
        # tokenize("(defun (double x) (+ x x))")) # Just to see the original code snippet
        result = parser([("(", ""), ("identifier", "defun"), ("(", ""), ("identifier", "double"), ("identifier", "x"),
         (")", ""), ("(", ""), ("identifier", "+"), ("identifier", "x"), ("identifier", "x"), (")", ""),
         (")", "")])
        self.assertEqual([[("identifier", "defun"),
                           [("identifier", "double"), ("identifier", "x")],
                           [("identifier", "+"), ("identifier", "x"), ("identifier", "x")]]]
            ,result)


if __name__ == '__main__':
    unittest.main()
