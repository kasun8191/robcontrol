#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point32

def callback(msg):
   print msg.data

rospy.init_node('listener', anonymous=True)

sub = rospy.Subscriber("/dist", Point32,callback)

rospy.spin()
   


