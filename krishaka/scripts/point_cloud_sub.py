#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2

def point_cloud_callback(msg):
    rospy.loginfo("Received a point cloud message.")

    # Extract point cloud data from the message
    pc_data = pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True)

    # Process and print the first few points
    num_points_to_print = 10
    for i, point in enumerate(pc_data):
        if i >= num_points_to_print:
            break
        x, y, z = point
        rospy.loginfo("Point %d: x=%.3f, y=%.3f, z=%.3f", i, x, y, z)

def main():
    rospy.init_node("point_cloud_subscriber_node")

    # Subscribe to the point cloud topic
    rospy.Subscriber("/depth_camera/depth/points", PointCloud2, point_cloud_callback)

    # Spin the node to receive messages
    rospy.spin()

if __name__ == "__main__":
    main()
