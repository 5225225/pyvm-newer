import sys
import json

import cmdio
from cmdio import Command

def jb(p1,p2):
    p1 = int(p1)
    p2 = int(p2)
    count = 0
    count = count + p1 * 256
    count = count + p2
    return count
    
def splitbytes(x):
    x = int(x)
    p1 = x // 256
    p2 = x - (p1*256)
    return(p1,p2)
    
def listin(list,check):
    for item in list:
        if check in item:
            return True
    return False

opcodes = {
"SET":4,
"JUMP":5,
"JUMPL":5,
"IFE":6,
"ADD":7,
"SUB":8,
}

commands = []

with sys.stdin as f:
    for item in cmdio.jsondecode(f.read()):
        commands.append(item)



output = []

def out(*arg):
    global output
    for item in arg:
        try:
            if type(item) == type(()): #Seeing if type of item is a tuple, the types.TupleType doesn't exist in python3
                for x in item:
                    output.append(x)
            elif type(item) == type(0):
                output.append(item)
            elif type(item) == type("str"):
                output.append(int(item))
        except TypeError:
            output.append(item) #Item was not a tuple, don't bother trying to unpack it.
for cmd in commands:
    out(opcodes[cmd.opcode])
    if False: pass
    elif cmd.opcode == "SET": #FORMAT: SET *x y
        out(splitbytes(cmd.arguments[0]))
        out(cmd.arguments[1])
    elif cmd.opcode == "JUMP":  or (EXTRA and item[0] == "JUMPL"):#FORMAT: JUMP *x
        if cmd.opcode == "JUMP":
            out(splitbytes(cmd.arguments[0]))
            
    elif cmd.opcode == "IFE": # or (EXTRA and item[0] == "IFEL"):#FORMAT: IFE *x *y *z
        out(splitbytes(cmd.arguments[0]))
        out(splitbytes(cmd.arguments[1]))
        out(splitbytes(cmd.arguments[2]))
        
    elif cmd.opcode == "ADD" or cmd.opcode == "SUB" :#FORMAT: ADD/SUB *x *y
        out(splitbytes(cmd.arguments[0]))
        out(splitbytes(cmd.arguments[1]))
        
strout = []
for item in output:
    strout.append(str(item))
print(json.dumps(strout))