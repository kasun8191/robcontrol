#!/usr/bin/env python
import rospy
import struct
import string
from std_msgs.msg import Float32
from std_msgs.msg import String
from msvcrt import getch
'''

def callback(data):
    gyro=[]
    for i in range(int(len(data.data)/4)):
        gyro.append(struct.unpack('<f',data.data[4*i:4*(i+1)])[0])
    print gyro
   

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/gyro", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

'''
def process(key):
    if key == 'x':
        exit('exitting')
    else:
        print(key)

if __name__ == "__main__":
    while True:
        key = getch()
        process(key)