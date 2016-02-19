
#!/usr/bin/env python

# Python Class for use on word clock project
# Assumes and 8x8 matrix common anode type
# David Saul 2015

# max7219 libuary Copyright 2015, Richard Hull
# https://github.com/rm-hull
# see http://max7219.readthedocs.org/index.html, for max7219.led documentaion

import max7219.led as led
import math

class DMS_wrdck:

	device = led.matrix(cascaded=1)

	def blank(self):	# blank - no hour displayed 
                pass

	def one(self):
		self.device.set_byte(0,4,0B00000111)

	def two(self):
		self.device.set_byte(0,3,0B00000011)
		self.device.set_byte(0,2,0B00000010)

	def three(self):
		self.device.set_byte(0,4,0B11111000)

	def four(self):
                self.device.set_byte(0,2,0B00001111)

	def five(self):
                self.device.set_byte(0,2,0B11110000)

	def six(self):
                self.device.set_byte(0,1,0B00000111)

	def seven(self):
                self.device.set_byte(0,1,0B11111000)

	def eight(self):
                self.device.set_byte(0,5,0B11111000)

	def nine(self):
                self.device.set_byte(0,5,0B00001111)

	def ten(self):
                self.device.set_byte(0,5,0B10000000)
		self.device.set_byte(0,4,0B10000000)
		self.device.set_byte(0,3,0B10000000)

	def eleven(self):
                self.device.set_byte(0,3,0B11111100)

	def twelve(self):
                self.device.set_byte(0,3,0B01111111)

	def oclock(self):	# blank no minute displayed
		pass		# pass is like nop in machine code 
	
	def five_past(self):
		self.device.set_byte(0,7,0B00101011)
		self.device.set_byte(0,6,0B01111000)

	def ten_past(self):
		self.device.set_byte(0,7,0B11010000)
		self.device.set_byte(0,6,0B01111000)

	def fifteen_past(self):
		self.device.set_byte(0,7,0B11110111)
		self.device.set_byte(0,6,0B01111000)

 	def twenty_past(self):
		self.device.set_byte(0,8,0B11111100)
		self.device.set_byte(0,6,0B01111000)

	def twenty5_past(self):
		self.device.set_byte(0,8,0B11111100)
		self.device.set_byte(0,7,0B00101011)
		self.device.set_byte(0,6,0B01111000)

	def half_past(self):
		self.device.set_byte(0,8,0B00000011)
		self.device.set_byte(0,6,0B01111011)

	def twenty5_to(self):
		self.device.set_byte(0,8,0B11111100)
		self.device.set_byte(0,7,0B00101011)
		self.device.set_byte(0,6,0B11000000)

	def twenty_to(self):
		self.device.set_byte(0,8,0B11111100)
		self.device.set_byte(0,6,0B11000000)

	def fifteen_to(self):
		self.device.set_byte(0,7,0B11110111)
		self.device.set_byte(0,6,0B11000000)

	def ten_to(self):
		self.device.set_byte(0,7,0B11010000)
		self.device.set_byte(0,6,0B11000000)

	def five_to(self):
		self.device.set_byte(0,7,0B00101011)
		self.device.set_byte(0,6,0B11000000)

	
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
                if min == 12:
                        min = 0
#		print "min lookup ",min		# for debug only
	
		# Display miuntes past / to the hour in to nearest 5 minute 'slot'
                pointerm = [self.oclock,self.five_past,self.ten_past,self.fifteen_past,\
		self.twenty_past,self.twenty5_past,self.half_past,self.twenty5_to,\
		self.twenty_to,self.fifteen_to,self.ten_to,self.five_to]
                pointerm[min]()

#		print "hour lookup ", hour	# for debug only

		# Display the hours
                pointer = [self.blank,self.one,self.two,self.three,self.four,self.five,\
		self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve]
                pointer[hour]()

		# update the output drivers
                self.device.flush()



		

