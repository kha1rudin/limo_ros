#!/usr/bin/env python

from std_msgs.msg import String
from limo_status_translator import *
import rospy

# global var
client_data = None
limo_data = None

vehicle_state = int(0)
control_mode = int(0)
battery_voltage = float(0.0)
error_code = int(0)
motion_mode = int(0)

# callback from client
def callback_client(data):
	global client_data
	client_data = data.data
	rospy.loginfo("%s", client_data) 

# callback to limo
def callback_limo(data):
	global limo_data
	limo_data = data.data
	rospy.loginfo("%s", limo_data)

def status_string():
	rospy.init_node('limo_status_translator_node', anonymous=True)
	sub_limo = rospy.Subscriber('limo_status', String, callback_limo)
	sub_client = rospy.Subscriber('status_received', String, callback_client)
	pub_client = rospy.Publisher('status_from_translator', String, queue_size=1)
	rate = rospy.Rate(1)
	rtn_str = "No request"	

	while not rospy.is_shutdown():
		print("%s", limo_data)
		rospy.wait_for_service('Get_limo_status')
		request_info = rospy.ServiceProxy('Get_limo_status', GetLimoStatus)
		if client_data == "0" : rtn_str = "STATUS 0"
		pub_client.publish(rtn_str)
		rate.sleep()
		rospy.loginfo(rtn_str + " sent")
		if client_data == "1" : rtn_str = "STATUS 1"
		pub_client.publish(rtn_str)
		rate.sleep()
		rospy.loginfo(rtn_str + " sent")
		if client_data == "2" : rtn_str = "STATUS 2"
		pub_client.publish(rtn_str)
		rate.sleep()
		rospy.loginfo(rtn_str + " sent")
		if client_data == "3" : rtn_str = "STATUS 3"
		pub_client.publish(rtn_str)
		rate.sleep()
		rospy.loginfo(rtn_str + " sent")
		if client_data == "4" : rtn_str = "STATUS 4"
		pub_client.publish(rtn_str)	# communicate to client - return a string
		rate.sleep()
		rospy.loginfo(rtn_str + " sent")

if __name__ == '__main__':
    try:
        status_string()
    except rospy.ROSInterruptException:
        pass
