#!/usr/bin/env python3
import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import random

import numpy

def talker():
    pub = rospy.Publisher('s52s8', numpy_msg(Floats),queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        a = numpy.array([1+random.random(), 1+random.random(), 1+random.random(), 1+random.random()], dtype=numpy.float32)
        pub.publish(a)
        r.sleep()

if __name__ == '__main__':
    talker()