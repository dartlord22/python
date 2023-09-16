from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, request, redirect

@app.route('/dojos/all')
def all_dojos():
    return render_template('all_dojos.html', dojos=Dojo.get_all())

@app.route('/dojos/new', methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.create(data)
    return redirect('/dojos/all')

@app.route('/dojos/ninjas/<int:id>')
def view_dojo(id):
    data = {
        'id': id
    }
    return render_template('view_dojo.html', dojo=Dojo.get_one(data))