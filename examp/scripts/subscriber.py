#!/usr/bin/env python
import std_msgs.msg
import rospy

rospy.init_node('subsriber')

def msg_callback(message):
    print(message)
rospy.Subscriber('topic', std_msgs.msg.String, msg_callback)
rospy.spin()

