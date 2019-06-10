# ****************************************
# This program will collect temperature
# and humidity data from the GrovePi+ 
# sensors, and incorporate button switch to 
# turn light on and off and transmit the data to IBM
# Watson IoT Platform to be displayed in 
# real-time.
# Author: David Chau, Vecheka Chhourn, Huy Tran
# Date: May 15, 2019
# ****************************************
import json
import time
#import sensorV2
#import vision
import paho.mqtt.client as mqtt

# IBM Watson IoT Platform connection details...
host = '8gdk2c.messaging.internetofthings.ibmcloud.com'
clientid = 'd:8gdk2c:ImpactSensor:IS'
username = 'use-token-auth'
password='Yo(cl&i6n-eQS@A*4o'
topic='iot-2/evt/data/fmt/json'

#connect to IBM Watson IoT platform server
client = mqtt.Client(clientid)
client.username_pw_set(username, password)
client.connect(host, 1883, 60)

def sendData(angle, mood):
    
    try:	    
        client.publish(topic, json.dumps({'Angle':angle,
                                          'Mood':mood
                                          }))	
            
            
    except Exception as ex:
            print('An error has occurred: %s' % ex)
    except KeyboardInterrupt:
            client.disconnect()

#loops forever and finally close the connection
client.loop()

