import rospy
from geometry_msgs.msg import Twist
import sys
from std_msgs.msg import String

rospy.init_node("imu_node")
movement_publisher= rospy.Publisher('/diffbot/base_controller/imu', Twist , queue_size=10)
movement_cmd = Twist()

if len(sys.argv)>2:
    speed = float(sys.argv[1])
    time = float(sys.argv[2])  
    print("imu data stream")
    if speed > 0.0:
        print("velocity =" , speed , "m/s")      
    else:
        print("Speed ​​parameter is missing or the value is incorrect") 
    if time > 0.0:
        print ("Tiempo = ",time, "s")
        movement_cmd.linear.x = 0
        movement_cmd.linear.y = 0
        movement_cmd.linear.z = 0
        movement_cmd.angular.x = 0
        movement_cmd.angular.y = 0              
        movement_cmd.angular.z = 0
        movement_publisher.publish(movement_cmd)
        print ("Publishing")
        rospy.spin()      
    else:
        print ("Time parameter is missing or the value is incorrect")     
else:
    print('one or more argument is missing!!')
