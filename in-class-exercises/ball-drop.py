#enter height of tower in meters
#returns amount of time it takes the dropped ball to hit the ground
#ignores air resistance

from math import *
from decimal import *

def drop_ball():
    
    height = input("Please enter the height of the tower in meters: ")

    time = sqrt(2*height/9.8)
    rounded_time = round(time,1)

    return '%s seconds' % (rounded_time)


print drop_ball()
