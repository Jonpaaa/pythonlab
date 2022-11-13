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

engine = 2
mdaVsDa = 2
while (engine != 1 or engine !=0):
    engdecision = (input ("Single or Multi? [s/M]"))
    engdecision = engdecision.lower()
    if engdecision == ("s"):
        engine = 0
        break
    elif engdecision ==("M"):
        engine = 1
        break


if (engine == 0):
    toMin = 800
    print (colored(">800M", "green"))
    toActual = int(input("DEP VIZ? : "))
    toAlt = 0
    
    if (toMin > toActual):
        print(colored("Warning, DEP ALT < 20 min", 'yellow'))
        toAlt = int(input("DEP ALT? (Min): "))
        if (toAlt > 20): 
            print("WARNING, DO NOT PROCEED TILL FURTHER NOTICE.")
    if (toMin < toActual) and (toAlt < 20):
        destMin = int(input(colored("Consult AIP, DEST MIN? (ft): ", 'yellow')))
        while (mdaVsDa != 1 or mdaVsDa !=0):
            mdaDadecision = (input ("DA or MDA?: "))
            mdaDadecision = mdaDadecision.lower()
            if mdaDadecision == ("da"):
                mdaVsDa = 0
                print (colored("WARNING: Check equipment serviceability and pilot qualifications for CAT of APP", "yellow"))
                break
            elif mdaDadecision ==("mda"):
                mdaVsDa = 1
                print (colored("WARNING: Check equipment serviceability and pilot qualifications.", "yellow"))
                print (colored("WARNING: DO NOT BREACH MINIMA!", "red"))
                break  
    if (mdaVsDa == 0):
        destAct = int(input("DEST DA? :"))
    else:
        destAct = int(input("DEST MDA? :"))
    if (destAct > destMin):
        print (colored("Proceed with checkout, preflight and briefings", "green"))
    else:
        print("WARNING")



