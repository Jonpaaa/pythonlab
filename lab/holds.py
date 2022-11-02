from termcolor import *

track = int (input("TRK: "))

track = ((track + 180) % 360)

radial = int (input("Radial: "))

toFlag = ((radial + 180) % 360)


direction = 2
while (direction != 1 or direction !=0):
    dirdecision = (input ("Standard Pattern? [Y/n]"))
    dirdecision = dirdecision.lower()
    if dirdecision == ("y"):
        direction = 1
        break
    elif dirdecision ==("n"):
        direction = 0
        break


if direction == 1:
    directToTeardrop = ((radial + 110) % 360)

    directToParallel = ((radial - 70) % 360)

    parallelToTeardrop = ((radial + 180) % 360)

    radConvert = ((radial - 180)  % 360)

    trackConvert = ((track - radConvert) % 360)

    print (colored ("⬆ TO STN: ", 'green')), print (colored (toFlag, 'green'))
    
    
    if (trackConvert > 110 and trackConvert < 290):
        print (colored("Direct", 'green'))
    elif (trackConvert > 290 and trackConvert < 359):
        print(colored("Teardrop", 'red'))
    elif (trackConvert < 110):
        print(colored("Parallel", 'blue'))

    print ("Transition zones")

    print (colored("3 ⮕ 1   Direct - Parallel", 'green')), print (colored(directToParallel, 'green'))

    print (colored("3 ⮕ 2   Direct - Teardrop", 'blue')), print (colored(directToTeardrop, 'blue'))

    print (colored("1 ⮕ 2   parallel - Teardrop", 'red')), print (colored(parallelToTeardrop, 'red'))

else:
    
    directToTeardrop = ((radial - 110) % 360)

    directToParallel = ((radial + 70) % 360)

    parallelToTeardrop = ((radial + 180) % 360)

    radConvert = ((radial - 180)  % 360)

    trackConvert = ((track - radConvert) % 360)

    print (colored ("⬆ TO STN: ", 'green')), print (colored (toFlag, 'green'))


    if (trackConvert > 70 and trackConvert < 250):
        print (colored("Direct", 'green'))
    elif (trackConvert > 250 and trackConvert < 359 or trackConvert == 0):
        print(colored("Parallel", 'blue'))
    elif (trackConvert < 70):
        print(colored("Teardrop", 'red'))


    print ("Transition zones")

    print (colored("3 ⮕ 1   Direct - Parallel", 'green')), print (colored(directToParallel, 'green'))

    print (colored("3 ⮕ 2   Direct - Teardrop", 'blue')), print (colored(directToTeardrop, 'blue'))

    print (colored("1 ⮕ 2   parallel - Teardrop", 'red')), print (colored(parallelToTeardrop, 'red'))   

    
