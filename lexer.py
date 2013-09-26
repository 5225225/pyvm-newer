#This is meant to strip out every comment and parse stdin into a list of Commands, put it into json, and print it to stdout.
#Memory addresses are unchanged, and once support for variables are added,
#They will be either declared at the top of the list, or put into a seperate list.

import json
import sys

import cmdio

infile = sys.stdin.read().split("\n")


class Command:
    def __init__(self, line, opcode, arguments):
        self.line = line
        self.opcode = opcode
        self.arguments = arguments
    
commands = []

for index,item in enumerate(infile, start=1):
    line = index
    opcode = item.split(" ")[0]
    arguments = item.split(" ")[1:]
    cmd = Command(line,opcode,arguments)
    commands.append(cmd)


sys.stdout.write(cmdio.jsonencode(commands))