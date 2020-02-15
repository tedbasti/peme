from __future__ import print_function
import re
import sys

def tokenize(code):
    #Put a space around all brackets and split it
    return re.sub(r"(\(|\))", r" \1 ", code).split()

def old_tokenize(code):
    result = []
    pos = 0
    lexar = {
        "open brackets": re.compile('\('),
        "close brackets": re.compile('\)'),
        "whitespace": re.compile('\s+'),
        "nowhitespace": re.compile('[^\s\(\)]+')
    }

    while pos < len(code):
        posbefore = pos
        for key, l in lexar.items():
            r = l.match(code[pos:])
            if r:
                if key != "whitespace":
                    result.append(r.group())
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
