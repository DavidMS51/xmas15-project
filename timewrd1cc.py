
#!/usr/bin/env python

# Python Class for use on word clock project
# Assumes and 8x8 matrix
# David Saul 2015

# max7219 libuary Copyright 2015, Richard Hull
# https://github.com/rm-hull
# see http://max7219.readthedocs.org/index.html, for max7219.led documentaion
#
# THIS VERSION OF timewrd IS FOR USE WITH COMMON CATHODE MATRIX
# USE THE ca VERSION FOR COMMON ANODE TYPES - LIKE THE 1088AS

import max7219.led as led
#import max7219.rotate8x8 as rotate
import math

class DMS_wrdck:

	device = led.matrix(cascaded=1)

	def blank(self):	# blank - no hour displayed 
                pass

	def one(self):
	#	self.device.set_byte(0,4,0B00000111)

		self.device.pixel(7,4,1,0)
		self.device.pixel(6,4,1,0)
		self.device.pixel(5,4,1,0)


	def two(self):
	#	self.device.set_byte(0,3,0B00000011)
	#	self.device.set_byte(0,2,0B00000010)

		self.device.pixel(7,5,1,0)
                self.device.pixel(6,5,1,0)
                self.device.pixel(6,6,1,0)

	def three(self):
	#	self.device.set_byte(0,4,0B11111000)

                self.device.pixel(4,4,1,0)
                self.device.pixel(3,4,1,0)
                self.device.pixel(2,4,1,0)
                self.device.pixel(1,4,1,0)
                self.device.pixel(0,4,1,0)

	def four(self):
        #	self.device.set_byte(0,2,0B00001111)

                self.device.pixel(7,6,1,0)
                self.device.pixel(6,6,1,0)
                self.device.pixel(5,6,1,0)
                self.device.pixel(4,6,1,0)

	def five(self):
        #	self.device.set_byte(0,2,0B11110000)

                self.device.pixel(3,6,1,0)
                self.device.pixel(2,6,1,0)
                self.device.pixel(1,6,1,0)
                self.device.pixel(0,6,1,0)

	def six(self):
        #	self.device.set_byte(0,1,0B00000111)

                self.device.pixel(7,7,1,0)
                self.device.pixel(6,7,1,0)
                self.device.pixel(5,7,1,0)

	def seven(self):
        #	self.device.set_byte(0,1,0B11111000)
                self.device.pixel(4,7,1,0)
                self.device.pixel(3,7,1,0)
                self.device.pixel(2,7,1,0)
                self.device.pixel(1,7,1,0)
		self.device.pixel(0,7,1,0)

	def eight(self):
        #	self.device.set_byte(0,5,0B11111000)

                self.device.pixel(4,3,1,0)
                self.device.pixel(3,3,1,0)
                self.device.pixel(2,3,1,0)
                self.device.pixel(1,3,1,0)
                self.device.pixel(0,3,1,0)

	def nine(self):
        #	self.device.set_byte(0,5,0B00001111)

                self.device.pixel(7,3,1,0)
                self.device.pixel(6,3,1,0)
                self.device.pixel(5,3,1,0)
                self.device.pixel(4,3,1,0)

	def ten(self):
        #	self.device.set_byte(0,5,0B10000000)

                self.device.pixel(0,3,1,0)
                self.device.pixel(0,4,1,0)
                self.device.pixel(0,5,1,0)

	def eleven(self):
        #	self.device.set_byte(0,3,0B11111100)

                self.device.pixel(5,5,1,0)
                self.device.pixel(4,5,1,0)
                self.device.pixel(3,5,1,0)
                self.device.pixel(2,5,1,0)
                self.device.pixel(1,5,1,0)
                self.device.pixel(0,5,1,0)

	def twelve(self):
        #	self.device.set_byte(0,3,0B01111111)

                self.device.pixel(7,5,1,0)
                self.device.pixel(6,5,1,0)
                self.device.pixel(5,5,1,0)
                self.device.pixel(4,5,1,0)
                self.device.pixel(2,5,1,0)
                self.device.pixel(1,5,1,0)

	def oclock(self):	# blank no minute displayed
		pass		# pass is like nop in machine code 
	
	def five_hr(self):
	#	self.device.set_byte(0,7,0B00101011)
	#	self.device.set_byte(0,6,0B01111000)

                self.device.pixel(7,1,1,0)
                self.device.pixel(6,1,1,0)
                self.device.pixel(4,1,1,0)
                self.device.pixel(2,1,1,0)

	def ten_hr(self):
	#	self.device.set_byte(0,7,0B11010000)
	#	self.device.set_byte(0,6,0B01111000)

                self.device.pixel(3,1,1,0)
                self.device.pixel(2,1,1,0)
                self.device.pixel(0,1,1,0)

	def fifteen(self):
	#	self.device.set_byte(0,7,0B11110111)
	#	self.device.set_byte(0,6,0B01111000)

                self.device.pixel(7,1,1,0)
                self.device.pixel(6,1,1,0)
                self.device.pixel(5,1,1,0)
                self.device.pixel(3,1,1,0)
                self.device.pixel(2,1,1,0)
                self.device.pixel(1,1,1,0)
                self.device.pixel(0,1,1,0)

 	def twenty(self):
	#	self.device.set_byte(0,8,0B11111100)
	#	self.device.set_byte(0,6,0B01111000)

                self.device.pixel(5,0,1,0)
                self.device.pixel(4,0,1,0)
                self.device.pixel(3,0,1,0)
                self.device.pixel(2,0,1,0)
                self.device.pixel(1,0,1,0)
                self.device.pixel(0,0,1,0)


	def twenty5(self):
