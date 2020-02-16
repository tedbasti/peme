# peme
This will be a small lisp/scheme interpreter written in python.
It is just developed for fun and not gonna be serious stuff.

# Steps to be done

## Lexer
The lexer(tokenizer) takes a scheme string and convert it to an array.
It finds out that 123 is a number and "b c d" is a string.
A code like '(a "b c d" 123)' will be
  --> [("(", ""), ("identifier", "a"), ("string", "b c d"), ("number", "123"), (")", "")].

## Parser
The parser will find out what the token is about. 
It will rebuild the bracket structure with encapsulated (python) lists.

## Eval
Now the magic comes to place.
Execute built in functions ( +, -, define or whatever) and take care of variable values.
Maybe 'if' will be implemented as a function, but thats not sure for now.

## Lambda
This is maybe the hardest part. Give the user the possibility to write own functions
with using the lambda builtin.
Lambda will looks like '(define double (lambda (x) (+ x x)))'.
