import json
import sys

import cmdio
from cmdio import Command


def decomment(commands):
    output = []
    for item in commands:
        if item == "":
            output.append("#")
        elif item.startswith("#"):
            output.append("#")  # Magic value, read on line 30
        elif "#" in item:
            output.append(item[:item.find("#")])
        else:
            output.append(item)
    return output

if len(sys.argv) == 2:
    infile = decomment(open(
        sys.argv[1]).read().strip().split("\n"))
else:
    infile = decomment(
        sys.stdin.read().strip().split("\n"))

commands = []


for index, item in enumerate(infile, start=1):
    line = index
    if not item == "#":
        opcode = item.split(" ")[0]
        arguments = item.split(" ")[1:]
        while "" in arguments:
            arguments.remove("")
        intargs = []
        for item in arguments:
            if item.startswith("$"):  # Convert hex values to decimal
                intargs.append(int(item[1:], 16))
            elif item.startswith("%"):
                intargs.append(int(item[1:], 2))  # Convert binary to decimal
            elif item.startswith("0"):
                try:
                    intargs.append(int(item[1:], 8))  # Convert oct to decimal
                except ValueError:
                    if item == "0":
                        intargs.append(0)
                    else:
                        raise
                        # The above code was to handle the case where a 0
                        # was being treated like a base specifier.
            else:
                try:
                    intargs.append(int(item))
                except ValueError:
                    intargs.append(item)
        cmd = Command(line, opcode, intargs)
        commands.append(cmd)


sys.stdout.write(cmdio.jsonencode(commands))
