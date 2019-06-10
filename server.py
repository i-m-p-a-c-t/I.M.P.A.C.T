
from flask import Flask, request, render_template, redirect, url_for, session, flash
import pymysql
import hashlib
import random
import pymysql
import random
import requests 
import numpy as np




db = pymysql.connect(host='localhost',user='root',passwd='', db="impact")
cursor = db.cursor()
app = Flask(__name__)
app.secret_key = '123'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login/')
def login_page():
    return render_template('login.html')

@app.route('/register/')
def register_page():
    return render_template('register.html')

@app.route('/user/')
def user_page():
    return render_template('user.html')

@app.route('/forgot-password/')
def forget_page():
    return render_template('forgot-password.html')

@app.route('/dashboard/')
def dashboard_page():
    email = session.get('email', None)
    return render_template('dashboard.html', email = email)

@app.route('/tables/')
def table_page():
    email = session.get('email', None)
    return render_template('tables.html', email = email)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    flag = False
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        h = hashlib.md5(password.encode())
        hash_password = h.hexdigest()
        cursor.execute("SELECT * FROM users WHERE Email = '%s' AND Password = '%s'" % (str(email) ,str(hash_password)))
        result_set = cursor.fetchall()
        if (len(result_set) > 0) :
            session['email'] = email
            return redirect(url_for('dashboard_page'))
    return render_template('login.html')         


@app.route('/reset/')
def reset_page():
    return render_template('reset.html')

@app.route('/logout')
def logout():
    return render_template('login.html')

@app.route('/charts/')
def chart_page():
    email = session.get('email', None)
    return render_template('charts.html', email = email)

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
    user_id = random.getrandbits(128)
    if (password == password2):
        h = hashlib.md5(password.encode())
        cursor.execute("""
        INSERT INTO users (Id,FName,LName,Gender,Email,Phone,Password) VALUES (%s,%s,%s,%s,%s,%s,%s) """,(user_id,str(fName),str(lName),str(gender),str(email),str(phone),str(h.hexdigest())))
        db.commit()
        return redirect(url_for('dashboard_page', email = email))
    return render_template('register.html')
if __name__ == "__main__":
    
    app.run(debug=True)
