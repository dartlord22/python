from flask_app import app 
from flask import render_template, redirect, request, session
from flask_app.models.tree import Tree
from flask_app.models.user import User

@app.route('/dashboard')
def dashboard(): 
    if 'user_id' not in session:
        return redirect('/login')
    
    return render_template('arbortrary_dashboard.html', user=User.get_by_id({'id':session['user_id']}), trees=Tree.get_all())

@app.route('/new/tree')
def plant_tree():
    if 'user_id' not in session:
        return redirect('/login')
    
    return render_template('plant_tree.html', user=User.get_by_id({'id':session['user_id']}))

@app.route('/new/tree/process', methods=['POST'])
def process_plant_tree():
    if 'user_id' not in session:
        return redirect('/login')
    
    if not Tree.validate_tree(request.form):
        return redirect('/new/tree')
    
    data = {
        'user_id': session['user_id'],
        'species': request.form['species'],
        'location': request.form['location'],
        'reason': request.form['reason'],
        'date_planted': request.form['date_planted']
    }
    Tree.save(data)
    return redirect('/dashboard')

@app.route('/show/<int:id>')
#id passed in as argument below
def show_tree(id):
    if 'user_id' not in session:
        return redirect('/login')
#make a data dictionary to pair our argument with the id value from our database    
    data = {'id': id}
#then pass data into the get_one() method 
    return render_template('show_tree.html', user=User.get_by_id({'id':session['user_id']}), tree=Tree.get_one(data))

@app.route('/edit/<int:id>')
def edit_tree(id):
    if 'user_id' not in session:
        return redirect('/login')
    
    data = {'id': id}
    
    return render_template('edit_tree.html', tree=Tree.get_one(data), user=User.get_by_id({'id':session['user_id']}))

@app.route('/edit/process/<int:id>', methods=["POST"])
def process_edit_tree():
    if 'user_id' not in session:
        return redirect('/login')

    Tree.update(request.form) 
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def delete(id):
    data = {'id': id}

    Tree.delete(data)
    return redirect('/user/account/<int:id>')