from termcolor import *

#AWOPS Flow Chart
#T/O ----------------- T/O ALT
#|
#| 
#|
#ENR
#|
#|
#|
#DEST ---------------- DEST ALT ----- 2nd ALT


#TO
#viz >800m ? --> landing minima? --> Over landing minima --> Takeoff
#under landing minima --> Alternate <20 min? --> Alternate Minima? --> Takeoff

#Dest
# VMC or Other? --> Land
# Above Minima? --> landing minima? --> over landing minima --> 1 alt / under landing minima --> 2 alt
# Alternate Landing Minima(s)? --> Land

def takeoff(toActualViz):
    toMinViz = 800
    toActualViz = int(takeOffActualViz)
    if (toMinViz < toActualViz):
        toMinima = int(input("MIN? "))
        toActual = int(input("ACT? "))
        if (toMinima < toActual):
            to = True         
        elif (toMinima > toActual): 
            timeToAlt = int(input("time?"))
            if (timeToAlt < 20):
                toAltMinima = int(input("MIN? "))
                toAltActual = int(input("ACT? "))
                if (toAltActual > toAltMinima):
                    to = True
                else:
                    to = False
            else:
                to = False
    else:
        to = False   
    return to

#Destination 
def destination(vmcOrOther):   

    if vmcOrOther == "y":
        ld = True
    else:
        destMinima = int(input("D MIN"))
        destActual = int(input("D Act"))    
        if (destMinima < destActual):
            destAltMinima = int(input("D ALT MIN"))
            destAltActual = int(input("D ALT Act")) 
            if (destAltMinima < destAltActual):
                ld = True
            else:
                ld = False
        elif (destMinima > destActual):
            destAltMinima = int(input("D ALT MIN"))
            destAltActual = int(input("D ALT Act")) 
            destAlt2Minima = int(input("D ALT2 MIN"))
            destAlt2Actual = int(input("D ALT2 Act")) 
            if (destAltMinima < destAltActual and destAlt2Minima > destAlt2Actual):
                ld = True
            else:
                ld = False
    return ld

takeOffActualViz = int(input("Viz"))
takeOff = takeoff(takeOffActualViz)

print(takeOff)

if takeOff == True:
    vmcOrOther = (input("VMC Or Other [y/N]"))
    landing = destination(vmcOrOther)
    print (landing)
else:
    print("False")