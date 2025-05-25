import sys
import time
import board
import adafruit_emc2101

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA

if len(sys.argv) == 2:
	dutyCycle=int(sys.argv[1])
else:
	print('-1')
	sys.exit(1)

try:
	emc = adafruit_emc2101.EMC2101(i2c)
	
	emc.manual_fan_speed = dutyCycle
	temperature = emc.internal_temperature
	fanspeed = emc.fan_speed
except:
	fanspeed=0
	temperature=0

print('{0:0.1f} | {1:0.1f}'.format(temperature, fanspeed))