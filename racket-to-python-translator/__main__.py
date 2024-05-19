import sys
import os
import argparse
import google.generativeai as genai
import graphviz
GOOGLE_API_KEY = 'AIzaSyC9vl1ZmmDg9kQ-g7sAuYCM6FhjvuBzOnI'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
from .lexer import Lexer
from .parser import Parser
from .parse_tree_printer import print_parse_tree


def test_line(racket_line: str):
    lexer = Lexer()
    tokens = lexer.tokenize_line(racket_line)
    parser = Parser(tokens)
    ast = parser.parse()
    python_code = None
    if ast:
        python_code = ast.generate_python_code()
    return python_code


def main(filename=None, ai=None):
    lexer = Lexer()        
    if filename:
        with open("parse_tree.txt", "w") as file:
            file.write("")
        with open("output_code.py", "w") as file:
            file.write("")
        with open("output_code.py", "a") as file:
            file.write(
                """
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

"""
            )
        with open(filename, "r") as file:
            ai_text = ""
            for line in file:
                tokens = lexer.tokenize_line(line)
                parser = Parser(tokens)
                ast = parser.parse()
                if ast:
                    python_code = ast.generate_python_code()
                    tree = print_parse_tree(ast)
                    with open("output_code.py", "a") as file:
                        file.write(python_code + "\n")
                    with open("parse_tree.txt", "a") as file:
                        file.write("\n" + line + "\n" + tree)
                        ai_text += "\n" + tree

            if ast and ai:
                book1 = "Compiler Principles, Techniques, & Tools, Second edition, Jeffery D. Ullman, Alfred V. Aho, Monica S. Lam, and Ravi Sethi, 2006"
                book2 = "Engineering a Compiler, Keith Cooper, Linda Torczon, second edition, 2011"
                book3 = "Modern Compiler Implementation in Java, Second Edition, Andrew W. Appel and Jens Palsberg"
                prompt=f"Take a deep breath and act as an Academic Professor teaching these books ${book1}, ${book2}, ${book3} Compilers course and convert the following structure to DOT format, it should look like a SCIENTIFIC COMPILER PARSE TREE, Follow these instructions: 1- Make sure it doesn't have any syntax errors and match all DOT restricitions, output will be directly used into graphviz.Source in python. 2- Make sure that each node has only 1 parent. Here's the reperesntation:\n{ai_text}",
                response = model.generate_content(prompt)
                dot_output = ""
                parts = response.candidates[0].content.parts
                for part in parts:
                    dot_output += part.text
                cleaned_dot_output = dot_output.replace("```", "")
                cleaned_dot_output = cleaned_dot_output.replace("DOT" , "")
                cleaned_dot_output = cleaned_dot_output.replace("dot", "")
                cleaned_dot_output = cleaned_dot_output.replace("python", "")

                print(cleaned_dot_output)
                graph = graphviz.Source(cleaned_dot_output)
                graph.render('output_graph', format='png', cleanup=True)
                graph.view()

    else:
        while True:
            text = input("racket >> ")
            if text == "exit":
                break
            tokens = lexer.tokenize_line(text)
            # print("tokens = ", tokens)
            parser = Parser(tokens)
            ast = parser.parse()
            if ast:
                python_code = ast.generate_python_code()
                print(print_parse_tree(ast))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Example usage: python3 -m racket-to-python-translator -rkt code.rkt -ai')
    parser.add_argument('-code', type=str, help='File name that contains racket code "code.rkt" for example', default=None)
    parser.add_argument('-ai', action='store_true', help='Use this arguemnt to activate AI enhancemnet')
    args = parser.parse_args()
    ai = args.ai
    file = args.code
    main(file, ai)
