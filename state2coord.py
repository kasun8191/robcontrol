#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from math import floor



xsize = 5
ysize = 5
position = [0,0,0]

blocklength = 1

xbase = -2.5
ybase = -2.5

state = int(input("Please enter the state ID [1-24]: "))

def state2coord(state):
   xaxis = state % xsize
   yaxis = floor(int(state) / int(xsize))
   x = xbase + (blocklength/2.) + (xaxis * blocklength )
   x = float(x)
   y = ybase + (blocklength/2.) + (yaxis * blocklength )
   y = float(y)
   return (x,y);

