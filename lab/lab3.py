import numpy as np
import time

force = 6000
mass = 400

acc = (force / mass )
print (acc)

speed = 1
sec = 0
for i in range (100):
    sec = sec + 1
    speed = 1 + (acc * sec) 
    print (speed)
    time.sleep(0.1)