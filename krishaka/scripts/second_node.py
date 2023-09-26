#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion

def odom_callback(msg):
    position = msg.pose.pose.position
    
    rospy.loginfo("Robot Position: x = {:.2f}, y = {:.2f}, z = {:.2f}".format(position.x, position.y, position.z))
    print(position.x, position.y)

def position_publisher():
    rospy.init_node('position_publisher_node', anonymous=True)
    rospy.Subscriber('/odom', Odometry, odom_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        position_publisher()
    except rospy.ROSInterruptException:
        pass
