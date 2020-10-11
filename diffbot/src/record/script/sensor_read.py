#! /usr/bin/env python

"""
script to read rosbag data
"""
"""
sources:
http://library.isr.ist.utl.pt/docs/roswiki/rosbag(2f)Code(20)API.html
https://www.fer.unizg.hr/_download/repository/lec08-rosbag-ipython.pdf
"""
import rosbag
from std_msgs import Int32, String

if __name__ =='__main__':
    imu_bag = rosbag.Bag('diffbot_imu.bag')
    odom_bag = rosbag.Bag('diffbot_odom.bag')
    ground_truth_bag = rosbag.Bag('diffbot_ground_truth.bag')

"""
obtain an array of imu sensor data
"""
    imu_x_vel = [msg.linear.x for(topic, msg, t)in imu_bag.read_messages(...)]
    t = [t.to_time()for(topic, msg, t)in imu_bag.read_messages(...)]
"""
obtain an array of odom sensor data
"""
    odom_x_vel = [msg.linear.x for(topic, msg, t)in odom_bag.read_messages(...)]
    t = [t.to_time()for(topic, msg, t)in odom_bag.read_messages(...)]
"""
obtain an array of ground truth data
"""
    ground_truth_x_vel = [msg.linear.x for(topic, msg, t)in ground_truth_bag.read_messages(...)]
    t = [t.to_time()for(topic, msg, t)in ground_truth_bag.read_messages(...)]
