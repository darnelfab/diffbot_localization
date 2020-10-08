#!/usr/bin/env python3


import rospy
import os
from std_msgs.msg import String

class IMU_diffbot:

    def __init__(self):

        # Init node
        rospy.init_node('diffbot_imu', anonymous=False)

        # Get node name
        self.node_name = rospy.get_name()

        # Get ros params
        self.get_ros_params()

        # Internal variables
        self.imu_data_seq_counter = 0
        self.stop_request = False

        # Create topics
        self.pub_imu_data = rospy.Publisher('imu/data', Imu, queue_size=1)


        # Create service
        self.reset_imu_device = rospy.Service('imu/reset_device', Empty, self.callback_reset_imu_device)
        self.calibration_imu_staus = rospy.Service('imu/calibration_status', Trigger, self.callback_calibration_imu_status)


        # Print node status
        rospy.loginfo(self.node_name + " already!")

    def publish_imu_data(self):

        imu_data = Imu()

        quaternion = self.imu.get_quaternion_orientation()
        linear_acceleration = self.imu.get_linear_acceleration()
        gyroscope = self.IMU_diffbot.get_gyroscope()

        imu_data.header.stamp = rospy.Time.now()
        imu_data.header.frame_id = self.frame_id
        imu_data.header.seq = self.imu_data_seq_counter

        imu_data.orientation.w = quaternion[0]
        imu_data.orientation.x = quaternion[1]
        imu_data.orientation.y = quaternion[2]
        imu_data.orientation.z = quaternion[3]

        imu_data.linear_acceleration.x = linear_acceleration[0]
        imu_data.linear_acceleration.y = linear_acceleration[1]
        imu_data.linear_acceleration.z = linear_acceleration[2]

        imu_data.angular_velocity.x = gyroscope[0]
        imu_data.angular_velocity.y = gyroscope[1]
        imu_data.angular_velocity.z = gyroscope[2]

        imu_data.orientation_covariance[0] = -1
        imu_data.linear_acceleration_covariance[0] = -1
        imu_data.angular_velocity_covariance[0] = -1

        self.imu_data_seq_counter=+1

        self.pub_imu_data.publish(imu_data)

    def run(self):

        # Reset IMU to reset axis orientation.
        if self.reset_orientation == True:
            self.reset_imu()

        # Configuration is necessary every time the IMU is turned on or reset
        self.set_imu_configuration()

        # Set frequency
        rate = rospy.Rate(self.frequency)

        while not rospy.is_shutdown():

            if self.stop_request == False:

                #start_time = time.time()
                self.bno055.update_imu_data()
                #print("--- %s seconds ---" % (time.time() - start_time))

                # Publish imu data
                self.publish_imu_data()

                # Publish magnetometer data
                if self.use_magnetometer == True:
                    self.publish_imu_magnetometer()

                # Publish temperature data
                if self.use_temperature == True:
                    self.publish_imu_temperature()

            rate.sleep()


if __name__ == '__main__':

    imu = SensorIMU()

    try:
        imu.run()

    except rospy.ROSInterruptException:
        pass
