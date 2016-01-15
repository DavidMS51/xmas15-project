#!/usr/bin/env python

# Basic 8x8 workclock program
# Requires timewrd1.py to be in same folder - this has the word data in

# to shutdown hold red and blue pushs for about 6 seconds

import os
from time import sleep
from timewrd1cc import DMS_wrdck	# setup for calling common cathode drive version
import datetime
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#set up class access
wrdck = DMS_wrdck()

def prog_term():
	# checks both keys are held down for 6 seconds before halting, while writing
	# 'countdown' bars across the screen
	# 
	print
	print "WARNING PI WILL START SHUTDOWN IF KEY HELD FOR 3 SECONDS"
	print
	t = 0
	col = 0
	while col < 8:
		col = col + 1
		while t < 8:
			t=t+1
			# check the keys are still being held down
			if GPIO.input(red) == True or GPIO.input(blue) == True:
				# clear and reset the display
				wrdck.device.clear()	
				wrdck.ckdisp(cur_time_min,cur_time_hr)
				print "shut down aborted"
				return()
			sleep(.1)
		wrdck.device.set_byte(0,col,0B11111111)
		wrdck.device.flush()		
		t = 0


	print "halting now"
	wrdck.device.clear()
	# halt pi
	os.system("sudo poweroff")
	sleep(10)

def tset():

	# wait for yellow key to be released
	while GPIO.input(yellow) == False: # wait until push is released
                                sleep(.1)

	sleep(.2)
	tout = 100
	wrdck.device.clear()	# clear display
	wrdck.device.pixel(5,2,1,1)	# shoe * to indicate device in set mode
	cur_time_hrt=int(datetime.now().strftime('%I'))  # these are local variable so need re defining
	cur_time_mint=int(datetime.now().strftime('%M'))

	while True:
		tout = tout -1	#dec time out counter
		if tout ==0:	# if tout reaches zero drop back to main prog loop with out changing time
			# clear and reset the display
			wrdck.device.clear()
                     	wrdck.ckdisp(cur_time_min,cur_time_hr)
                        print "time out - time update aborted"
			return

		if GPIO.input(red) == False:	# check for red push if yes inc hour counter
			tout = 100	# reset time out flag
			while GPIO.input(red) == False:	# wait until push is released
				sleep(.1)
			cur_time_hrt=cur_time_hrt+1	# increment temp hour flag 
			if cur_time_hrt == 13:
				cur_time_hrt = 1

			wrdck.ckdisp(cur_time_mint,cur_time_hrt) # display temp time info
			wrdck.device.pixel(5,2,1,1)

                elif GPIO.input(blue) == False:    # check for blue push if yes inc hour counter
                        tout = 100      # reset time out flag
                        while GPIO.input(blue) == False: # wait until push is released
                                sleep(.1)
                        cur_time_mint=cur_time_mint+5     # increment temp hour flag
                        if cur_time_mint >59:
                                cur_time_mint = 0

                        wrdck.ckdisp(cur_time_mint,cur_time_hrt) # display temp time info
                        wrdck.device.pixel(5,2,1,1)

		elif GPIO.input(yellow) == False:		# check for yellow push if yes
							# start time update procedure to hwclock

        		print
		        print "WARNING SYSTEM TIME  WILL BE UPDATED IF KEY HELD FOR 3 SECONDS"
		        print
		        t = 0
		        col = -1
		        while col < 7:
                		col = col + 1
                		while t < 8:
                        		t=t+1
                        		# check the yellow key is still being held down
                        		if GPIO.input(yellow) == True:
                        		        # clear and reset the display
                                		wrdck.device.clear()
                                		wrdck.ckdisp(cur_time_min,cur_time_hr)
                                		print "time update aborted"
                                		return()
                        		sleep(.1)
	       	        	wrdck.device.pixel(col,col,1,1)
                		t = 0


        		print "updating TIME now"
        		wrdck.device.clear()
        		# time update code in here

#			os("sudo date -s"+
			wrdck.device.clear()			# re-fresh the display
                        wrdck.ckdisp(cur_time_min,cur_time_hr)
			sleep(2)
			return()
 		sleep(.1)

#set up buttons to thier GPIO no

blue = 20
red = 21
yellow = 22

GPIO.setup(blue,GPIO.IN)
GPIO.setup(red,GPIO.IN)
GPIO.setup(yellow,GPIO.IN)

t = 0		#initise temp counter for later

#get an initial time
cur_time_hr=int(datetime.now().strftime('%I'))
cur_time_min=int(datetime.now().strftime('%M'))

#ckdisp() take 2 arguments in the min (0-59) and hour (0-12 displays) them
# on an 8x8 matrix suitably coded

print
print
print "Starting Clock Application"



while True:
#	wrdck.device.clear(0)
	# update display
	wrdck.ckdisp(cur_time_min,cur_time_hr)
	
	# wait until minute changes before calling display update again
	temp = cur_time_min
#	print cur_time_hr,cur_time_min
	while cur_time_min == temp:
		cur_time_min=int(datetime.now().strftime('%M'))
		print "hr",cur_time_hr,"mn",cur_time_min
		t = 0
		while t < 100:			# delay with key push check
			t = t + 1
			sleep(.1)
			if GPIO.input(red) == False and GPIO.input(blue) == False:
				prog_term()
			elif GPIO.input(yellow) == False:
				tset()		

	cur_time_hr=int(datetime.now().strftime('%I'))	




