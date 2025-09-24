from lexer import *
from parser import *
from emitter import *
import sys

def main():
    print("MY FIRST COMPILER")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs a source file as argument")
    with open(sys.argv[1], "r") as inputFile:
        source = inputFile.read()

    lexer = Lexer(source)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program()
    emitter.writeFile()
    print("Compiling Completed")

main()
