#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray
rospy.init_node('request')
pub = rospy.Publisher('requestpol', Int16MultiArray, queue_size=10)
rate = rospy.Rate(1)

def callback(msg):
  rospy.loginfo('Sum1 %s', msg.data)
  rospy.Subscriber('summingreq' , Int8, callback, queue_size=10)
def Req():
  poly_msg = Int16MultiArray()
  var = [2, 4, 5]
  while not rospy.is_shutdown():
   poly_msg.data = var
   rospy.loginfo('Req2 %s', poly_msg.data)
   pub.publish(poly_msg)
   rate.sleep()
try:
  Req()
except (rospy.ROSInterruptException, KeyboardInterrupt):
  rospy.logerr('Exception catched')
