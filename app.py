from flask import Flask, session ,render_template , redirect
from flask import request
from db import Databse
import api

app = Flask(__name__)

dbo = Databse()

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('uer_email')
    password = request.form.get('user_password')
    response = dbo.insert(name, email, password)
    if response:
        return render_template('login.html',message='register success')
    else:
        return  render_template('register.html',message='email already exist')

@app.route('/perform_login',methods=['post'])
def perform_login():

    user_email = request.form.get('user_email')
    user_password = request.form.get('user_possword')
    response = dbo.search(user_email, user_password)
    if response:
        session['login'] ==1
        return redirect('/profile')
    else:
        return render_template('login.html',message='incorrect email')

@app.route('/profile')
def profile():
    if session['login'] ==1
        return render_template('profile.html')
    else:
        redirect('/')

@app.route('/ner')
def ner():
    if['login']==1
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    if['login']==1
    text = request.form.get('ner_text')
    response = api.ner(text)
    return "somrething"

    for i in  response

app.run(debug = True)
