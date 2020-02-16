from __future__ import print_function


class ParserException(Exception):
    pass


def parser(tokens):
    return parserInternal(tokens, 0, 0)[0]

def parserInternal(tokens, pos, depth):
    result = []
    while pos < len(tokens):
        if tokens[pos][0] == "(":
            subresult, pos = parserInternal(tokens, pos + 1, depth+1)
            result.append(subresult)
        elif tokens[pos][0] == ")":
            if depth == 0:
                raise ParserException("To many closed brackets")
            return result, pos + 1
        else: #This is a 'real' object for sure!
            result.append(tokens[pos])
            pos += 1
    return result, pos
