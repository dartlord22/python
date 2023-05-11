from flask_app import app 
from flask_app.models.user import User
from flask import render_template, redirect, request, session
import os
import uuid


@app.route('/')
def index():
    return redirect('/user/login')

@app.route('/user/login')
def login():
    return render_template('login.html')

@app.route('/user/register')
def register():
    return render_template('registration.html')

@app.route('/user/login/process', methods=['POST'])
def login_success():
    
    user = User.get_by_email(request.form)
    session['user_id'] = user.id 
    
    return redirect('/events')

@app.route('/user/register/process', methods=['POST'])
def register_success(): 
    data ={ 
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    User.save(data)
    return redirect('/user/login')

@app.route('/user/profile')
def my_profile():
    return render_template('my_profile.html', user=User.get_user_info({'id':session['user_id']}))

@app.route('/user/profile/save', methods=['POST'])
def my_profile_submit():
    data={
        'profile_picture': request.form['profile_picture']
    }
    User.save_picture(data)
    return redirect('my_profile.html')

@app.route('/logout')
def logout():
    return redirect('/')

