#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion, Twist
import tf
import math
import numpy as np

targetx, targety = 10.0, 10.0

def odom_callback(msg):
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    position = msg.pose.pose.position
    # orientation = msg.pose.pose.orientation
    
    # Convert quaternion to Euler angles (roll, pitch, yaw)
    #euler = tf.transformations.euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
    #roll, pitch, yaw = euler
    quaternion = (
        msg.pose.pose.orientation.x,
        msg.pose.pose.orientation.y,
        msg.pose.pose.orientation.z,
        msg.pose.pose.orientation.w)
    euler = tf.transformations.euler_from_quaternion(quaternion)
    yaw_angle = euler[2]  # Get the yaw angle (rotation around the vertical axis)

    rospy.loginfo("Robot Yaw Angle (in degrees): {:.2f}".format(math.degrees(yaw_angle)))
    # angle = math.degrees(yaw_angle)

    # vel = Twist()
    # delx = targetx-int(position.x)
    # dely = targety-int(position.y)
    # slope = delx/dely
    
    # while angle != math.atan(slope):
    #     vel.angular = 0.5
    #     pub.publish(vel)

    # while int(position.x) != targetx and int(position.y) != targety :
    #     vel.linear = 1.0
    #     pub.publish(vel)    
    
  
    
    #rospy.loginfo("Robot Position: x = {:.2f}, y = {:.2f}, z = {:.2f}".format(position.x, position.y, position.z))
    #rospy.loginfo("Robot Orientation: roll = {:.2f}, pitch = {:.2f}, yaw = {:.2f}".format(roll, pitch, yaw))
    #print(yaw*180/3.14) 

def position_publisher():
    rospy.init_node('position_publisher_node', anonymous=True)
    
    rospy.Subscriber('/odom', Odometry, odom_callback)
    
    rospy.spin()

if __name__ == '__main__':
    try:
        position_publisher()
    except rospy.ROSInterruptException:
        pass
