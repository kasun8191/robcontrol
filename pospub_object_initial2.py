#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import Point
from geometry_msgs.msg import PoseStamped
from time import sleep
from math import floor
from std_msgs.msg import Float64

xsize = 5
ysize = 5

blocklength = 1

xbase = -2.5
ybase = -2.5

rospy.init_node('listener1', anonymous=True)
pub1 = rospy.Publisher('/setPosobject1', Float64, queue_size=10)
rate = rospy.Rate(5) 

pub2 = rospy.Publisher('/setPosobject2', Float64, queue_size=10)
rate = rospy.Rate(5) 

def state2coord(state):
   
   xaxis = state % xsize
   yaxis = floor(int(state) / int(xsize))
   x = xbase + (blocklength/2.) + (xaxis * blocklength )
   x = float(x)
   y = ybase + (blocklength/2.) + (yaxis * blocklength )
   y = float(y)
   return (x,y);



#callback and listener used to receive pose data for initial launch 
def callback1(msg):
    global x1
    global y1
    position_current = msg.pose.position
    x1 = position_current.x
    y1 = position_current.y    
    

def listener1():
    
    rospy.Subscriber("/object1pos", PoseStamped, callback1)
    
#callback and listener used to receive pose data for initial launch 
def callback2(msg):
    global x3
    global y3
    position_current = msg.pose.position
    x3 = position_current.x
    y3 = position_current.y    
    

def listener2():
   
    rospy.Subscriber("/object2pos", PoseStamped, callback2)
    



def setvel(x2,x,obj):

    #x is desired position
    #x2 is current position

    #condition 1
    if x>x2:
        
        vel = 1

        if obj == 1:
            rospy.loginfo(vel)
            pub1.publish(vel)
            rate.sleep()
        elif obj == 2:
            rospy.loginfo(vel)
            pub2.publish(vel)
            rate.sleep()

    #condition 2
    elif x<x2:
       
        vel = -1

        if obj == 1:
            rospy.loginfo(vel)
            pub1.publish(vel)
            rate.sleep()
        elif obj == 2:
            rospy.loginfo(vel)
            pub2.publish(vel)
            rate.sleep()
    else:
        
        vel = 0
        
        if obj == 1:
            rospy.loginfo(vel)
            pub1.publish(vel)
            rate.sleep()
        elif obj == 2:
            rospy.loginfo(vel)
            pub2.publish(vel)
            rate.sleep()
   


if __name__ == '__main__':
    
    listener1()
    sleep(1)
   # listener2()

    
    state1 = [10, 11, 12, 13, 14, 13, 12, 11, 10]
    #state2 = [19, 18, 17, 16, 15, 16, 17, 18, 19]
    
    #while (0<1):
    try:
        for i in range (0,9):
            

            x_old = x1
            state_1 = state1[i]
            new_state = state2coord(state_1)
            print(x_old)
            print(state_1)
            setvel(x_old,new_state[0],1)
                

               # state_2 = state2[i]
               # state2coord(state_2)
               # setvel(x3,x,2)
           
    except rospy.ROSInterruptException:
        pass