#		self.device.set_byte(0,8,0B11111100)
#		self.device.set_byte(0,7,0B00101011)
#		self.device.set_byte(0,6,0B01111000)

                self.device.pixel(5,0,1,0)
                self.device.pixel(4,0,1,0)
                self.device.pixel(3,0,1,0)
                self.device.pixel(2,0,1,0)
                self.device.pixel(1,0,1,0)
                self.device.pixel(0,0,1,0)
                self.device.pixel(7,1,1,0)
                self.device.pixel(6,1,1,0)
                self.device.pixel(4,1,1,0)
                self.device.pixel(2,1,1,0)


	def half(self):
	#	self.device.set_byte(0,8,0B00000011)
	#	self.device.set_byte(0,6,0B01111011)

                self.device.pixel(7,0,1,0)
                self.device.pixel(6,0,1,0)
                self.device.pixel(7,2,1,0)
                self.device.pixel(6,2,1,0)
		

	def past(self):

                self.device.pixel(4,2,1,0)
                self.device.pixel(3,2,1,0)
                self.device.pixel(2,2,1,0)
                self.device.pixel(1,2,1,0)


	def to(self):

                self.device.pixel(1,2,1,0)
                self.device.pixel(0,2,1,0)


	
	def ckdisp(self,mint,hour):

		# Perfor basic error check on variables
               	if mint < 0 or mint > 59:
                        return
               	if hour < 0 or hour > 12:
                        return

		# Clear the display first
		self.device.clear(0)

		# Convert minutes into 5 minute slots
                mint = float(mint)
                mint = mint / 5
                tmp = math.modf(mint)
                if tmp[0] < 0.5:
                        min = int(tmp[1])
                else:
                        min = int(tmp[1]+1)

		# add incrument 'hour' for >30 mins past the hour
		if min > 6:
			hour = hour +1
			if hour == 13:
				hour = 1	

		# Bodge to keep display correct for the last 3 minutes before the hour
#                if min == 12:
 #                       min = 0

		
		# compile past / to as need
		if min == 12:			# Bodge to keep display correct for the last
			min = 0			# 3 minutes before the hour

		elif min == 0:			# Bodge to keep display correct for the last
			pass			# 3 minutes past the hour

		elif min < 7:			# before half past display 'past'
			self.past()

		else:
			self.to()		# otherwise display 'to'
			min = (6-(min-6))	# sort out 'min' offset for 'to' 5 minute slots 	

#		print "min lookup ",min		# for debug only
	
		# Display miuntes past / to the hour in to nearest 5 minute 'slot'
                pointerm = [self.oclock,self.five_hr,self.ten_hr,self.fifteen,\
		self.twenty,self.twenty5,self.half]
		
                pointerm[min]()

#		print "hour lookup ", hour	# for debug only

		# Display the hours
                pointer = [self.blank,self.one,self.two,self.three,self.four,self.five,\
		self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve]
                pointer[hour]()

		# update the output drivers
                self.device.flush()



		

