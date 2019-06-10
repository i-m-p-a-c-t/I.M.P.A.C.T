# ADXL345 Python example 
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
# 
# This is an example to show you how to use our ADXL345 Python library
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer

from adxl345 import ADXL345
import math
import time

## return angle of the car
def orentation(X, Y, Z):
    Roll = math.atan2(Y, Z) * 180 / math.pi;
    Pitch = math.atan2(-X, math.sqrt(Y*Y + Z*Z)) * 180 / math.pi
    #print("Roll: ", Roll)
    #print("Pitch: ", Pitch)
    return Roll


def getAngle():
    
    adxl345 = ADXL345()
    #while(1):     
    axes = adxl345.getAxes(True)
    #print("ADXL345 on address 0x%x:" % (adxl345.address))
    #print("   x = %.3fG" % ( axes['x'] ))
    #print("   y = %.3fG" % ( axes['y'] ))
    #print("   z = %.3fG" % ( axes['z'] ))
    angle = orentation(axes['x'], axes['y'], axes['z'])
    
    #time.sleep(1.0)
    return angle


