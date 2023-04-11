#!/usr/bin/env python3
import rospy
import tf
import math
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose
rospy.init_node('turtle')
turtlename = rospy.get_param('~turtle')
def handle_turtle_pose(msg):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),quaternion_from_euler(0, 0, msg.theta),rospy.Time.now(),turtlename,"world")
    orb=rospy.Time.now().to_sec() * math.pi
    xc=0.5*math.cos(orb)
    yc=0.5*math.sin(orb)    
    br.sendTransform((xc, yc, 0), quaternion_from_euler(0, 0, orb), rospy.Time.now(), "carrot", 
    turtlename)
rospy.Subscriber('input_pose',Pose,handle_turtle_pose)
rospy.spin()
