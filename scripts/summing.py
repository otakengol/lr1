#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Int16MultiArray
rospy.init_node('summing')
def callback(msg):
  array = msg.data
  rospy.loginfo('Sum1 %s', array)
  sumel = sum(array)
  sum_msg = Int16()
  sum_msg.data = sumel
  rospy.loginfo('Sum2 %s', sum_msg.data)
  pub.publish(sum_msg)  
pub = rospy.Publisher('summingreq', Int16, queue_size=10)
rospy.Subscriber('polynomialsum', Int16MultiArray, callback, queue_size=10)
rospy.spin()
