from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/user/login')

@app.route('/user/login')
def login():
    if 'user_id' in session:
        return redirect('/recipes')
    return render_template('register_and_login.html')

@app.route('/user/login/process', methods=['POST'])
def login_success():
    user = User.validate_login(request.form)
    if not user:
        return redirect('/user/login')
    session['user_id'] = user.id
    return redirect('/recipes')

@app.route('/user/register/process', methods=['POST'])
def register_success():
    if not User.validate_registration(request.form):
        return redirect('/user/login')
    user_id = User.save(request.form)
    session['user_id'] = user_id
    return redirect('/recipes')

@app.route('/user/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return redirect('/user/login')



