import sys

opcodes = {
"SET":4
"JUMP":5
"IFE":6
"ADD":7
"SUB":8
}

commands = []
file = open(sys.argv(1))
for line in file.readline():
    commands.append(line.split(" "))
output = []


for item in commands:
    curritem = []
    curritem.append(opcodes[item[0]])
    if False: pass
    if not(item[0].startswith("#")):
        if item[0] in opcodes:
            item[0] = opcodes[item[0]]
        else:
            print("{} INVALID OPCODE".format(item[0]))

        
