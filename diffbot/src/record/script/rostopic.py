#!/usr/bin/env python
import sys
import rospy
from geometry_msgs.msg import Twist

def commander(speed, time):
    movement_publisher = rospy.Publisher('cmd_vel', Twist , queue_size=10)
    rospy.init_node("diffbot_odometry", anonymous=True)
    rate = rospy.Rate(10) # 10hz
    movement_cmd = Twist()

    while not rospy.is_shutdown():
        movement_cmd.linear.x = 0
        movement_cmd.linear.y = 0
        movement_cmd.linear.z = 0
        movement_cmd.angular.x = 0
        movement_cmd.angular.y = 0
        movement_cmd.angular.z = 0
        rospy.logdebug("Publishing")
        movement_publisher.publish(movement_cmd)
        rate.sleep()

if __name__ == '__main__':
    speed = float(sys.argv[0])
    time = float(sys.argv[2])

    rospy.logdebug("Adelante") # Use rospy.logdebug() for debug messages.

    if speed > 0:
        rospy.logdebug("Velocidad = %s m/s", speed)
    else:
        raise ValueError("Falta parametro de velocidad o el valor es incorrecto")

    if time > 0 :
        rospy.logdebug("Tiempo = %s s", time)
    else:
        raise ValueError("Falta parametro de tiempo o el valor es incorrecto")

    try:
        commander(speed, time)
    except rospy.ROSInterruptException:
        pass
