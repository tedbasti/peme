# peme
This will be a small lisp/scheme interpreter written in python.
It is just developed for and not gonna be serious stuff.

# Steps to be done

## Tokenizer
The tokenizer takes a scheme string and convert it to an array.
This is done with alot of regex

## Parser
The parser will find out what the token is about. 
E.g. 100 is a number, "abcd" is a string and + is an atom (or how ever im gonna call it).
Furthermore it will rebuild the bracket structure with encapsulated (python) lists.

## Eval
Now the magic comes to place.
Execute built in functions ( +, -, define or whatever) and take care of variable values.
Maybe 'if' will be implemented as a function, but thats not sure for now.

## Lambda
This is maybe the hardest part. Give the user the possibility to write own functions
with using the lambda builtin.
Lambda will looks like '(define double (lambda (x) (+ x x)))'.
