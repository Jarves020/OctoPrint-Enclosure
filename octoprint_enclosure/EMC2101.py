import sys
import time
import board
import adafruit_emc2101

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA

try:
	emc = adafruit_emc2101.EMC2101(i2c)
	itemperature = emc.internal_temperature
	fanspeed = emc.fan_speed
	temperature=itemperature

except:
	fanspeed=-1
	temperature=-1
	
print('{0:0.1f} | {1:0.1f}'.format(temperature, fanspeed))