from __future__ import print_function
import re
import sys


class Lexer:
    def __init__(self, regex, name, valueNeeded=True, skip=False):
        self.regex = regex # the regex to be used
        self.name = name # The name of the token (--> "string" <--, "Michael")
        self.valueNeeded = valueNeeded # Is the value of the token needed?
        self.skip = skip # Skip the fields (whitespaces are skipped


def tokenize(code):
    result = []
    pos = 0
    lexer = [
        Lexer(re.compile('\('), "(", False), # Open brackets
        Lexer(re.compile('\)'), ")", False), # Closing brackets
        Lexer(re.compile('".*"'), "string"), # Strings "a b c d"
        Lexer(re.compile('\s+'), "whitespace", False, True), # Skip whitespaces
        Lexer(re.compile('[a-zA-Z\+\-\/\*][a-zA-Z0-9\+\-\/\*]*'), "identifier"), # identifier
        Lexer(re.compile('[0-9.]+'), "number"),  # numbers
    ]

    while pos < len(code):
        posbefore = pos
        for l in lexer:
            r = l.regex.match(code[pos:])
            if r:
                if not l.skip:
                    value = ""
                    if l.valueNeeded:
                        value = r.group()
                    #This is ugly, but gets rid of the ""
                    if l.name == "string":
                        value = r.group()[1:-1]
                    result.append((l.name, value))
                pos += r.end()
                break
        # When the position doesnt change,
        # no regex matches.
        if posbefore == pos:
            print("Invalid Symbol beginning at:")
            print(code[pos:])
            print("At position:")
            print(pos)
            print("Code:")
            print(code)
            sys.exit(1)
    return result
