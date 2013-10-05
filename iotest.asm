#Set up needed constants
SET 2001 1
SET 2002 58 #Ascii for ":"

#Set up variables
SET 3000 0 #Where to GCHR, high byte
SET 3001 150 #Where to GCHR, low byte

SET !23+1 0 #Reset the address of GCHR
SET !23+2 0

SET !25+1 0 #Reset the ifel
SET !25+2 0

ADD !23+1 3000 #Copy high byte into gchr
ADD !23+2 3001 #Copy low byte into gchr

ADD !25+1 3000 #Copy high/low into ifel
ADD !25+2 3001



GCHR 66 #Kinda obvious what it does, 66 is a placeholder.

IFEL 66 2002 37 #66 is a placeholder, will be overwritten

ADD 3001 2001 #Increment where to GCHR by 1
#There isn't any range checking (yet) so it will work
#Later on when I add it, I'll need to implement a way to check for an over/under flow 
#so you can correct it manually


ADD 6 2001
JUMPL 9
#This is where it jumps to if its a :
#As of right now, it does nothing but let the counter go free
SET 6666 0 #Really need to get around to implementing a NOOP


SET 3000 0
SET 3001 150 #Reset the gchr.

SET !56+1 0
SET !56+2 0

SET !58+1 0
SET !58+2 0


ADD !56+1 3000
ADD !56+2 3001

ADD !58+1 3000
ADD !58+2 3001

PCHR 0

IFEL 0 2002 63

ADD 3001 2001
JUMPL 43

SET 6666 0