from __future__ import print_function

import tokenizer
import parser
import evaluator

try:
    input = raw_input
except NameError:
    pass

def execute(code):
    return evaluator.execute(parser.parser(tokenizer.tokenize(code)))

def main():
    while True:
        line = input("> ")
        result = execute(line)
        for r in result:
            print(r)


if __name__ == "__main__":
    main()