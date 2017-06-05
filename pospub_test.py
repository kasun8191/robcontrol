#!/usr/bin/env python
import roslib
import rospy
import json
from geometry_msgs.msg import Point
from geometry_msgs.msg import PoseStamped
from time import sleep
from math import floor
from democontroller1 import ExampleCtrl

list1 = []
list2 = []
ctrl = ExampleCtrl()
env_vars = dict()
xsize = 10
ysize = 5

blocklength = 1

xbase = -5
ybase = -2.5

def coord2state(x, y):
   yaxis = abs(int(y - ybase))/blocklength
   xaxis = abs(int(x - xbase))/blocklength
   state = xaxis + (yaxis*xsize)
   return state;

def state2coord(state):
   
   xaxis = state % xsize
   yaxis = floor(int(state) / int(xsize))
   x = xbase + (blocklength/2.) + (xaxis * blocklength )
   x = float(x)
   y = ybase + (blocklength/2.) + (yaxis * blocklength )
   y = float(y)
   return (x,y);


#callback and listener used to receive pose data for initial launch 
#callback and listener used to receive pose data for initial launch 
def callback1(msg):
    global x_obj_1
    global y_obj_1
    position_current = msg.pose.position
    x_obj_1 = position_current.x
    y_obj_1 = position_current.y
    

def listener1():
   
    
    rospy.Subscriber("/object1pos", PoseStamped, callback1)
    
#callback and listener used to receive pose data for initial launch 
def callback2(msg):
    global x_obj_2
    global y_obj_2
    position_current = msg.pose.position
    x_obj_2 = position_current.x
    y_obj_2 = position_current.y
    

def listener2():
   
  
    rospy.Subscriber("/object2pos", PoseStamped, callback2)

def callback(msg):
    global x1
    global y1
    position_current = msg.pose.position    
    x1 = position_current.x
    y1 = position_current.y    
    

def listener():
   
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("/posi", PoseStamped, callback)
    



def setpos(x2,y2,x,y):

    #initialize publisher of pose data
    pub = rospy.Publisher('/setPos', Point, queue_size=10)
    rate = rospy.Rate(5) # 10hz

    inc = .065
    incx = inc
    incy = inc
    #calculate index for for loop
    i = abs(x-x2)
    j = abs(y-y2)
    n = int(i/inc)
    m = int(j/inc)

    z = .5


    if m>n:
        n = m
        incx = incx*(i/j)
        incy = inc
    elif n>m:
        incx = inc
        incy = incy*(j/i)
    else:
        incx = inc
        incy = inc


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

            position = Point(x2,y2,z)
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

            position = Point(x2,y2,z)
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

            position = Point(x2,y2,z)
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

            position = Point(x2,y2,z)
            pub.publish(position)
            rate.sleep()


if __name__ == '__main__':
    
    listener()
    listener1()
    listener2()
    sleep(1)
    while (0<1):
        try:

            current_state_obj1 = coord2state(x_obj_1,y_obj_1)
            current_state_obj1 = current_state_obj1 - 20
            current_state_obj2 = coord2state(x_obj_2,y_obj_2)
            current_state_obj2 = current_state_obj2 - 30
            env_vars['env2'] = current_state_obj1
            env_vars['env3'] = current_state_obj2
            list1.append(env_vars.copy())
            print(env_vars)
            json.dump(list1, open("/home/siddarthkaki/new_ws/src/robcontrol/src/log.txt",'w'))
            state = ctrl.move(**env_vars)
            copy = state.copy()
            copy['env2'] = env_vars['env2']
            copy['env3'] = env_vars['env3']
            list2.append(copy)
            json.dump(list2, open("/home/siddarthkaki/new_ws/src/robcontrol/src/log2.txt",'w'))
            new_state = state2coord(state['loc'])
            setpos(x1,y1,new_state[0],new_state[1])
        except rospy.ROSInterruptException:
            pass
