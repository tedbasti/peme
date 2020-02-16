import unittest
from tokenizer import *


class MyTestCase(unittest.TestCase):
    def test_empty_line(self):
        self.assertEqual([], tokenize(""))

    def test_bracket_open(self):
        self.assertEqual([("(", "")], tokenize("("))

    def test_bracket_open_double(self):
        self.assertEqual([("(", ""), ("(", "")], tokenize("(("))

    def test_bracket_close(self):
        self.assertEqual([(")", "")], tokenize(")"))

    def test_bracket_close(self):
        self.assertEqual([(")", ""), (")", "")], tokenize("))"))

    def test_bracket_open_close(self):
        self.assertEqual([("(", ""), (")", "")], tokenize("()"))

    def test_bracket_close_open(self):
        self.assertEqual([(")", ""), ("(", "")], tokenize(")("))

    def test_numeric_atom(self):
        self.assertEqual([("number", "1234")], tokenize("1234"))

    def test_character_atom(self):
        self.assertEqual([("identifier", "character")], tokenize("character"))

    def test_space_end_and_beginning(self):
        self.assertEqual([("(", ""), ("identifier", "+"), ("number", "2"), ("number", "2"), (")", "")],
                         tokenize(" (+ 2 2) "))

    def test_complex_code(self):
        self.assertEqual(
            [("(", ""), ("identifier", "defun"), ("(", ""), ("identifier", "double"), ("identifier", "x"),
             (")", ""), ("(", ""), ("identifier", "+"), ("identifier", "x"), ("identifier", "x"), (")", ""),
             (")", "")],
            tokenize("(defun (double x) (+ x x))"))

    def test_string(self):
        self.assertEqual([("(", ""), ("string", "a b c"), ("number", "123"), (")", "")],
                         tokenize('("a b c" 123)'))

    def test_number_with_dots(self):
        self.assertEqual([("number", "105.2")],
                         tokenize("105.2"))

    def test_number_or_identifier(self):
        self.assertEqual([("identifier", "abc123"), ("number", "123")],
                         tokenize("abc123 123"))

    def test_identifier_with_dots(self):
        self.assertEqual([("identifier", "abc.")], tokenize("abc."))

    def test_unknown_symbol(self):
        with self.assertRaises(LexerException):
            tokenize("!")

if __name__ == '__main__':
    unittest.main()
