# Racket Multi-Paradigm Translator

## Features
* **Interpreter Mode**: Allows users to run the translator in an interactive mode.
    * **Usage**:
        * On Unix (Linux/Mac): `python3 -m racket-to-python-translator`
        * On Windows: `python -m racket-to-python-translator`
* File Translation: Translates a specific Racket file.
    * Usage: `python -m racket-to-python-translator file_name.rkt`
* Unit Testing: Supports running unit tests to verify translation accuracy.
    * Usage: `python -m racket-to-python-translator/tests/test_name.py`

## Supported Tokens and Examples
1. Variable Declarations:
    * Racket: `(define x 10)`
    * Racket Grammer: `(define <variable> <value>)`
    * Python: `x = 10`
1. Functions:
2. Conditional Statements:
3. Loops:
4. List Operations:

## Real Applications
### Matrix Multiplication
### Computer Vision and image processing
### leetcode problems

## CFG
``` go
<program> ::= <expression> | <expression> <program>

<expression> ::= <define> | <function> | <if> | <for> | <map> | <lambda> | <let> | <begin>

<define> ::= "(define" <variable> <value> ")"

<function> ::= "(define" "(" <function-name> <parameters> ")" <body> ")"
<parameters> ::= <variable> | <variable> <parameters>
<body> ::= <expression> | <expression> <body>

<if> ::= "(if" <condition> <then-branch> <else-branch> ")"
<condition> ::= <expression>
<then-branch> ::= <expression>
<else-branch> ::= <expression>

<for> ::= "(for" "(" "[" <variable> "(" "in-range" <start> <end> ")" "]" ")" <body> ")"
<start> ::= <number> | <variable>
<end> ::= <number> | <variable>

<map> ::= "(map" <function> <list> ")"
<list> ::= "'" "(" <elements> ")"
<elements> ::= <value> | <value> <elements>

<lambda> ::= "(lambda" "(" <parameters> ")" <body> ")"

<let> ::= "(let" "(" "[" <variable> <value> "]" ")" <body> ")"

<begin> ::= "(begin" <expressions> ")"
<expressions> ::= <expression> | <expression> <expressions>

<variable> ::= <identifier>
<value> ::= <number> | <string> | <boolean> | <variable> | <function-call>
<function-call> ::= "(" <function-name> <arguments> ")"
<arguments> ::= <value> | <value> <arguments>

<function-name> ::= <identifier>

<identifier> ::= <letter> | <letter> <identifier>
<letter> ::= "a" | "b" | "c" | ... | "z" | "A" | "B" | "C" | ... | "Z"
<number> ::= <digit> | <digit> <number>
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<string> ::= "\"" <characters> "\""
<characters> ::= <character> | <character> <characters>
<character> ::= <letter> | <digit> | <symbol>
<symbol> ::= "!" | "@" | "#" | "$" | "%" | "^" | "&" | "*" | "(" | ")" | "-" | "_" | "=" | "+" | "[" | "]" | "{" | "}" | ";" | ":" | "'" | "<" | ">" | "," | "." | "?" | "/"
<boolean> ::= "#t" | "#f"

```
