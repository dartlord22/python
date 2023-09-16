from flask_app import app
from flask_app.models.user import User
from flask_app.models.tree import Tree
from flask import redirect, render_template, request, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login_and_registration.html')

@app.route('/login/process', methods=['POST'])
def process_login():
    valid_user = User.validate_login(request.form)
    if not valid_user:
        return redirect('/login')
    
    user = User.get_by_email(request.form)
    session['user_id'] = user.id    
    
    return redirect('/dashboard')
    

@app.route('/registration/process', methods=['POST'])
def process_registration():
    if not User.validate_registration(request.form):
        return redirect('/')
    data ={ 
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    User.save(data)
    
    user = User.get_by_email(request.form)
    session['user_id'] = user.id 
    
    return redirect('/dashboard')

@app.route('/user/account/<int:id>')
def my_profile(id):
    if 'user_id' not in session:
        return redirect('/login')
    
    data = {'id': id}
    return render_template('my_profile', user_trees=User.get_one_with_trees(data), user=User.get_by_id({'id':session['user_id']}))

@app.route('/logout')
def logout():
    return redirect('/')