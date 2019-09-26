#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def msg_callback(message):
    global velocity
    velocity = message.data


rospy.init_node('movement_controller')
pos = 0
pub = rospy.Publisher('current_position', Float64, queue_size=10)
rospy.Subscriber("velocity_command", Float64, msg_callback)
rate = rospy.Rate(1)
velocity = 0

while not rospy.is_shutdown():
    pub.publish(pos)
    pos += velocity
    rate.sleep()

rospy.spin()

