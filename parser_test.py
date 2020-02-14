import unittest
from parser import parser
from parser import Element
from parser import TYPES


class MyTestCase(unittest.TestCase):
    def test_empty_token(self):
        self.assertEqual([], parser([]))

    def test_atom_object(self):
        self.assertEqual([Element(TYPES.ATOM, 'atom')],
                         parser(['atom']))

    def test_atom_object_brackets(self):
        self.assertEqual([[Element(TYPES.ATOM, 'atom')]],
                         parser(['(', 'atom', ')']))

    def test_wrong_brackets(self):
        parser(['(', ')', ')', ')'])


if __name__ == '__main__':
    unittest.main()
