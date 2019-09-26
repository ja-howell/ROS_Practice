#!/usr/bin/env python
import std_msgs.msg
import rospy

rospy.init_node('publisher')
pub = rospy.Publisher('topic', std_msgs.msg.String, queue_size=10)
while True:
    pub.publish("Hello World")
    rospy.sleep
rospy.spin()

print("Hello World")
