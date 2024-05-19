# Racket Multi-Paradigm Translator

The Racket Multi-Paradigm Translator is a tool designed to convert Racket code into Python code. Racket is a functional programming language that supports multiple paradigms, including functional, imperative, and logic programming. This translator focuses on converting Racket's functional constructs into Python's equivalent functional paradigm, using constructs like `map`, `filter`, and comprehensions to replace traditional loops like `while` and `for`.

This translator employs AI technologies to generate parse tree graphs for visualizing the abstract syntax trees (ASTs) of Racket code. These parse tree graphs aid in understanding the structure and behavior of the code during the translation process.

The Translator focus on declarative Python, avoiding traditional imperative constructs - look at functions examples - .


## Features
* **Interpreter Mode**: Allows users to run the translator in an interactive mode.
    * **Usage**:
        * On Unix (Linux/Mac): `python3 -m racket-to-python-translator`
        * On Windows: `python -m racket-to-python-translator`
* **AI-powered Parse Tree Generation**: Utilizes AI technologies from `google.generativeai` and `graphviz` to generate parse tree graphs for visualizing the abstract syntax trees (ASTs) of Racket code. These parse tree graphs aid in understanding the structure and behavior of the code during the translation process.
* **File Translation**: Translates a specific Racket file.
    * **Usage**: `python -m racket-to-python-translator file_name.rkt`
* **Unit Testing**: Supports running unit tests to verify translation accuracy.
    * **Usage**: `python -m racket-to-python-translator/tests/test_name.py`

## Supported Constructs and Examples

### Variable Declarations
- **Racket**: `(define x 10)`
- **Racket Grammar**: `(define <variable> <value>)`
- **Python**: `x = 10`

### Basics
- **Racket**:
  ```racket
  ; comment
  
  (+ 1 2 3)

  (define y (+ x 1))

  (max 3 -2 4.1 1/3)

  (sqrt 9/4)

  (abs -5)

  (display "I'm Racket. Nice to meet you!\n")

  (writeln (sum-of-squares x y)) ; output: 25
  ```
- **Python**:
  ```python
  # comment
  
  add_all((1, 2, 3))

  y = all_add((x, 1))

  max(3, -2, 4.1, 1/3)

  math.sqrt(9/4)

  abs(-5)

  print("I'm Racket. Nice to meet you!\n")

  print(sum_of_squares(x, y)) # output: 25
  ```

### let 
- **Racket**:
  ```racket
  (let ([x 3][y (+ x 1)])(y))
  ```
- **Python**:
  ```python
  print((y:=x + 1))
  ```

### Functions (Declarative vs Imperative)
(Declarative is used)

- **Racket (declarative)**:
  ```racket
  (define square (lambda (x) (* x x)))
  (square 5)
  (display ((lambda (x) (* x x)) 5))
  ```

- **Python (declarative)**:
  ```python
  square = lambda x: x * x
  print(square(5))
  print((lambda x: x * x)(5))
  ```

- **Python (imperative)**:
  ```python
  def square(x):
      return x * x
  print(square(5))
  ```

### Map Function
- **Racket (functional)**:
  ```racket
  (map (lambda (x) (* x 2)) '(1 2 3 4 5))
  ```

- **Python (functional)**:
  ```python
  squared_numbers = list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))
  ```

- **Python (imperative)**:
  ```python
  def square(x):
      return x * x

  numbers = [1, 2, 3, 4, 5]
  squared_numbers = []
  for num in numbers:
      squared_numbers.append(square(num))
  print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
  ```

### Filter Function
- **Racket (functional)**:
  ```racket
  (display (filter (lambda (x) (= (even? x) 0)) '(1 2 3 4 5)))
  ```

- **Python (functional)**:
  ```python
  even_numbers = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
  ```

- **Python (imperative)**:
  ```python
  numbers = [1, 2, 3, 4, 5]
  even_numbers = []
  for num in numbers:
      if num % 2 == 0:
          even_numbers.append(num)
  print(even_numbers)  # Output: [2, 4]
  ```

