import unittest
from tokenizer import tokenize

class MyTestCase(unittest.TestCase):
    def test_empty_line(self):
        self.assertEqual([], tokenize(""))

    def test_bracket_open(self):
        self.assertEqual(['('], tokenize("("))

    def test_bracket_open_double(self):
        self.assertEqual(['(', '('], tokenize("(("))

    def test_bracket_close(self):
        self.assertEqual([')'], tokenize(")"))

    def test_bracket_close(self):
        self.assertEqual([')', ')'], tokenize("))"))

    def test_bracket_open_close(self):
        self.assertEqual(['(', ')'], tokenize("()"))

    def test_bracket_close_open(self):
        self.assertEqual([')', '('], tokenize(")("))

    def test_numeric_atom(self):
        self.assertEqual(['1234'], tokenize("1234"))

    def test_character_atom(self):
        self.assertEqual(['character'], tokenize("character"))

    def test_space_end_and_beginning(self):
        self.assertEqual(['(', '+', '2', '2', ')'], tokenize(" (+ 2 2) "))

    def test_complex_code(self):
        self.assertEqual(
            ['(', 'defun', '(', 'double', 'x', ')', '(', '+', 'x', 'x', ')', ')'],
            tokenize("(defun (double x) (+ x x))"))

if __name__ == '__main__':
    unittest.main()
