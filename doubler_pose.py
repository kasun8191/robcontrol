#!/usr/bin/env python
import roslib
import rospy
from geometry_msgs.msg import PoseStamped

rospy.init_node('doubler')

position_current = []

def callback(msg):
	global position_current
	position_current.append(PoseStamped(msg.header, msg.pose))
	if len(position_current)>10:
		pub.publish(position_current[-1])
		position_current = []


	
  	

sub = rospy.Subscriber('/posi', PoseStamped, callback)
pub = rospy.Publisher('/posedata', PoseStamped, queue_size=1)

rospy.spin()