### Reduce Function
- **Racket (functional)**:
  ```racket
  (display (foldl (lambda (x y) (+ x y)) 0 '(1 2 3 4 5))) ; Output: 15
  ```

- **Python (functional)**:
  ```python
  from functools import reduce
  total_sum = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
  print(total_sum)  # Output: 15
  ```

- **Python (imperative)**:
  ```python
  numbers = [1, 2, 3, 4, 5]
  total_sum = 0
  for num in numbers:
      total_sum += num
  print(total_sum)  # Output: 15
  ```

### if Statements
- **Racket**:
  ```racket
  (if (> x 0) 'positive 'non-positive')
  ```
- **Python**:
  ```python
  'positive' if x > 0 else 'non-positive'
  ```

### `cond` Statements
- **Racket**:
  ```racket
  (define (example x)
   (cond
    [(< x 0) 'negative']
    [(= x 0) 'zero']
    [(> x 0) 'positive']))
  ```
- **Python**:
  ```python
  example = lambda x: (
    'negative' if x < 0 else
    ('zero' if x == 0 else
    ('positive' if x > 0 else None))
   ```
### `cond` Statements
- **Racket**:
  ```racket
  (define (fact-helper n acc)
   (cond
     [(= n 1) acc]
     [else (fact-helper (- n 1) (* n acc))]))
    (define (fact n) (fact-helper n 1))
  ```
- **Python**:
  ```python
  fact_helper = lambda n, acc: acc if n == 1 else fact_helper(n - 1, n * acc)
  fact = lambda n: fact_helper(n, 1)

  ```

### Lambda Function
- **Racket**:
  ```racket
  (define sum_ (lambda (x y) (+ x y)))
  (sum_ 5 3)
  ```
- **Python**:
  ```python
  sum_ = lambda x, y: add_all((x, y))
  print(sum_(5, 3))
  ```

### Map Function
- **Racket**:
  ```racket
  (map (lambda (x) (* x 2)) '(1 2 3 4 5))
  ```
- **Python**:
  ```python
  list(map(lambda x: mul_all(x, x), [1, 2, 3, 4, 5]))
  ```

### Reduce Function
- **Racket**:
  ```racket
  (foldl + 0 '(1 2 3 4 5))
  ```
- **Python**:
  ```python
  from functools import reduce
  reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
  ```

## Advantages
- **Turing Complete**: The subset of Racket supported by this translator is Turing complete, meaning it can compute anything that is computable.
- **Practical Applications**: The translator can be used for practical applications such as matrix multiplication, computer vision, image processing, and solving LeetCode problems.

## Context-Free Grammar (CFG)
```go
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

## Real Applications
### Calculation of Centroid in N Dimensions (N = 1)

- **Racket**:
  ```racket
  (define average (lambda (lst) (/ (foldl (lambda (x y) (+ x y)) 0 lst) (length lst))))
  (display (average (list 1 2 3)))
  ```

- **Python Output**:
  ```python
  from functools import reduce
  import operator
  from math import sqrt

  binary_func_all = lambda func: lambda l: reduce(func, l)
  add_all = binary_func_all(operator.add) # +
  sub_all = binary_func_all(operator.sub) # -
  mul_all = binary_func_all(operator.mul) # *
  div_all = binary_func_all(operator.truediv) # /

  all_binary_func = lambda func: lambda l: all([True if func(l[i -1], l[i]) else False for i in range(1, len(l))])
  all_eq = all_binary_func(operator.eq) # ==
  all_gt = all_binary_func(operator.gt) # >
  all_ge = all_binary_func(operator.ge) # >=
  all_lt = all_binary_func(operator.lt) # <
  all_le = all_binary_func(operator.le) # <=

  average = lambda lst: div_all((reduce(lambda x, y: add_all((x, y)), lst, 0), len(lst)))
  print(average([1, 2, 3]))
  ```

- **Parse Tree**:
  ```
  DefineNode
    ├── IdentifierNode
    │   └── average
    └── LambdaNode
        └── PARAMS
            └── IdentifierNode
                └── lst
        └── EXPRESSION
            └── DivNode
                ├── IdentifierNode
                │   └── lst
                ├── IdentifierNode
                │   └── length
                └── FoldlNode
                    ├── IdentifierNode
                    │   └── lst
                    ├── NumberNode
                    │   └── 0
                    └── LambdaNode
                        ├── PARAMS
                        │   ├── IdentifierNode
                        │   │   └── x
                        └── IdentifierNode
                            └── y
                        └── EXPRESSION
                            └── AddNode
                                ├── IdentifierNode
                                │   └── y
                                └── IdentifierNode
                                    └── x

