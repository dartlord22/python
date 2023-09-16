from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models import dojo
from flask import render_template, request, redirect

@app.route('/ninja/edit/<int:id>')
def edit_ninja(id):
    data = {'id': id}
    return render_template('edit_ninja.html', ninja=Ninja.get_one(data))

@app.route('/ninja/edit/process', methods=['POST'])
def process_edit_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.update_ninja(data) #could also pass in request.form directly into our update method as long as our names in the template line up with the names in the model/db
    return redirect('/dojos/all')
    
@app.route('/ninja/new')
def new_ninja():
    return render_template('new_ninja.html', dojos=dojo.Dojo.get_all())

@app.route('/ninja/new/process', methods=['POST'])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.create_ninja(data)
    return redirect('/dojos/all')
    
    