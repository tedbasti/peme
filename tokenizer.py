from __future__ import print_function
import re
import sys

def tokenize(code):
    #Put a space around all brackets and split it
    return re.sub(r"(\(|\))", r" \1 ", code).split()
