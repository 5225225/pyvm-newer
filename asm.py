import sys

EXTRA = True

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
def varreplace(varx,commands):
    new = []
    for cmd in commands:
        new.append([])
        for item in cmd:
            if item in varx:
                new[-1].append(varx[item])
            else:
                new[-1].append(item)
    return new 
opcodes = {
"SET":4,
"JUMP":5,
"JUMPL":5,
"IFE":6,
"ADD":7,
"SUB":8,
}

var = {}

commands = []
file = open(sys.argv[1])
for line in file.read().split("\n"):
    commands.append(line.split(" "))
output = []

for item in commands:
    if item[0] == "var":
        var[item[1]] = item[2]

for item in commands:
    if item[0].startswith("#"):
        commands.remove(item)
while listin(commands,"var"):
    for item in commands:
        if item[0] == "var":
            commands.remove(item)
commands = varreplace(var,commands)
if EXTRA:
    global jumpcalc
    jumpcalc = []
for item in commands:
    curritem = []
    try:
        curritem.append(opcodes[item[0]])
    except KeyError:
        curritem.append(item[0])
    if False: pass
    elif item[0] == "SET": #FORMAT: SET *x y
        high,low = splitbytes(item[1])
        curritem.append(high)
        curritem.append(low)#Memory address
        curritem.append(item[2])#Value
    elif item[0] == "JUMP" or (EXTRA and item[0] == "JUMPL"):#FORMAT: JUMP *x
        if item[0] == "JUMP":
            high,low = splitbytes(item[1])
            curritem.append(high)
            curritem.append(low)
        if item[0] == "JUMPL":
            high,low = splitbytes(item[1])
            curritem.append("*" + str(high))
            curritem.append(str(low))
    elif item[0] == "IFE" or (EXTRA and item[0] == "IFEL"):#FORMAT: IFE *x == *y *z
        highnum1,lownum1 = splitbytes(item[1])
        curritem.append(highnum1)
        curritem.append(lownum1)
        
        highnum2,lownum2 = splitbytes(item[2])
        curritem.append(highnum2)
        curritem.append(lownum2)
        if item[0] == "IFE":
            highjump,lowjump = splitbytes(item[3])
            curritem.append(highjump)
            curritem.append(lowjump)
        elif item[0] == "IFEL":
            high,low = splitbytes(item[3])
            curritem.append("*" + str(high))
            curritem.append(str(low))
    elif item[0] == "ADD" or item[0] == "SUB" :#FORMAT: ADD/SUB *x *y
        high1,low1 = splitbytes(item[1])
        curritem.append(high1)
        curritem.append(low1)
        
        high2,low2 = splitbytes(item[2])
        curritem.append(high2)
        curritem.append(low2)
    if EXTRA:
        if len(jumpcalc) > 0:
            jumpcalc.append(len(curritem) + jumpcalc[-1])
        else:
            jumpcalc.append(len(curritem))
    for item in curritem:
        output.append(str(item))
if EXTRA:
    highjump = 0
    lowjump = 0
    for index,item in enumerate(output):
        sw = False
        try:
            sw = item.startswith("*")
        except AttributeError:
            pass #Item is most likely an int, ignore it.
        if sw:
            highjump = item[1:]
            lowjump = int(output[index + 1]) + 1
            memhigh,memlow = splitbytes(jumpcalc[jb(highjump,lowjump) - 1])
            output[index] = memhigh
            output[index + 1] = memlow
                    
strout = []
for item in output:
    strout.append(str(item))
print(",".join(strout))