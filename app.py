from flask import Flask, request, render_template, redirect, url_for, session, flash
#from flask_sse import sse
import flask
import pymysql
import hashlib
import random
import requests 
import numpy as np
import time
#import vision
import contact
import sensorV2
import threading
import uuid
import redis
# from flask_redis import Redis
import IBM_WATSON
## connecting to local database

## Pi Version user = admin, passwd = password
db = pymysql.connect(host='localhost',user='admin',passwd='password', db="impact")
cursor = db.cursor()
app = Flask(__name__)
current_safety = "yes"
DEFAULT_MOOD = "neutral"
# redis = Redis(app)
# app.config["REDIS_HOST"] = "localhost"
# app.config["REDIS_PORT"] = 6379

# app.config["REDIS2_URL"] = "redis://localhost:6379/1"
# app.register_blueprint(sse, url_prefix = "/stream")
app.secret_key = 'impact'
red = redis.StrictRedis()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/aboutus')
def aboutus_page():
    return render_template('aboutus.html')

@app.route('/user', methods=['GET', 'POST'])
def user_page():
    if session.get('login', None) == None:
            return redirect(url_for('index'))
    name = session.get('name', None)


    return render_template('user.html', name = name)

def event_stream():
    
    pubsub = red.pubsub()
    pubsub.subscribe('danger')
    angle = sensorV2.getAngle()
    moodFile = open("mood.txt", "r")
    mood = moodFile.readline()
    isSafe = "yes"
    if angle >= 90 or angle <= -90:
        isSafe = "no"
        contact.send_message()
        contact.dial_numbers()
    
    #mood = vision.get_current_mood()
    message = isSafe + ", " + mood
    yield 'data: %s\n\n' % message
    ##time.sleep(1)
    IBM_WATSON.sendData(angle, mood)
        



@app.route('/stream')
def stream():
	return flask.Response(event_stream(),
	mimetype="text/event-stream")


# @app.route('/test', methods = ['POST'])
# def test_push():
	# sse.publish({"message": "Hello World!"} , type = "test")
	# return "Message Sent!"

        
# @app.route('/get_safety_status', methods=['GET'])
# def get_safety_status():
    # IBM_WATSON.sendData()
    # angle = sensorV2.getAngle()
    # isSafe = "yes"
    # if angle >= 90 or angle <= -90:
        # isSafe = "no" 
    # return isSafe

# @app.route('/get_current_mood', methods = ['GET'])
# def get_current_mood():
    # #numbers = ["+12064883393"]
    # #twilio_phone.dial_numbers(numbers)
    # return vision.get_current_mood();

# @app.route('/contact_help', methods = ['GET'])
# def contact_help():
    # contact.send_message();


@app.route('/forgot-password')
def forget_page():
    
    return render_template('forgot-password.html')

@app.route('/dashboard')
def dashboard_page():
    if session.get('login', None) == None:
        return redirect(url_for('index'))
    name = session.get('name', None)
    return render_template('dashboard.html', name = name)


@app.route('/tables')
def table_page():
    if session.get('login', None) == None:
        return redirect(url_for('index'))
    name = session.get('name', None)
    return render_template('tables.html', name = name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        h = hashlib.md5(password.encode())
        hash_password = h.hexdigest()
        cursor.execute("SELECT * FROM USERS WHERE Email = '%s' AND Password = '%s'" % (str(email) ,str(hash_password)))
        result_set = cursor.fetchall()
        if (len(result_set) > 0) :
            session['name'] = result_set[0][1] + " " + result_set[0][2]
            session['login'] = True	
            return redirect(url_for('dashboard_page'))
    return render_template('login.html')         


@app.route('/reset')
def reset_page():
    return render_template('reset.html')


@app.route('/logout')
def logout():
    session['login'] = None
    return render_template('login.html')


@app.route('/charts')
def chart_page():
    name = session.get('name', None)
    return render_template('charts.html', name = name)


@app.route('/reset_password', methods=['POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form['email']
        cursor.execute("SELECT * FROM users WHERE Email = '%s'" % str(email))
        result_set = cursor.fetchall()
        if (len(result_set) > 0):
            return redirect(url_for('reset_page'))


@app.route('/set_new_password', methods=['POST'])
def set_new_password():
    if request.method == 'POST':
        password = request.form['password']
        password2 = request.form['password2']
        if password == password2:
            h = hashlib.md5(password.encode())
            hash_password = h.hexdigest()
            cursor.execute("UPDATE users SET Password = '%s'" % str(hash_password))
            db.commit()
            return redirect(url_for('login_page'))
    return render_template('reset.html')


@app.route('/register', methods=['POST'])
def register():
    fName = request.form['fName']
    lName = request.form['lName']
    gender = request.form['gender']
    phone = request.form['phone']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']
    user_id = uuid.uuid4().hex
    if (password == password2):
        h = hashlib.md5(password.encode())
        cursor.execute("""
        INSERT INTO USERS (Id,FName,LName,Gender,Email,Phone,Password) VALUES (%s,%s,%s,%s,%s,%s,%s) """,
		(str(user_id),str(fName),str(lName),str(gender),str(email),str(phone),str(h.hexdigest())))
        session['login'] = True
        session['name'] = fName +  " " + lName
        db.commit()
        return redirect(url_for('dashboard_page'))
    return render_template('register.html')



## Run application
if __name__ == "__main__":
	app.debug=True
	app.run(threaded=True, port = 8080)
        
