#This will determine a holds entry sector and subsequent procedure based on:
        # inbound TRK of hold, and current track of the aircraft
        # circuit is left or right

currTrack = int (input("Current TRK: "))


radial = int (input("Radial: "))

adjustTrk = 180 - radial 

currTrack = ((currTrack + adjustTrk) % 360)


#if diffRadTrk in range (70, 179) or diffRadTrk == -180 :
    #print("parallel")
#elif diffRadTrk in range (0, 70) or diffRadTrk in range (-110, 0):
    #print("Direct")
#elif diffRadTrk in range (-110, -180):
    #print("Teardrop")


#print (diffRadTrk)


