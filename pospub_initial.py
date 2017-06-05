#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import Point
from geometry_msgs.msg import PoseStamped
from time import sleep
from math import floor


xsize = 10
ysize = 10

blocklength = 1

xbase = -5
ybase = -5



def state2coord(state):
   
   global x
   global y
   xaxis = state % xsize
   yaxis = floor(int(state) / int(xsize))
   x = xbase + (blocklength/2.) + (xaxis * blocklength )
   x = float(x)
   y = ybase + (blocklength/2.) + (yaxis * blocklength )
   y = float(y)
   return (x,y);


#callback and listener used to receive pose data for initial launch 
def callback(msg):
    global x1
    global y1
    position_current = msg.pose.position	
    x1 = position_current.x
    y1 = position_current.y    
    

def listener():
   
    	rospy.init_node('listener', anonymous=True)
    	rospy.Subscriber("/posi", PoseStamped, callback)
    	

inc = .1

def setpos(x2,y2,x,y):
	
	#initialize publisher of pose data
	pub = rospy.Publisher('/setPos', Point, queue_size=10)
    	rate = rospy.Rate(5) # 10hz

	incx = .1
	incy = .1
	#calculate index for for loop
	i = abs(x-x2)
	j = abs(y-y2)
	n = int(i/inc)
	m = int(j/inc)

	

	if m>n:
		n = m
		incx = incx*(i/j)
		incy = .1
	elif n>m:
		incx = .1
		incy = incy*(j/i)
	else:
		incx = .1
		incy = .1

	

	#condition 1
	if x>=x2 and y>=y2:
		for i in range(0, n):
			if x>x2:
				x2 = x2+incx
			
			else:
				x2 = x2+0
				
				
			if y>y2:
				y2 = y2+incy
				
			else:
				y2 = y2+0
			
			position = Point(x2,y2,.5)
        		rospy.loginfo(position)
        		pub.publish(position)
        		rate.sleep()			
	
	#condition 2
	elif x>=x2 and y<=y2:
		for i in range(0, n):
			if x>x2:
				x2 = x2+incx
				
			else:
				x2 = x2+0
				
				
			if y<y2:
				y2 = y2-incy
				
			else:
				y2 = y2+0
				
			position = Point(x2,y2,.5)
        		rospy.loginfo(position)
        		pub.publish(position)
        		rate.sleep()			
	
	#condition 3
	elif x<=x2 and y>=y2:
		for i in range(0, n):
			if x<x2:
				x2 = x2-incx
				
			else:
				x2 = x2+0
				
				
			if y>y2:
				y2 = y2+incy
				
			else:
				y2 = y2+0
			
			position = Point(x2,y2,.5)
        		rospy.loginfo(position)
        		pub.publish(position)
        		rate.sleep()		
			
	#condition 4
	elif x<=x2 and y<=y2:
		for i in range(0, n):
			if x<x2:
				x2 = x2-incx
				
			else:
				x2 = x2+0
				
				
			if y<y2:
				y2 = y2-incy
				
			else:
				y2 = y2+0
				
			position = Point(x2,y2,.5)
        		rospy.loginfo(position)
        		pub.publish(position)
        		rate.sleep()	
		

if __name__ == '__main__':
    listener()
    sleep(1)
    while (0<1):
	    try:
	    	state = int(input("Please enter the state ID [1-24]: "))
	    	state2coord(state)
		setpos(x1,y1,x,y)
	    except rospy.ROSInterruptException:
		pass
