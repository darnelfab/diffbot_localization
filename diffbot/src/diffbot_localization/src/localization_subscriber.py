#!/usr/bin/env python
import rospy
from std_msgs.msg import String



class listener:
    def __init__(self):
        rospy.init_node('subscriber', anonymous=True)
        rospy.Subscriber("subscribed_topic", String, self.callback)
        rospy.spin()

    def callback(self,data):
        print(data)


if __name__ == '__main__':
    try:
        node=listener()
    except rospy.ROSInterruptException:
        pass
