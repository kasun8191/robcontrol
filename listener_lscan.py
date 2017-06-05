#!/usr/bin/env python
import rospy
import struct
import string
from std_msgs.msg import Float32
from std_msgs.msg import String
from math import atan2
from math import sqrt
from time import sleep


gyro = []

def callback(data):
    global gyro
    for i in range(int(len(data.data)/4)):
        gyro.append(struct.unpack('<f',data.data[4*i:4*(i+1)])[0])


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/gyro", String, callback)


def convtocoord():
    i = 0
    j = 1
    while i<2051 and j<2051:
        d = sqrt((gyro[i])**2+(gyro[j])**2)
        if d != 0:
            print('distance',d)
            print('angle',atan2(gyro[j],gyro[i])*(180/3.14))
        i = i+3
        j = j+3


if __name__ == '__main__':
    
    listener()
    sleep(1)
    convtocoord()
    

