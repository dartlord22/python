from flask_app import app 
from flask_app.models.event import Event 
import datetime
from flask import render_template, redirect, request, session

@app.route('/events')
def my_events():
    user_id = session['user_id']
    return render_template('my_events.html', events=Event.get_all(), datetime=datetime, user_id=user_id)

@app.route('/events/add', methods=['POST'])
def add_event():
    data = {
        'user_id': session['user_id'],
        'event_name': request.form['event_name'],
        'event_start': request.form['event_start'],
        'event_end': request.form['event_end'],
        'event_date': request.form['event_date'] 
    }
    Event.save(data)
    return redirect('/events')

@app.route('/events/all')
def posted_events():
    return render_template('posted_events.html', events=Event.get_all(), datetime=datetime)