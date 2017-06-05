#!/usr/bin/env python
import rospy


xsize = 5
ysize = 5

blocklength = 1

xbase = -2.5
ybase = -2.5

x = float(input("Please enter an x-coordinate between -2.5 and 2.5: "))
y = float(input("Please enter an y-coordinate between -2.5 and 2.5: "))


def coord2state(x, y):
   yaxis = abs(int(x - xbase))/blocklength
   xaxis = abs(int(y - ybase))/blocklength
   state = xaxis + (yaxis*xsize)
   print(state);

coord2state(x, y)
