#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def volt_callback(message):
    global bvolt
    bvolt = message.data

def pos_callback(posit):
    global tpos
    tpos = posit.data

def cpos_callback(currpos):
    global cpos
    cpos = currpos.data

rospy.init_node('behavior_coordinator')
bvolt = 0
tpos = 0
cpos = 0
kP = .5
error = 0
velo = 0
home = 0
rate = rospy.Rate(1)

rospy.Subscriber("target_position", Float64, pos_callback)
rospy.Subscriber("battery_voltage", Float64, volt_callback)
rospy.Subscriber("current_position", Float64, cpos_callback)
pub = rospy.Publisher('velocity_command', Float64, queue_size=10)

while not rospy.is_shutdown():
#    if bvolt < 24 and (cpos > 0 or cpos <= 0):
 #       error = (0 - cpos) - error
  #      velo = kP * error
   #     if velo > 6 or velo < -6:
    #        velo = -6
     #   pub.publish(velo)
   # elif bvolt < 24 and cpos <= 0:
   #     pub.publish(0)
   if bvolt < 24:
        while bvolt < 58:
            error = (home - cpos)
            velo = kP * error
            if velo > 6 or velo < -6:
                velo = -6
            pub.publish(velo)

   else:
        error = (tpos - cpos)  #first iteration should be target_position - current_position(0) 
        velo = kP * error
        if velo > 6:
            velo = 6
        pub.publish(velo)
   rate.sleep()

rospy.spin()
