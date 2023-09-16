from flask import Flask, render_template, session

app = Flask(__name__)

app.secret_key="secretkey"

@app.route('/')
def number_of_visits():
    if "visits" not in session:
        session["visits"] = 0
    else:
        session["visits"] += 1
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)