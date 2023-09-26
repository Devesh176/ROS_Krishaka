#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped, Point, Quaternion

def publish_pose():
    rospy.init_node('pose_publisher')
    pub = rospy.Publisher('/pose', PoseStamped, queue_size=10)
    rate = rospy.Rate(10)  # Publish at 10 Hz

    while not rospy.is_shutdown():
        pose_msg = PoseStamped()
        pose_msg.header.stamp = rospy.Time.now()
        pose_msg.header.frame_id = 'base_link'  # Change this frame ID if needed
        
        # Set pose information (position and orientation) in pose_msg.pose
        pose_msg.pose.position = Point(x=0.0, y=0.0, z=0.0)  # Set the position values (x, y, z)
        pose_msg.pose.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)  # Set the orientation values (x, y, z, w)
        
        pub.publish(pose_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_pose()
    except rospy.ROSInterruptException:
        pass
