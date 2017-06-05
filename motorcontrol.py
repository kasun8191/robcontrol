#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32
from math import atan2
from math import pi

rospy.init_node('talker',anonymous=True)

def setpos(x1,y1):
    
    pub = rospy.Publisher('counter', Float32, queue_size=10)
    pub2 = rospy.Publisher('counter2', Float32, queue_size=10)
    rate = rospy.Rate(1)

    x = float(input('Please enter an x-coordinate: '))
    y = float(input('Please enter a y-coordinate: '))

    
    n = int(abs(x-x1)/.05)
    m = int(abs(y-y1)/.05)
    
    if m>n:
        n = m
    
    #condition 1
    if x>=x1 and y>=y1:
        theta = atan2(abs((y-y1)),abs((x-x1)))*(180/pi)

if __name__ == '__main__':
    try:
        setpos(0,0)
    except rospy.ROSInterruptException:
        pass
