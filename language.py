from lexer import *
from parser import *
import sys

def main():
    print("MY FIRST COMPILER")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs a source file as argument")
    with open(sys.argv[1], "r") as inputFile:
        source = inputFile.read()

    lexer = Lexer(source)
    parser = Parser(lexer)

    parser.program()
    print("Parsing Completed")

main()
