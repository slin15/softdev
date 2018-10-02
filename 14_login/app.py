# Team SillySquids : Robin Han and Susan Lin 
# SoftDev pd8
# K #14: Do I Know You?    this
# 2018-10-01

from flask import Flask, render_template, request, session, redirect, url_for
from os import urandom

app = Flask(__name__)

app.secret_key = urandom(32)

users = {"slin15": "12345"} 
       
@app.route('/', methods=["POST", "GET"])
def home():
     if not session.get('logged_in'):
          return render_template('form.html')
     else:
        return "Hello!"

@app.route('/login')
def login():
    user = request.args["in"]
    password = request.args["pass"]

    if user in users.keys() and users[user] == password:
        session['logged_in'] = True
    
    elif user not in users.keys():
        return render_template('error.html', error = "username not found")

    elif users[user] != password:
        return render_template('error.html', error = "incorrect password")

    else:
        return render_template('error.html', error = "just bad juju")

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.debug = True
    app.run()
