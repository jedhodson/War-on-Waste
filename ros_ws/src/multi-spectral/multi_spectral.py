#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class MultiSpectral:
    """ To move the RGB values so R -> G, G -R B, B -> R """

    def __init__(self):
        self.publisher_1 = rospy.Publisher("multispectral/one", Image, queue_size=1)
	self.publisher_2 = rospy.Publisher("multispectral/two", Image, queue_size=1)
	self.publisher_3 = rospy.Publisher("multispectral/three", Image, queue_size=1)
	self.publisher_c = rospy.Publisher("multispectral/combo", Image, queue_size=1)

        self.subscriber = rospy.Subscriber("/camera/image_raw", Image, self.callback, queue_size=1)

        self.bridge = CvBridge()

        self.activeChannel = 0

        self.ch1_pin = 11
        self.ch2_pin = 12
	self.ch3_pin = 13

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup((11, 12, 13), GPIO.OUT, initial=GPIO.LOW)

    def callback(self, raw):
        frame = self.bridge.imgmsg_to_cv2(raw, desired_encoding="passthrough")

	(channel_ir, channel_g, channel_r) = cv2.split(frame)

        if self.activeChannel == 0:
	  GPIO.output((12, 13), GPIO.LOW)
	  GPIO.output(11, GPIO.HIGH)
	  self.activeChannel = 1
	  self.ch_r = channel_ir
          self.publisher_1.publish(self.bridge.cv2_to_imgmsg(cv2.merge([channel_ir, channel_ir, channel_ir]), encoding="rgb8"))
	elif self.activeChannel == 1:
	  GPIO.output((11, 13), GPIO.LOW)
	  GPIO.output(12, GPIO.HIGH)
	  self.activeChannel = 2
	  self.ch_g = channel_ir
          self.publisher_2.publish(self.bridge.cv2_to_imgmsg(cv2.merge([channel_ir, channel_ir, channel_ir]), encoding="rgb8"))
	elif self.activeChannel == 2:
          GPIO.output((11, 12), GPIO.LOW)
	  GPIO.output(13, GPIO.HIGH)
          self.ch_b = channel_ir
	  self.publisher_3.publish(self.bridge.cv2_to_imgmsg(cv2.merge([channel_ir, channel_ir, channel_ir]), encoding="rgb8"))
	  self.activeChannel = 0

#        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

	

#	mergedImage = cv2.merge([mono_ch, mono_ch, mono_ch])

	mergedImage = cv2.merge([self.ch_r, self.ch_g, self.ch_b])

#	mergedImage = frame

        out = self.bridge.cv2_to_imgmsg(mergedImage, encoding="rgb8")

        self.publisher_c.publish(out)


def main():
    """ Intialises and cleansup after the ros node """

    rospy.init_node("multi_spectral", log_level=rospy.INFO, anonymous=True)

    spectral = MultiSpectral()
    try:
        rospy.spin()
    except KeyboardInterrupt:
	GPIO.cleanup()
        print("Exit")


if __name__ == "__main__":
    main()
