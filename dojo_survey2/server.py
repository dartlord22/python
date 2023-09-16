from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key="secretkey"

@app.route('/')
def survey():
    return render_template("survey.html")


@app.route('/process', methods = ['POST'])
def process():
    session['first_name'] = request.form['first_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/submittedinfo')
#session is used to send values from form over to our result page
#should always redirect on POST methods 

@app.route('/results')
def results():
    return render_template('results.html')
    
if __name__=="__main__":
    app.run(debug=True)