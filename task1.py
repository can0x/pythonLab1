from sys import argv
# The sys module provides access to some variables and
# functions that interact strongly the interpreter

from sys import argv
if name == 'main':
    if len(argv) != 4 or not argv[1].isdigit() or argv[2] not in '+-*/' or not argv[3].isdigit():
        print('Please enter arguments properly: operand operator operand')
    else:
        try:
            print('Result: ', eval(argv[1] + argv[2] + argv[3]))
        except ZeroDivisionError:
            print("Division by zero")