(display (average (list 1 2 3)))
  ```
DisplayNode
    └── FunctionCallNodeWithOperands
        └── ListNodes
            ├── NumberNode
            │   └── 3
            ├── NumberNode
            │   └── 2
            └── NumberNode
                └── 1
  ```

### Computer Vision and Image Processing
The translator can be used to convert Racket code for image processing tasks into Python. Here's an example of image thresholding:

- **Racket**:
  ```racket
  (display (map (lambda (row) (map (lambda (pixel) (if (> pixel 100) 255 0)) row)) (list (list 123 50 200) (list 150 200 255) (list 100 100 100))))

  ```

- **Python** (translated):
  ```python
  print(map(lambda row: 
                map(lambda pixel: 
                        255 if pixel > 100 else 0, 
                    row), 
            [[123, 50, 200], 
             [150, 200, 255], 
             [100, 100, 100]]))
  ```

### AST Representation
The Abstract Syntax Tree (AST) for the above Racket code is as follows:

```
DisplayNode
    └── MapNode
        └── LambdaNode
            └── PARAMS
                └── IdentifierNode
                    └── row
            └── EXPRESSION
                └── MapNode
                    ├── IdentifierNode
                    │   └── row
                    └── LambdaNode
                        └── PARAMS
                            └── IdentifierNode
                                └── pixel
                        └── EXPRESSION
                            └── IfNode
                                ├── CONDITION
                                │   ├── GreaterNode
                                │   │   ├── NumberNode
                                │   │   │   └── 100
                                │   │   └── IdentifierNode
                                │   │       └── pixel
                                ├── THEN
                                │   ├── NumberNode
                                │   │   └── 255
                                └── ELSE
                                    └── NumberNode
                                        └── 0
```

This demonstrates how the translator converts complex Racket expressions into Python while preserving the functional programming paradigm.

Great! Adding a section to showcase the parse tree graphs generated by AI sounds like a valuable addition. Here's how you can include it in your README:

## Parse Tree Graphs

In this section, we present the parse tree graphs generated by AI for the Racket code examples provided in the previous sections. These graphs visualize the abstract syntax trees (ASTs) of the Racket code, showcasing how the code is structured and how different components interact.

### (> 1 2 (< 3 4 ))

![Condition_Graph](https://github.com/standard-librarian/Racket-Multi-Paradigm-Translator/assets/67175615/0c03eee4-37e6-4cb6-88ca-97d64c77e417)


### (if (= 10 10) 10 5)

![If_Graph](https://github.com/standard-librarian/Racket-Multi-Paradigm-Translator/assets/67175615/171af9d5-d1ce-4bd7-a9f1-bcca9b3c3355)


### (display (define x 10))

![Display_Graph](https://github.com/standard-librarian/Racket-Multi-Paradigm-Translator/assets/67175615/30c811d6-262a-4d9c-ab54-04f9f04cb473)

These parse tree graphs offer insights into the internal representation of the code and how it is translated into Python. They aid in understanding the transformation process and can be helpful for debugging and code optimization.

## Exporting Parse Trees

The parse tree graphs are generated by AI tools and can be exported as PNG images or PDF files for further analysis and documentation purposes.

## License
This project is licensed under the MIT License.

