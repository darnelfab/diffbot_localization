#!/usr/bin/env python
import rospy
from std_msgs.msg import String


class talker:
    def __init__(self):
        rospy.init_node('publisher',anonymous=True)
        self.pub=rospy.Publisher('published_topic',String,queue_size=10)
        self.rate=rospy.Rate(10)

    def run(self):
        rate=rospy.Rate(10)
        while not rospy.is_shutdown():
            message="this message was sent at %s"%rospy.get_time()
            self.pub.publish(message)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        node=talker()
        node.run()
    except rospy.ROSInterruptException:
        pass
