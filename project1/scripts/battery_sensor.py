#!/usr/bin/env python
from std_msgs.msg import Float64
import rospy

def cpos_callback(pos):
    global cpos
    cpos = pos.data

rospy.init_node('battery_sensor')
pub = rospy.Publisher('battery_voltage', Float64, queue_size=10)
rospy.Subscriber("current_position", Float64, cpos_callback)
bat_volt = 68
max_charge = 68
cpos = 0

while not rospy.is_shutdown():
    if cpos < 6 and bat_volt < max_charge:
        pub.publish(bat_volt)
        bat_volt += 1
    elif bat_volt > 0:
        pub.publish(bat_volt)
        bat_volt -= 1
    else:
        pub.publish(bat_volt)
    rospy.sleep(1.)

#while(bat_volt != 0):
 #   pub.publish(bat_volt)
  #  bat_volt -= 1
   # rospy.sleep(1.)

#while not rospy.is_shutdown():
 #   pub.publish(bat_volt)
rospy.spin()

