#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import Point
from geometry_msgs.msg import PoseStamped
from time import sleep
from math import floor


xsize = 5
ysize = 5

blocklength = 1

xbase = -2.5
ybase = -2.5

rospy.init_node('listener1', anonymous=True)
pub1 = rospy.Publisher('/setPosobject1', Point, queue_size=10)
rate = rospy.Rate(5) 

pub2 = rospy.Publisher('/setPosobject2', Point, queue_size=10)
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
    position_current = msg.pose.position
    x1 = position_current.x
  
    

def listener1():
   
    
    rospy.Subscriber("/object1pos", PoseStamped, callback1)
    
#callback and listener used to receive pose data for initial launch 
def callback2(msg):
    global x3
    position_current = msg.pose.position
    x3 = position_current.x
    

def listener2():
   
  
    rospy.Subscriber("/object2pos", PoseStamped, callback2)
    

def setpos2obj(x2,x,x6,x4):


  #x2 inital position of object 1 
  #x final position of object 1 
  
  #x6 initial position of object 2 
  #x4 final position of object 2 

  inc = .13
  #calculate index for for loop
  i = abs(x-x2)
  j = abs(x4-x6)
  n = int(i/inc)
  m = int(j/inc)
    
  if m>n:
    n = m




    #condition 1
  if x>=x2 and x4<=x6:
    
    for i in range(0,n):
      
      if x>x2:
        x2 = x2+inc
       
      else:
        x2 = x2+0
      
      position1 = Point(x2,0,0)

      if x4<x6:
        x6 = x6-inc
        
      else:
        x6 = x6-0
      
      position2 = Point(x6,1,0)

      rospy.loginfo(position1)
      pub1.publish(position1)
      rate.sleep()

      rospy.loginfo(position2)
      pub2.publish(position2)
      rate.sleep()

  elif x<=x2 and x4>=x6:
    
    for i in range(0,n):
      
      if x<x2:
        x2 = x2-inc

      else:
        x2 = x2-0

      position1 = Point(x2,0,0)
      
      if x4>x6:
        x6 = x6+inc

      else:
        x6 = x6+0

      position2 = Point(x6,1,0)

      rospy.loginfo(position1)
      pub1.publish(position1)
      rate.sleep()

      rospy.loginfo(position2)
      pub2.publish(position2)
      rate.sleep()

if __name__ == '__main__':
    
    listener1()
    listener2()
    
    sleep(1)
    
    state1 = [10, 11, 12, 13, 14, 13, 12, 11, 10]
    state2 = [19, 18, 17, 16, 15, 16, 17, 18, 19]
    
    while (0<1):
        try:
            for i in range (0,8):

                state_1 = state1[i]
                new_state1 = state2coord(state_1)
                state_2 = state2[i]
                new_state2 = state2coord(state_2)
                setpos2obj(x1,new_state1[0],x3,new_state2[0])
                
           
        except rospy.ROSInterruptException:
            pass
