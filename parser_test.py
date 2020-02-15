import unittest
from parser import *


class MyTestCase(unittest.TestCase):
    def test_empty_token(self):
        self.assertEqual([], parser([])[0])

    def test_atom_object(self):
        self.assertEqual([Element(TYPES.ATOM, 'atom')],
                         parser(['atom'])[0])

    def test_atom_object_brackets(self):
        self.assertEqual([[Element(TYPES.ATOM, 'atom')]],
                         parser(['(', 'atom', ')'])[0])

    def test_wrong_brackets(self):
        with self.assertRaises(ParserException):
            parser(['(', ')', ')'])

    def test_huge(self):
        result,_ = parser(['(', 'defun', '(', 'double', 'x', ')', '(', '+', 'x', 'x', ')', ')'])
        self.assertEqual(
            [[Element(TYPES.ATOM, 'defun'),
             [Element(TYPES.ATOM, 'double'), Element(TYPES.ATOM, 'x')],
             [Element(TYPES.ATOM, '+'), Element(TYPES.ATOM, 'x'), Element(TYPES.ATOM, 'x')]]]
            ,
            result)


if __name__ == '__main__':
    unittest.main()
