#-*- coding:utf-8 -*-

import os
import time
#cmd = "adb shell input keyevent 27"
sleep = "sleep(2)"
""""for i in range(5):
	os.popen(cmd)
	print("capture:", i)
"""
count = 0
while True:
	os.popen("adb shell input keyevent 27")
#	os.popen(sleep)
	time.sleep(1)
	count += 1
	if count == 5:
		print("capture over")
		break
#pull isp-log
os.popen("adb pull /data/log/isp-log")
os.popen("adb shell rm /data/log/isp-log/*")
