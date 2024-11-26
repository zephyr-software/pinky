import sys
from utils import *
from tokens import *
from lexer import *
from parser import *
from interpreter import *

if __name__ == '__main__':
  if len(sys.argv) != 2:
    raise SystemExit('Usage: python3 pinky.py <filename>')
  filename = sys.argv[1]

  with open(filename) as file:
    source = file.read()

    print(f'{Colors.MAGENTA}***************************************{Colors.WHITE}')
    print(f'{Colors.MAGENTA}SOURCE:{Colors.WHITE}')
    print(f'{Colors.MAGENTA}***************************************{Colors.WHITE}')
    print(source)

    print(f'{Colors.MAGENTA}***************************************{Colors.WHITE}')
    print(f'{Colors.MAGENTA}TOKENS:{Colors.WHITE}')
    print(f'{Colors.MAGENTA}***************************************{Colors.WHITE}')
    tokens = Lexer(source).tokenize()
    for tok in tokens: print(tok)

    print()
    print(f'{Colors.MAGENTA}***************************************{Colors.WHITE}')
    print(f'{Colors.MAGENTA}AST:{Colors.WHITE}')
    print(f'{Colors.MAGENTA}***************************************{Colors.WHITE}')
    ast = Parser(tokens).parse()
    print_pretty_ast(ast)

    print()
    print(f'{Colors.MAGENTA}***************************************{Colors.WHITE}')
    print(f'{Colors.MAGENTA}INTERPRETER:{Colors.WHITE}')
    print(f'{Colors.MAGENTA}***************************************{Colors.WHITE}')
    interpreter = Interpreter()
    val = interpreter.interpret(ast)
    print(val)
