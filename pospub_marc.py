#!/usr/bin/env python
import roslib
import rospy
import struct
import string
import numpy as np
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import PoseStamped
from math import floor
from std_msgs.msg import Float32
from std_msgs.msg import String
from math import atan2
from math import sqrt
from math import sin
from math import cos
from math import pi
from math import asin
from time import sleep
from openbci.msg import BCIuVolts

xsize = 10
ysize = 10

blocklength = 1

xbase = -5
ybase = -5

rospy.init_node('quad_ls', anonymous=True)
pub2 = rospy.Publisher('/setyaw', Quaternion, queue_size=10)
pub3 = rospy.Publisher('/gyrodata',BCIuVolts, queue_size=1)
pub4 = rospy.Publisher('/posi_wall',BCIuVolts, queue_size=1)
gyro = []
stamp = rospy.get_rostime()

##############################################################################

#laser scanner data
def callback2(data):
    global gyro
    for i in range(int(len(data.data)/4)):
        gyro.append(struct.unpack('<f',data.data[4*i:4*(i+1)])[0])
        pub3.publish(stamp,gyro)


def listener2():
    rospy.Subscriber("/gyro", String, callback2)

#converts laser scanner data to distance and angle
def convtocoord():
    global d
    global angle
    global list2
    a = 0
    b = 1
    c = 2
    count = 0
    while a<2051 and b<2051 and c<2051:
        xl = gyro[a]
        yl = gyro[b]
        zl = gyro[c]
        distance = sqrt(xl**2+yl**2)
        angle_angle = atan2(yl,xl)

        if distance != 0:
            count = count+1
            d = distance
            angle = angle_angle
            print('d:', d)
            print ('angle:', angle)
            if count == 1:
                list2 = np.array([[xl],[yl],[zl]])
            else:
                list1 = np.array([[xl],[yl],[zl]])
                list2 = np.hstack((list2,list1))

                

        a = a+3
        b = b+3
        c = c+3
        

###############################################################################


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

###############################################################################

#callback and listener used to receive pose data for initial launch - quad pose
def callback(msg):
    global x1
    global y1
    global z
    position_current = msg.pose.position
    orientation_current = msg.pose.orientation
    x1 = position_current.x
    y1 = position_current.y    
    z = (asin(orientation_current.z))*2    

def listener():
   rospy.Subscriber("/posi", PoseStamped, callback)

###############################################################################

#laser scanner pose
def callback3(msg):
    
    global x3
    global y3
    global z3
    global qx
    global qy
    global qz
    global qw
    position_current = msg.pose.position
    orientation_current = msg.pose.orientation
    x3 = position_current.x
    y3 = position_current.y
    z3 = position_current.z    
    qx = orientation_current.x
    qy = orientation_current.y
    qz = orientation_current.z
    qw = orientation_current.w
    
    

def listener3():
    rospy.Subscriber("/posi2", PoseStamped, callback3)    

def setyaw(z1,yaw):
    
    yaw = yaw*(pi/180)
    if z1<yaw:
        while z1 < yaw:
            z1 = z1+.05
            sleep(.5)
            orientation = Quaternion(0,0,sin(z1/2),cos(z1/2))
            pub2.publish(orientation)
            print z1
    elif z1>yaw:
        while z1 > yaw:
            z1 = z1-.05
            sleep(.5)
            orientation = Quaternion(0,0,sin(z1/2),cos(z1/2))
            pub2.publish(orientation)
            print z1

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
            pub.publish(position)
            rate.sleep()

if __name__ == '__main__':
    
    
    listener()
    listener2()
    listener3()
    sleep(1)
    convtocoord()
    num = list2.shape[1]
    lscan_posi = np.tile(np.array([[x3,y3,z3]]).transpose(), (1, num))
    rotation = np.matrix([[1-2*qy**2-2*qz**2,2*qx*qy-2*qz*qw,2*qx*qz+2*qy*qw],[2*qx*qy+2*qz*qw,1-2*qx**2-2*qz**2,2*qy*qz-2*qx*qw],[2*qx*qz-2*qy*qw,2*qy*qz+2*qx*qw,1-2*qx**2-2*qy**2]])
    posi_wall = np.dot(rotation,list2)
    posi_wall = lscan_posi+posi_wall
    posi_wall = posi_wall.tolist()
    pub4.publish(stamp,posi_wall)
    
    while (0<1):
        try:

            data = 0
            
            #yaw = int(input("Please enter the state ID [1-24]: "))
            #setyaw(z,yaw)

        except rospy.ROSInterruptException:
            pass
