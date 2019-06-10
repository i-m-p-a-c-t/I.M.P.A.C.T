# I.M.P.A.C.T
Intelligent Messaging Personal Accident Communication Technology

# Introduction
With a lot of consideration, and thoughts within our team, we have decided to implement an IoT product that would help increase the response rate when a traffic accident happens, and that would help save lives in the process. We have come up with a product that would detect when a car is in a collapsed or flipped state. We have learned that in most cases in a traffic accident relating to a car flipping over with the driver or passengers inside the car, they are not able to call or get help as quickly as they should. Sometimes a split second in response time from the emergency crews can determine the life and death of the victims in this situation. 
<br>
With that in mind, our concept for the product is simple concept, we will be utilizing sensors such as gyroscope and accelerometer and will be integrating it to a vehicle to help detect whether is flipped or in collapsed state. Our sensors will be sending data, and will be talking with our interface, and if it detects a positive state (collapsed state), our application will notify emergency personals in place of the victim. Moreover, the consumers of our product will also have access to our interface where they will have to sign up with our application, and provide their and love ones’ contacts information. When an accident occurs, not only our application will call emergency personals as mentioned above, it will also alert their love ones with a text/SMS specifying the location of the accident, so their love ones are aware, and could also get help or come help. 

# Implementation
In the early stage of the project, we started off by figuring out the sensors, and what technologies or hardware we wanted to include to accomplish our end goal. Once we have that figured out, we started experimenting with our hardware, and sensors to see what kind of data are being given by them, and what we can do with them. One of the technologies we used is gyroscope sensor which we use to help detect flipped state. The sensor gave us angle as data, and we used this to calculate if a car is flipped (angle > 90).  We also made used pi camera where we incorporated with Microsoft Visual Recognition machine learning model to detect what kind of mood the driver currently has. Another technology we used is GPS using Ardunio to ping pong the latitude and longitude coordinate of the current user and we pass that coordinate to our front end and use it on the Bing Map API to display the current location of the user, but we also implemented a nearby system to track the nearest hospital based on a specific radius that we provided and send the message or phone call to the hospital to help to come to the user’s place.
<br><br>
Our next step was building a web interface to represent our application and test our prototype. We used Flask library in Python to build our web interface, and REST APIs. We decided to use this because it fit well with the technologies that we are using, and makes the job of connecting them together easier. On the web interface, we constantly grabbed data from our hardware, and showcase on the platform. Every time, we detect a flipped state we text a message to presumably an emergency responder, and send emails to prove the concept of our prototype. The camera is also constantly detecting face of the driver, and updating the current mood to the web interface. The GPS system will continue to sending the current location of the user for every one minute and that data will be used to display the user’s current location on the Bing Map and also it will show the nearest hospital around the user’s current area so if they involve in accident the system will notify the nearest hospital to come to help the user.

# Devices
__Components__
  * Raspberrypi
  * Grovepi
  * Accelerometer
  * Pi Camera
  * Naroband
  
# Techonology
__Technologies__
  * Microsoft Vision API (provided inside the code)
  * Microsoft Bing Map API (provided inside the code)
  * Phpmyadmin
  * IBM Watson
  * Twilio
  
# Languages
__List of all the languages that have been implemented in the project__
 * Python
 * Javascript
 * C
 * Html5
 * Css
 * Bootstrap
 * Javascript
 * MySql
 * Sass
 * Jquery
# Llibrary
__python libary that needs to run the program__
 * Flask
 * pymysql
 * hashlib
 * random
 * requests
 * numpy
 * time
 * json
 * PiCamera
 * sleep
 * operator
 * uuid
 * redis
 * smtplib
 * Client
 * threading
 * ADXL345
 * math
# Instruction 
__Down load the zip file and extract it to the specific location you want to run inside the raspbian__
Install all the libraries that have been listed about then run the command below 
<br>
```sudo python3 vision.py```
<br>
Open another terminal and run 
```sudo python3 app.py```
<br>
Install Phpmyadmin on raspbian and then import the impact SQL file inside the Phpmyadmin then start copy the local IP address that have been provided in the terminal, paste the address to the web browser. Start registering for an account and then login to start using the application.

