from __future__ import print_function


# This is a class to store every element
# and its value
class Element:
    def __init__(self, dtype, value):
        self.dtype = dtype
        self.value = value

    #Equals to check with == (e.q. for the tests)
    def __eq__(self, other):
        return type(other) == Element \
               and self.dtype == other.dtype \
               and self.value == other.value

    #not equals
    def __ne__(self, other):
        return not self.__eq__(other)

    #toString() method
    def __str__(self):
        return "dtype: " + self.dtype + ", value " + self.value

    #Seems like within lists this is called instead of __str__()
    def __repr__(self):
        return self.__str__()


class TYPES:
    INTEGER = 1
    STRING = 2
    ATOM = 3


class ParserException(Exception):
    pass


def parser(tokens, pos=0, depth=0):
    result = []
    while pos < len(tokens):
        if tokens[pos] == "(":
            subresult, pos = parser(tokens, pos + 1, depth+1)
            result.append(subresult)
        elif tokens[pos] == ")":
            if depth == 0:
                raise ParserException("To many closed brackets")
            return result, pos + 1
        else: #This is a 'real' object for sure!
            #At the moment everything is just an atom.
            #TODO: here need to be checked, if this is an
            #atom, a string, a number or whatever is possible
            result.append(Element(TYPES.ATOM, tokens[pos]))
            pos += 1
    return result, pos
