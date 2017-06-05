#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import PoseStamped



def callback(msg):
    
    	position_current = msg.pose.position
    	x1 = position_current.x
    	y1 = position_current.y
   	print(x1)
   	print(y1)
  	

def listener():

    	rospy.init_node('listener', anonymous=True)
    	rospy.Subscriber("/posi", PoseStamped, callback)
    	rospy.spin()

if __name__ == '__main__':
    listener()
