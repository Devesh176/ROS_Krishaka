#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion, Twist
import tf
import math
import numpy as np




def cmd_vel_publisher():
    rospy.init_node('cmd_vel_publisher_node', anonymous=True)
    #rate = rospy.Rate(10)  # 10 Hz

    cmd_vel_topic = '/cmd_vel'
    cmd_vel_pub = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

   

    while not rospy.is_shutdown():
        # Create a Twist message to control the robot's velocity
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = 0.00  # linear velocity along the x-axis (forward)
        cmd_vel_msg.angular.z = 0.0  # angular velocity around the z-axis (no rotation)

        # Publish the Twist message
        

        #quaternion = (
        #msg.pose.pose.orientation.x,
        #msg.pose.pose.orientation.y,
        #msg.pose.pose.orientation.z,
        #msg.pose.pose.orientation.w)
        #euler = tf.transformations.euler_from_quaternion(quaternion)
        #yaw_angle = euler[2]
        #Convert quaternion to Euler angles (roll, pitch, yaw)
        #euler = tf.transformations.euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
        #roll, pitch, yaw = euler
        
        #angle = math.degrees(yaw)

        
        #rospy.loginfo("The angle of robot is: " + angle )

        cmd_vel_pub.publish(cmd_vel_msg)

        # Sleep to maintain the specified rate
        rospy.spin()

if __name__ == '__main__':
    try:
        

      if __name__ == '__main__':
       rospy.init_node("draw_circle")
       rospy.loginfo("Node has been started")

      pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

      rate = rospy.Rate(2)

      while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 0.5
        msg.angular.z = 0.0
        pub.publish(msg)
        rate.sleep()
        
    except rospy.ROSInterruptException:
        pass
